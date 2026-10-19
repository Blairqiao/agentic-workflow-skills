---
name: fast-track
description: Use for bounded small fixes, especially follow-up defects within approved behavior. Direct non-boost implementation without implementation subagents.
---

# Fast track

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `fast`.

## Fit and authorization boundary

Use direct non-boost execution for a bounded repair that fits a single linear task. A follow-up defect is a mismatch with approved behavior. New behavior is new scope even when the code change is small. File count alone does not establish fit. No implementation subagents are allowed. Read-only exploration is permitted under [discovery](../_workflow/discovery.md#code-exploration-and-delegation).

For an in-track follow-up in an active execution session, reuse the existing candidate checkout and exact parent plan. Inherit only authorization that covers the repair. State the defect, expected behavior, likely files, and verification inline in chat, then proceed without another approval. Do not turn diagnosis into an implicit promise that the repair remains small.

Standalone small fixes execute in a single chat. Write a two to three sentence mini-spec, numbered acceptance criteria, target files, and verification commands directly in `<main-repo>/.agent-docs/fast-track/<feature>.md` using [the fast-track template](../_workflow/templates/fast-track.md). Present the mini-spec inline in chat and pause for user approval before modifying code or tests. Always place a direct clickable link to the fast-track record at the very bottom of the chat response. No separate plan file is required for standalone fast-track.

## Escalation

If diagnosis requires a product decision, new dependency, migration, security change, architecture change, material risk, or multi-task coordination, stop dependent work and return the affected decision to the planning phase. Recommend [full-track](../full-track/SKILL.md) for wider implementation, or see [the Antigravity adapter](../_workflow/adapters/antigravity.md) for harness-specific orchestration. Continue independent authorized work. A revised ready plan needs a new execution instruction.

## Evidence and records

Add a focused regression test and observe its failure before a behavioral repair under [test integrity](../_workflow/testing.md). Record exact red and green commands and observed outputs. For purely visual issues, reproducible before-and-after browser evidence may prove the requirement more directly. Verify affected integration and rerun checks whose prior evidence the fix invalidates. Obtain focused [independent review](../_workflow/review.md) of the patch and integration boundary.

Append defect, cause, change, verification, review, and limitations to the parent's proof when available. Update affected parent task status and invalidated evidence. Do not duplicate the parent plan or create another taskboard for one fix. Without an active parent, keep the lean standalone record in `<main-repo>/.agent-docs/fast-track/<feature>.md`, updating it in place on retries.

Preserve user changes, make no execution commits, and follow [handoff](../_workflow/handoff.md). Cap failed implementation attempts and review-fix rounds at three each. On an in-place cap, restore only modified candidate files to their pre-task state and record failed approaches in the active proof or standalone record. Stage candidate changes at handoff and leave the final commit to the user.
