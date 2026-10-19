---
name: fast-track
description: Use for small fixes or simple additions. Standard model without boost capabilities or implementation subagents.
---

# Fast track

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `fast`.

## Fit check

Confirm the request fits small fixes or simple additions in the current workspace before starting:

- Scope is limited to making small fixes or simple additions, executed by the standard model without boost capabilities.
- Implementable as a single linear sequence in the current session without multi-step orchestration or implementation subagents.
- No new dependencies, database migrations, or changes to security or architectural boundaries.

Read-only code exploration subagents are permitted under [discovery](../_workflow/discovery.md#code-exploration-and-delegation). They do not count as implementation subagents or multi-step implementation orchestration. The orchestrator may read documentation directly.

If the request exceeds this scope at the start or during implementation, stop, explain what outgrew the fit check, and escalate to [full-track](../full-track/SKILL.md) or [orchestration-track](../orchestration-track/SKILL.md).

## Execution and documentation

Record the entire run in one lean documentation file at `<main-repo>/.agent-docs/fast-track/<feature>.md` using [the fast-track template](../_workflow/templates/fast-track.md) and a short, stable `<feature>` slug. Update the file in place on retries or follow-ups rather than creating separate spec, plan, taskboard, proof, or walkthrough files.

Write a two to three sentence mini-spec, numbered acceptance criteria, and target files in `<main-repo>/.agent-docs/fast-track/<feature>.md`, present them inline in chat, and pause for approval before editing code or tests. For follow-up defect reports, update the diagnosis and criteria in place, present them inline in chat, and pause for approval before modifying code.

Implement in the current session without making Git commits, preserving unrelated user changes. Follow [test integrity](../_workflow/testing.md) with recorded red and green command evidence, perform relevant UI verification, and obtain [independent review](../_workflow/review.md). If the three-attempt implementation or review-fix cap is reached, restore modified candidate files to their pre-task state while recording what was tried and what failed in `<main-repo>/.agent-docs/fast-track/<feature>.md`. At handoff, stage candidate changes and leave the final commit to the user.
