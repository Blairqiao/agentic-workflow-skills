---
name: one-shot
description: Use only when the user explicitly requests one-shot or autonomous execution from one prompt without human feedback.
---

# One-shot

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `one-shot`.

Start immediately. Make product and implementation decisions using your best judgment; record material choices, assumptions, alternatives, and reasons in the run document. Do not ask for confirmation, preference selection, design feedback, spec approval, plan approval, or test-design approval. Do not invoke interactive grilling or human-guided TDD during this run.

Pause only for critical missing access or additional authorization. Reuse existing authorization. Ordinary product ambiguity, review disagreements, and local test or snapshot revisions are decisions to resolve autonomously.

Prefer a worktree. Delegate independent implementation tasks when useful and obtain independent review. If no independent reviewer can run, disclose self-review. If technical alternatives are exhausted, deliver an honest incomplete result without requesting design feedback.

Leave a run document containing the design decisions, plan, progress, proof, and walkthrough. Stage candidate changes, report limitations, and leave publishing and the final target-branch commit to the user.
