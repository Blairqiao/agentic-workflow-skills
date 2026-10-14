# Agent Guidelines: Agentic Workflow

> These rules enforce rigorous behavior, planning, test-driven execution, verification, and safety across all projects and tasks using the agentic workflow.

## Core Behaviors

1. **Evidence Over Assertions:** Never claim a bug is fixed or a feature works without running the relevant test or command and observing the output. Provide the terminal proof.
2. **Design First & Track Policy:** Do not write implementation code for complex features without a plan. Read `<main-repo>/.agent-docs/CONTEXT.md` if present, and if architectural or domain terminology decisions are needed, invoke `grilling` or `domain-modeling`. Select the appropriate track:
   - `full-track`: Prefer an isolated worktree (`.worktrees/<run-id>`); produce a detailed spec, plan, taskboard, proof, and walkthrough in `<main-repo>/.agent-docs/` with one combined spec-and-plan approval.
   - `fast-track`: Scoped to one-off bug fixes, minor UI adjustments, and small self-contained changes in the **current workspace** without implementation subagents. Record the mini-spec, acceptance criteria, `S0`/`S1`/`S2` tree snapshots, review verdict, and proof in `<main-repo>/.agent-docs/fast-track/<feature>.md`, pause for mini-spec approval, and escalate to `full-track` if scope outgrows a single task.
   - **Approval Gates & Inline Presentation:** Every approval gate (initial or follow-up defect/pivot) must display the plan or mini-spec inline in chat (scope, affected files, technical strategy, acceptance criteria) and pause for explicit approval before editing code or tests. 
   - `one-shot`: Start immediately without feedback gates; record autonomous decisions, plan, progress, proof, and walkthrough in `<main-repo>/.agent-docs/runs/<feature>.md`.
   - Cap failed task implementation attempts at 3 and review-fix cycles at 3 rounds across all tracks.
3. **No Phantom Edits:** Preserve all existing comments, docstrings, and unrelated logic when making edits. Only modify what is strictly in scope.
4. **Testing Modes & Track-Aware TDD Integrity:** Default to Autopilot TDD for behavior changes unless the user requests `human-tdd` (`one-shot` always runs Autopilot).
   - **In an isolated worktree (`full-track`, `one-shot`):** Enforce `test(red)` and `feat(green)` commits; the test code diff between red and green must be strictly empty (`git diff --stat <red>..<green> -- <test-paths>` prints nothing). Every `test(amend)` must be listed in the proof and explicitly accepted by the reviewer.
   - **In the current workspace (`fast-track` or in-place runs):** Do not make intermediate commits so `HEAD` and pre-existing user changes stay untouched. Capture temporary-index `git write-tree` snapshots `S0` at task start, `S1` after red, and `S2` after green, verify `git diff --stat "$S1" "$S2" -- <test-paths>` prints nothing, and pass `git diff "$S0" "$S2"` to the reviewer.
5. **Clean Handoff & Git Safety:** Never commit directly to the target branch, deploy, or run `git push`. For in-place runs, stage candidate changes; for isolated worktree runs, keep `test(red)` and `feat(green)` commits on the worktree branch and provide the worktree path, branch name, and `git merge --squash <worktree-branch>` command for the user.

## Execution & Verification Standards

1. **Workflow Tool Skills:** Leverage specialized workflow skills according to task needs:
   - `domain-modeling`: Build and maintain the shared domain dictionary in `<main-repo>/.agent-docs/CONTEXT.md`.
   - `grilling`: Stress-test thinking, architectural decisions, and tradeoffs before implementation.
   - `human-tdd`: Align collaboratively with the user on test cases (`[Specific]`, `[Intermediate]`, `[Global]`) before coding.
   - `unslop`: Strip AI fluff, buzzwords, and boilerplate from written artifacts while preserving code, commands, and logs.
   - `research`: Explain codebase architecture or audit maintained code against existing documentation.
2. **Worktree Placement, Parent-Repo `.agent-docs/`, & Ignore Discipline:** Put worktrees in `<main-repo>/.worktrees/<run-id>`, and place all workflow documentation (`CONTEXT.md`, `CONTEXT-MAP.md`, `spec/`, `plans/`, `taskboard/`, `proofs/`, `walkthroughs/`, `fast-track/`, `runs/`) in the parent repository at `<main-repo>/.agent-docs/` directly by path, never as isolated files or symlinks inside a worktree. Before creating a worktree or writing `.agent-docs/`, ensure both `.worktrees` (`.worktrees/*`, `.worktrees`) and `.agent-docs` (`.agent-docs/*`, `.agent-docs`) are added to `<main-repo>/.gitignore` and `<main-repo>/.git/info/exclude`, and add root-anchored `.worktrees` exclusions to glob-based project tool configs. Never create worktrees inside harness directories (`.codex`, `.claude`, `.gemini`).
3. **Subagent Model Tiering:** When dispatching subagents in Antigravity or multi-agent runners:
   - **Task Implementer:** `"flash"` (fast generation, low thinking overhead, strictly scoped to one task; not used in `fast-track`).
   - **Explorer / Scanner:** `"flash_lite"` (minimal reasoning, directory scans, symbol grepping).
   - **Task Reviewer & Auditor:** `"inherit"` or `"pro"` (high reasoning budget, adversarial spec compliance, anti-gaming checks; required across all tracks including `fast-track`).
   - **Fix Escalation:** Promoted to `"inherit"` / `"pro"` after round 2, capped at 3 attempts/rounds.
4. **Multimodal UI Verification:** For any web or UI tasks, do not rely solely on compiler or build passes (`tsc --noEmit`). Use `agent-browser` with accessibility snapshots (`agent-browser snapshot -i`) and annotated screenshots (`agent-browser screenshot --annotate`) to verify layout, mobile viewports (390x844), and interactive elements. Embed all referenced screenshot proofs in markdown documentation directly using markdown image syntax (`![<Descriptive Caption>](<path-to-image.png>)`) rather than raw file paths or plain text links.

## Transparency & Honesty

1. **Admit Knowledge Gaps:** If you don't know how to do something, or if the documentation is missing, be honest. Do not hallucinate APIs or guess.
2. **Disclose Shortcuts & Debt:** If you take a shortcut to accomplish a goal, or if your solution introduces technical debt or performance risks, explicitly flag it.
3. **No Silent Assumptions:** If a requirement is vague, stop and ask (unless in `one-shot`, where you record the decision and rationale in `.agent-docs/runs/<feature>.md`).
4. **No "Yes-Man" Behavior:** If a suggested approach is flawed, insecure, or violates project architecture, respectfully push back and explain why before implementing it.

## Guardrails & Safety

1. **No Placeholders:** Write complete code. Never leave `// TODO`, `/* implement here */`, or truncated snippets unless explicitly told we are prototyping.
2. **Dependency Discipline:** Do not install new dependencies or third-party packages without prior confirmation and justification.
3. **Destructive Action Safety:** Never run destructive git operations (`git reset --hard`, `git push --force`), drop databases, or delete directories without explicit user confirmation.
