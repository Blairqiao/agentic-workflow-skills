---
name: retro
description: Learn from past agent chat logs to cut repeated human work. Cheap readers scan distilled T3 Code threads for repeated requests, corrections, and manual relays. The main agent turns the cross-project patterns into ranked workflow changes such as skill edits, rules, hooks, or scripts. Use when the user asks for a retro, to learn from chat logs, or to find what they keep repeating. Not for project-specific bugs.
---

# Retro

Find work the human keeps doing by hand across sessions, and propose workflow changes that remove it. The output is a short list of changes ranked by human time saved, not a summary of what happened.

Stay at the workflow level. A finding counts only if it would come up in any project: how the human starts work, steers agents, reviews, commits, or hands off. One project's bugs, data, or design choices are out of scope, even when they come up often.

Run this as a strong model (Opus or Astra). Cheap readers do the reading. You do the thinking.

## 1. Scope

Look for earlier retros in `.agent-docs/retros/`. If one exists, default `--since` to its date, and note what it proposed and what the user accepted or rejected, so you don't propose the same change twice. With no earlier retro, cover the last 30 days unless the user names a window.

## 2. Distill

The source is T3 Code's state database (`~/.t3/userdata/statev2.sqlite`), which holds every thread across every provider T3 runs. Shrink it first:

```sh
python3 -I <skill dir>/distill.py --out .agent-docs/retros/work --since <YYYY-MM-DD>
```

It opens the database read-only. It keeps the messages T3 records as written by the human, the end of the agent reply before each one, where the human interrupted a run, how often the agent stopped to ask, and tool counts. It skips subagent threads and messages written by agents or the server. It redacts obvious secrets. It writes one text file per thread and splits them into batches of about 120 KB in `batches.txt`. Work done outside T3 isn't covered. Say so in the report.

Read the printed summary. If almost everything is one project, tell the user the patterns may not generalize.

## 3. Read with cheap models

Send each line of `batches.txt` to its own reader, all in parallel, using [reader-prompt.md](reader-prompt.md). Readers are read-only.

- **Model.** The cheapest capable one: Gemini Flash through `delegate_task` in T3 Code, Haiku through `Agent` in Claude Code, or a mini model through `spawn_agent` in Codex.
- **Privacy.** The logs go to the reader's provider. Logs hold whatever the user pasted. If the user hasn't used a cross-provider reader before, ask once before sending logs to a different provider than the one you're running on.
- Don't read the session files yourself at this stage. That's what the readers are for.

## 4. Synthesize

This is the part that needs a strong model.

1. **Merge.** Readers name the same pattern differently. Cluster their findings and add up sessions and projects per cluster.
2. **Filter.** Keep a cluster only if it appears in at least 3 sessions and 2 projects, or is a correction the human made with visible frustration. Drop anything project-specific.
3. **Verify.** For each cluster you keep, open 2 of the cited session files and check that the quotes exist and mean what the reader said. Cheap readers over-report. Drop what doesn't hold up.
4. **Find the cause.** Ask why the human had to do it. Read the skill, rule, or config involved before blaming it. Typical causes: a skill doesn't say to do the step, a rule lives only in the human's head, the agent stops to ask when it could act, no hook or script exists, or two skills disagree.
5. **Pick the cheapest fix that removes the repetition:**

| Fix | When |
| --- | --- |
| Edit an existing skill | The step belongs to a skill that leaves it out or gets it wrong |
| Rule in AGENTS.md or CLAUDE.md | A preference that applies everywhere and is short |
| Hook or permission allowlist | Something that should always or never happen, with no judgment needed |
| Script | A mechanical sequence the human or agent repeats |
| New skill | A recurring multi-step task with no home. Rarely the right answer |
| Nothing | Repetition that's cheap, or where the human's judgment is the point |

Prefer removing a step to automating it. Prefer one change that fixes several patterns over one change each.

## 5. Report

Write `.agent-docs/retros/<YYYY-MM-DD>.md`:

- **Window:** dates, thread count, and projects.
- **Changes**, ranked by estimated human turns saved per week. For each: the pattern, the evidence (counts plus 2 quotes with session file names), the cause, the exact change (file and wording, or a diff sketch), and the risk.
- **Considered and dropped:** patterns that looked real but failed verification or were project-specific, one line each.
- **Last retro's changes:** whether the patterns they targeted have gone down.

Apply `unslop`. Delete `.agent-docs/retros/work/` afterwards, since it holds log excerpts.

In chat, list the changes in one line each and ask which to apply. Apply only what the user picks. Changes to skills in this repository get committed, staging only the files you touched. Ask before editing global config such as `~/.claude/settings.json`. Record which changes were accepted at the bottom of the report, so the next retro can check them.
