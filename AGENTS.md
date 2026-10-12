# Agent Guidelines: Agentic Workflow Skills

> These rules enforce rigorous behavior, planning, verification, and multi-harness portability across this repository.

## Core Behaviors

1. **Evidence Over Assertions:** Never claim a bug is fixed or a feature works without running the relevant test or command and observing the output. Provide the terminal proof.
2. **Design First & Track Policy:** Do not write implementation code for complex features without a plan. Read `CONTEXT.md` if present, and if architectural decisions are needed, invoke `grilling` or `domain-modeling`.
   - `full-track`: Prefer an isolated worktree (`.worktrees/<run-id>`); produce a detailed spec, plan, taskboard, proof, and walkthrough with one combined spec-and-plan approval.
   - `fast-track`: Produce the same full spec, plan, taskboard, proof, walkthrough, combined approval, and independent review as `full-track`, but execute in the **current workspace** without implementation subagents.
   - `one-shot`: Start immediately without feedback gates; record autonomous decisions, plan, progress, proof, and walkthrough in `docs/runs/<feature>.md`.
3. **No Phantom Edits:** Preserve all existing comments, docstrings, and unrelated logic when making edits. Only modify what is strictly in scope.
4. **Testing Modes & Track-Aware TDD Integrity (Option C):** Default to Autopilot TDD for behavior changes unless the user requests `human-tdd` (one-shot always runs Autopilot).
   - **In an isolated worktree (`full-track`, `one-shot`):** Enforce `test(red)` and `feat(green)` commits; the test code diff between red and green must be strictly empty (`git diff --stat <red>..<green> -- <tests> == 0`).
   - **In the current workspace (`fast-track` or in-place runs):** Do not make intermediate commits so `HEAD` and pre-existing user changes stay untouched; verify red and green via terminal output and rely on independent review to audit the test diff.
5. **Clean Handoff & Git Safety:** Never commit directly to the target branch, deploy, or run `git push`. Stage candidate changes and present verification proof for the user to make the final commit.

## Multi-Harness Skill Authoring & Standards

1. **Open `SKILL.md` Format & `_workflow/` Architecture:** Expose only the 6 public entry/tool skills (`full-track`, `fast-track`, `one-shot`, `grilling`, `human-tdd`, `unslop`) with `SKILL.md` files containing only `name` and `description` in YAML frontmatter. Internal phase procedures live in `skills/_workflow/` (no `SKILL.md`) with harness specifics isolated in `skills/_workflow/adapters/`.
2. **Worktree Placement, Parent-Repo `docs/`, & `.gitignore` Discipline:** Put worktrees in `<main-repo>/.worktrees/<run-id>`, and place all workflow documentation (`docs/spec/`, `docs/plans/`, `docs/taskboard/`, `docs/proofs/`, `docs/walkthroughs/`, `docs/runs/`) in the parent (main) repository at `<main-repo>/docs/`—never as isolated files inside a worktree (when inside a worktree, either write directly to `<main-repo>/docs/` or symlink `<worktree>/docs` to `<main-repo>/docs`). Whenever creating or updating `.gitignore`, ensure both `.worktrees` (`.worktrees/*`, `.worktrees`) and `docs` (`docs/*`, `docs`) are added to the repository's root `.gitignore` so all files inside those folders are hidden from Git. Never create worktrees inside harness directories (`.codex`, `.claude`, `.gemini`).
3. **Subagent Model Tiering:** When dispatching subagents in Antigravity or multi-agent runners (per `skills/_workflow/adapters/antigravity.md`):
   - **Task Implementer:** `"flash"` (fast generation, low thinking overhead, strictly scoped to one task; not used in `fast-track`).
   - **Explorer / Scanner:** `"flash_lite"` (minimal reasoning, directory scans, symbol grepping).
   - **Task Reviewer & Auditor:** `"inherit"` or `"pro"` (high reasoning budget, adversarial spec compliance, anti-gaming checks; required across all tracks including `fast-track`).
   - **Fix Escalation:** Promoted to `"inherit"` / `"pro"` after round 2.
4. **Multimodal UI Verification:** For any web or UI tasks, do not rely solely on compiler or build passes (`tsc --noEmit`). Use `agent-browser` with accessibility snapshots (`agent-browser snapshot -i`) and annotated screenshots (`agent-browser screenshot --annotate`) to verify layout, mobile viewports (390x844), and interactive elements.
5. **Installer Validation:** Validate any changes to `install.sh` or bundle structure with `python3 -B -m unittest discover -s tests -v` and `bash -n install.sh`.

## Transparency & Honesty

1. **Admit Knowledge Gaps:** If you don't know how to do something, or if the documentation is missing, be honest. Do not hallucinate APIs or guess.
2. **Disclose Shortcuts & Debt:** If you take a shortcut to accomplish a goal, or if your solution introduces technical debt or performance risks, explicitly flag it.
3. **No Silent Assumptions:** If a requirement is vague, stop and ask (unless in `one-shot`, where you record the decision and rationale in `docs/runs/<feature>.md`).
4. **No "Yes-Man" Behavior:** If a suggested approach is flawed, insecure, or violates our architecture, respectfully push back and explain why before implementing it.

## Guardrails & Safety

1. **No Placeholders:** Write complete code. Never leave `// TODO`, `/* implement here */`, or truncated snippets unless explicitly told we are prototyping.
2. **Dependency Discipline:** Do not install new dependencies or third-party packages without prior confirmation and justification.
3. **Destructive Action Safety:** Never run destructive git operations (`git reset --hard`, `git push --force`), drop databases, or delete directories without explicit user confirmation.
