#!/usr/bin/env python3
"""Distill T3 Code threads into small text transcripts for the retro skill.

Reads T3 Code's state database (read-only). Covers every provider T3 runs: Claude, Codex,
Antigravity, and others. Keeps messages the human wrote (createdBy = "user"), a short tail of
the agent reply before each one, interrupts, and tool counts. Skips subagent threads and
messages written by agents or the server. Redacts obvious secrets.

Usage: distill.py --out DIR [--since YYYY-MM-DD] [--batch-kb 120] [--db PATH]
Writes DIR/sessions/*.txt, DIR/batches.txt (one line of session files per batch), and prints a summary.
"""
import argparse, collections, json, os, re, sqlite3, sys
from urllib.parse import quote

DEFAULT_DB = os.path.expanduser("~/.t3/userdata/statev2.sqlite")
INJECTED = re.compile(
    r"<(system-reminder|environment_context|local-command-stdout|local-command-stderr|command-message|user_instructions|permissions instructions|turn_aborted)>.*?</\1>",
    re.S,
)
INJECTED_PREFIXES = ("# AGENTS.md instructions", "<environment_context>", "<user_instructions>", "Caveat:")
SECRET = re.compile(
    r"(sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|gh[ousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[abpr]-[A-Za-z0-9-]{10,}"
    r"|eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)
MAX_USER = 1500   # chars kept per human message
MAX_TAIL = 300    # chars kept from the agent reply before it


def clean(text):
    text = SECRET.sub("[REDACTED]", INJECTED.sub("", text or "")).strip()
    if text.startswith(INJECTED_PREFIXES):
        return ""
    return re.sub(r"\n{3,}", "\n\n", text)


def clip(text, n):
    return text if len(text) <= n else text[:n] + " […]"


def js(raw):
    try:
        return json.loads(raw or "{}")
    except ValueError:
        return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--since", help="only threads updated on or after this date (YYYY-MM-DD)")
    ap.add_argument("--batch-kb", type=int, default=120, help="target size of each reader batch")
    ap.add_argument("--db", default=DEFAULT_DB, help="T3 state database")
    a = ap.parse_args()

    if not os.path.exists(a.db):
        sys.exit(f"T3 database not found: {a.db}")
    db = sqlite3.connect(f"file:{quote(a.db)}?mode=ro", uri=True)

    projects = {pid: (title, root) for pid, title, root in db.execute(
        "select project_id, title, workspace_root from projection_projects")}

    threads = db.execute(
        """select thread_id, project_id, title, default_provider, created_at, payload_json
           from orchestration_v2_projection_threads
           where deleted_at is null and updated_at >= ? order by created_at""",
        (a.since or "",),
    ).fetchall()

    os.makedirs(f"{a.out}/sessions", exist_ok=True)
    written, counts, per_project = [], collections.Counter(), collections.Counter()
    for tid, pid, title, provider, created, payload in threads:
        meta = js(payload)
        if (meta.get("lineage") or {}).get("relationshipToParent") == "subagent":
            counts["subagent"] += 1
            continue

        msgs = db.execute(
            "select role, run_id, payload_json from orchestration_v2_projection_messages "
            "where thread_id = ? and streaming = 0 order by created_at, message_id", (tid,))
        items = db.execute(
            "select type, run_id, payload_json from orchestration_v2_projection_turn_items where thread_id = ?",
            (tid,)).fetchall()

        tools, interrupted = collections.Counter(), set()
        for kind, run, ipayload in items:
            if kind == "dynamic_tool":
                name = js(ipayload).get("toolName") or "tool"
                tools["question" if " " in name else name] += 1  # some providers store the question as the name
            elif kind in ("command_execution", "file_change", "web_search", "subagent"):
                tools[kind] += 1
            elif kind == "run_interrupt_request":
                interrupted.add(run)
        asked = sum(1 for k, _, _ in items if k == "user_input_request")

        turns, reply, reply_run = [], "", None
        for role, run, mpayload in msgs:
            m = js(mpayload)
            text = clean(m.get("text"))
            if role == "assistant":
                if text:
                    reply, reply_run = text, run
            elif role == "user" and m.get("createdBy") == "user" and text:
                turns.append((reply, reply_run in interrupted, text))
                reply, reply_run = "", None
        if not turns:
            counts["no human messages"] += 1
            continue

        ptitle, root = projects.get(pid, ("unknown", ""))
        model = (meta.get("modelSelection") or {}).get("model") or provider
        date = (created or "")[:10]
        per_project[ptitle] += 1
        safe = re.sub(r"[^A-Za-z0-9._-]", "-", ptitle)[:40]
        name = f"{date}_{safe}_{re.sub(r'[^A-Za-z0-9]', '', tid)[-8:]}.txt"
        tool_line = ", ".join(f"{k} {v}" for k, v in tools.most_common(12)) or "none"
        lines = [
            f"# {ptitle} | {clip(clean(title), 80)} | {date} | {model} | {len(turns)} human turns",
            f"# tools: {tool_line} | agent asked the human {asked} times | human interrupted {len(interrupted)} runs",
            "",
        ]
        for i, (prev, was_interrupted, user) in enumerate(turns, 1):
            if prev:
                lines.append(f"[agent, end of reply] {clip(prev[-MAX_TAIL:], MAX_TAIL)}")
            if was_interrupted:
                lines.append("[human interrupted the agent here]")
            lines.append(f"[human {i}] {clip(user, MAX_USER)}")
            lines.append("")
        body = "\n".join(lines)
        with open(f"{a.out}/sessions/{name}", "w") as f:
            f.write(body)
        written.append((name, len(body)))

    batches, cur, size = [], [], 0
    for name, n in written:
        if cur and size + n > a.batch_kb * 1024:
            batches.append(cur)
            cur, size = [], 0
        cur.append(name)
        size += n
    if cur:
        batches.append(cur)
    with open(f"{a.out}/batches.txt", "w") as f:
        f.write("".join(" ".join(b) + "\n" for b in batches))

    total = sum(n for _, n in written)
    skipped = ", ".join(f"{v} {k}" for k, v in counts.items()) or "none"
    print(f"threads: {len(written)} kept, skipped {skipped}")
    print(f"distilled: {total // 1024} KB in {len(batches)} batches of ~{a.batch_kb} KB")
    print("projects: " + ", ".join(f"{p} {n}" for p, n in per_project.most_common()))


if __name__ == "__main__":
    sys.exit(main())
