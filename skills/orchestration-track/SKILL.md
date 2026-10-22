---
name: orchestration-track
description: Use for large multi-part initiatives, project jumpstarts, complex multi-service features, or full codebase audits and refactors. Delegate vertical implementation slices while coordinating architecture, dependencies, and verification.
---

# Orchestration track

Apply [workflow core](../_workflow/core.md), including supplied-context reuse. Load the active adapter and procedure details only for the current operation; linked procedures are references.

Automatically select this track for large multi-part initiatives, project jumpstarts, complex multi-service features, and full codebase audits or refactors. Use custom non-boost coordination. Keep runner-specific capabilities in the active adapter and disclose unavailable tools or model selection.

The planning phase writes the ready plan at `<main-repo>/.agent-docs/plans/<feature>.md` and presents scope, affected files, strategy, vertical slices, and acceptance criteria inline with the plan link at the bottom. Execution requires the user's instruction to execute that named ready plan. Validate revision, checkout, starting state, and protected edits, then execute without repeating approval or interviews. Ready status alone grants no permission.

Maintain the taskboard and proof under the parent repository's `.agent-docs/`, with the same execution slug as the plan. Prepare an isolated candidate at `<main-repo>/.worktrees/<feature>` under [workspace preparation](../_workflow/workspace.md).

Mandate subagent delegation for implementation. The coordinator owns architecture, dependencies, integration, and quality gates. Divide work into vertical slices that each deliver an end-to-end behavior with acceptance criteria, target files, and verification commands. Concurrent slices require disjoint file scopes and isolated resources. Use [implementer briefs](../_workflow/templates/implementer-brief.md) and the active adapter's supported capability tiers.

Apply [execution](../_workflow/execution.md), [test integrity](../_workflow/testing.md), and [independent review](../_workflow/review.md) when those operations begin. Review completed slices and the unified candidate. Record observed red and green outputs, test amendments, and missing evidence. Apply core's three-attempt and three-review-round caps.

Material changes return to planning and require renewed execution authorization. Every interactive follow-up repair needs its own inline mini-spec approval before code or test edits under core. Follow [verification](../_workflow/verification.md) and [handoff](../_workflow/handoff.md), stage the candidate, and leave commits and integration to the user.
