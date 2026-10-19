---
name: full-track
description: Use for isolated features and debugging beyond a bounded repair. Complete non-boost workflow with delegated implementation and independent review.
---

# Full track

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `full`.

## Scope and records

Use full-track as the non-boost default for feature work and debugging beyond [fast-track](../fast-track/SKILL.md). The custom orchestrator owns implementation delegation, task dependencies, evidence, and review.

Maintain the ready plan at `<main-repo>/.agent-docs/plans/<feature>.md`, the taskboard at `<main-repo>/.agent-docs/taskboard/<feature>.md`, and proof with walkthrough at `<main-repo>/.agent-docs/proofs/<feature>.md`. Scale record detail to task size. Concurrent runs use a distinct execution slug consistently across records, images, and workspace references.

## Plan adoption and execution entry

The planning phase writes the complete plan and presents its scope, affected files, strategy, and acceptance criteria inline in chat with the plan link at the bottom. Execution starts when the user instructs execution of the named ready plan. That instruction authorizes its scope. Load and validate the plan against the starting revision and protected edits, then execute without repeating approval or interviews. A ready status alone is not authorization. Consequential unresolved blockers prevent execution.

Material scope changes return to the planning phase. Record the affected blocker and continue independent authorized work. A revised plan requires a new execution instruction for the changed scope. Bounded defects within approved behavior can use fast-track and append evidence to the parent proof.

## Execution and handoff

Prefer an isolated candidate worktree at `<main-repo>/.worktrees/<feature>`. Mandate subagent delegation for task implementation. The orchestrator assigns bounded tasks through [implementer briefs](../_workflow/templates/implementer-brief.md), coordinates dependencies, and verifies integration. Use supported standard coding models through [the adapter](../_workflow/adapters/antigravity.md). Obtain [independent review](../_workflow/review.md) of the candidate, with earlier reviews for high-risk boundaries. Follow [test integrity](../_workflow/testing.md), autopilot TDD unless human-guided testing was requested, and [verification](../_workflow/verification.md).

Cap failed implementation attempts at three and review-fix rounds at three. Preserve unrelated edits and record failures. Follow [handoff](../_workflow/handoff.md), leaving publishing and the final target-branch commit to the user. Load linked procedures when their phase begins.
