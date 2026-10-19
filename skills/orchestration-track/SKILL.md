---
name: orchestration-track
description: Use for large multi-part initiatives, project jumpstarts, complex multi-service features, or full codebase audits and refactors. Designed for the frontier orchestrator, Gemini 4 Argon, enhanced by user-invoked /boost, managing strategic alignment, vertical slice decomposition, and quality gatekeeping while delegating vertical implementation slices to smaller subagents.
---

# Orchestration track

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `orchestration`.

## Scope and purpose

Use orchestration-track for large multi-part initiatives, project jumpstarts, complex multi-service features, or full codebase audits and refactors. The track is designed for the frontier orchestrator, Gemini 4 Argon, enhanced by user-invoked `/boost`.

When executing under `/boost`, standard workflow invariants apply: worktree isolation in `<main-repo>/.worktrees/<feature>`, `.agent-docs/` tracking artifacts, evidence-based red-before-green TDD, and independent review.

The track operates with a clear role division:
- **Frontier orchestrator Gemini 4 Argon.** Manages user alignment, overall architecture, vertical slice decomposition, dependency tracking, quality gates, and final synthesis. To preserve high-reasoning context and minimize token burn, the orchestrator avoids direct code implementation.
- **Implementation subagents `flash` or `flash_lite`.** Dispatched via `invoke_subagent` to implement discrete, vertically sliced units of work. If a slice fails verification after two attempts, escalate the task implementation to `Model: "pro"`.

## Vertical slice decomposition

Instead of horizontal layering such as implementing all database models first, then backend APIs, then frontend UI, divide the initiative into **vertical slices** on [the taskboard](../_workflow/templates/taskboard.md):
- Each vertical slice delivers a functional, end-to-end increment of behavior combining data model, business logic, API or UI, and tests.
- Each slice is self-contained with explicit acceptance criteria, target files, and verification commands.
- Independent slices can be delegated concurrently if file scopes are strictly disjoint.

## Workflow documents

Maintain three workflow documents in `<main-repo>/.agent-docs/` using a short, stable `<feature>` slug:
- `<main-repo>/.agent-docs/plans/<feature>.md` for the combined specification and implementation plan.
- `<main-repo>/.agent-docs/taskboard/<feature>.md` for task orchestration, vertical slices, progress, and the review verdict.
- `<main-repo>/.agent-docs/proofs/<feature>.md` for the combined verification proof and change walkthrough.

## Execution and approval gates

1. **Workspace isolation.** Always execute in an isolated worktree at `<main-repo>/.worktrees/<feature>`. Configure `.worktrees` and `.agent-docs` ignore patterns in `<main-repo>/.git/info/exclude` before creating worktrees or writing `.agent-docs/` files.
2. **Approval gate and inline presentation.** Present the combined spec and plan inline in chat covering scope, affected files, technical strategy, vertical slice breakdown, and acceptance criteria. Pause for explicit user approval before editing code or tests. For follow-up rounds or defect fixes that alter the approach, update the plan in place, present the revised approach inline in chat, and obtain approval before editing code.
3. **Delegated implementation.** Dispatch each vertical slice using `invoke_subagent` with [a scoped implementer brief](../_workflow/templates/implementer-brief.md), workspace path, and verification commands. Require each subagent to run autopilot TDD, recording red failure and green pass outputs, and report evidence.
4. **Independent review.** Require independent review of completed slices and the final unified candidate using [the reviewer brief](../_workflow/templates/reviewer-brief.md).
5. **Clean handoff.** Follow [integration and handoff](../_workflow/handoff.md). Never run `git commit` on the target branch. Provide the worktree path, branch name, and complete merge instructions for the user.
