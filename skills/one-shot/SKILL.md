---
name: one-shot
description: Use only when the user explicitly requests one-shot or autonomous execution from one prompt without human feedback. Autonomous track leveraging boost capabilities.
---

# One-shot

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `one-shot`.

## Scope and autonomous execution

Use one-shot only when explicitly requested by the user. One-shot is an autonomous execution track from a single prompt that leverages boost capabilities to deliver end-to-end changes without interactive human feedback gates.

Start immediately. Make product and implementation decisions using your best judgment, and record material choices, assumptions, alternatives, and reasons in `<main-repo>/.agent-docs/runs/<feature>.md`. Do not ask for confirmation, preference selection, design feedback, spec approval, plan approval, or test-design approval. Do not invoke interactive grilling or human-guided TDD during this run.

Pause only for critical missing access or additional authorization. Reuse existing authorization. Resolve ordinary product ambiguity, review disagreements, and local test or snapshot revisions autonomously.

Prefer an isolated worktree at `<main-repo>/.worktrees/<feature>`, using a distinct `<run-id>` only when needed to avoid colliding with an active worktree. When running under an active `/boost` session, enforce all standard workflow invariants: keep candidate changes confined to `<main-repo>/.worktrees/<feature>`, maintain workflow records in `/.agent-docs/`, capture verbatim red and green test evidence, and obtain independent review. Delegate independent implementation tasks when useful and obtain independent review. If no independent reviewer can run, disclose self-review. If technical alternatives are exhausted or retry caps are reached, deliver an honest incomplete result without requesting design feedback. For in-place runs that hit a retry cap, restore modified candidate files to their pre-task state while recording what was tried and why it failed.

Maintain the single run document at `<main-repo>/.agent-docs/runs/<feature>.md` containing the design decisions, plan, progress, review, proof, and walkthrough. Report limitations and leave publishing and the final target-branch commit to the user.
