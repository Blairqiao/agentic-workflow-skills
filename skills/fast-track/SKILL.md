---
name: fast-track
description: Use when the user explicitly requests fast-track for a one-off bug fix, minor UI adjustment, or small self-contained change in the current workspace.
---

# Fast track

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `fast`.

## Fit check

Confirm the request fits a localized bug fix, minor UI adjustment, or small self-contained change before starting:

- No new dependencies, database migrations, or changes to security or architectural boundaries.
- Implementable as a single focused task in the current workspace without implementation subagents.

If the request exceeds this scope at the start or during implementation, stop, explain what outgrew the fit check, and recommend switching to [full-track](../full-track/SKILL.md).

## Execution and documentation

Record the entire run in one file at `<main-repo>/.agent-docs/fast-track/<feature>.md` using [the fast-track template](../_workflow/templates/fast-track.md). Do not create separate spec, plan, taskboard, proof, or walkthrough files.

Write a two to three sentence mini-spec and numbered acceptance criteria in `<main-repo>/.agent-docs/fast-track/<feature>.md` and pause once for user approval before editing code. Implement in the current session, preserving existing user changes. Enforce deterministic [test integrity](../_workflow/testing.md) with temporary-index `S0`, `S1`, and `S2` tree snapshots, relevant UI verification, and mandatory [independent review](../_workflow/review.md). Stage only candidate changes and leave the final commit to the user.
