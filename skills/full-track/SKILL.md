---
name: full-track
description: Use for adding isolated features whether large or medium, or debugging specific parts of a program. Standard model with boost capabilities and mandated subagent delegation.
---

# Full track

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `full`.

## Scope and purpose

Use full-track for adding isolated features, whether large or medium, or debugging specific parts of a program. It employs the standard model with boost capabilities and mandates subagent delegation for task implementation.

Maintain three workflow documents in `<main-repo>/.agent-docs/` using a short, stable `<feature>` slug:

- `<main-repo>/.agent-docs/plans/<feature>.md` for the combined specification and implementation plan.
- `<main-repo>/.agent-docs/taskboard/<feature>.md` for task orchestration, progress, and the review verdict.
- `<main-repo>/.agent-docs/proofs/<feature>.md` for the combined verification proof and change walkthrough.

## Execution and approval gates

Present the combined spec and plan inline in chat for approval before implementation. For follow-up rounds or defect fixes that alter the approach, update the plan in place, present the revised approach inline in chat, and obtain approval before editing code. Resolve consequential questions beforehand and reuse prior approval only within its original scope.

Prefer an isolated worktree at `<main-repo>/.worktrees/<feature>`, or use a distinct `<run-id>` only when concurrent executions require separate checkouts. Mandate subagent delegation for task implementation; the orchestrator coordinates task assignments, dependencies, and review rather than implementing code directly. Require independent review of the completed candidate, with earlier reviews for high-risk tasks. Use autopilot TDD unless the user requests human-guided testing.

Load each linked procedure when its phase begins. Deliver verified candidate changes and complete documentation, leaving publishing and the final target-branch commit to the user.
