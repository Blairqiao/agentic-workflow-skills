---
name: one-shot
description: Use only when explicitly requested for autonomous planning and implementation from one prompt. Supports native boost and non-boost execution without interactive feedback gates.
---

# One-shot

Apply [workflow core](../_workflow/core.md), including supplied-context reuse. Load the active adapter and procedure details only for the current operation; do not recursively load linked documents.

## Autonomous exception and executor

Use one-shot only when explicitly requested by the user. It combines autonomous planning and implementation from a single prompt without interactive approval, interviews, grilling, or human-guided test design. Start immediately and record consequential decisions, assumptions, alternatives, and reasons.

Support both boost and non-boost execution. Record the selected executor in the single run document at `<main-repo>/.agent-docs/runs/<feature>.md` before implementation. Honor the user's executor choice. When none is specified, use native boost only if the user has already activated it, otherwise select non-boost and record why. Do not silently switch executors.

For boost execution, the user must invoke `/boost`; a skill cannot activate it. The native boost owns decomposition, worker dispatch, model allocation, implementation, and iterative verification. Apply the active adapter's evidence and ownership contract with autonomous planning in this run document replacing separate planning and execution sessions. If the requested executor is unavailable, report the blocker and await an explicit executor change rather than claiming fallback success.

For non-boost execution, use custom coordination through [execution](../_workflow/execution.md). Delegate independent implementation tasks when useful and obtain [independent review](../_workflow/review.md). Both executors preserve autonomous decisions, evidence, and the single run record.

## Evidence, isolation, and completion

Pause only for critical missing access or additional authorization. Reuse existing authorization. Resolve ordinary product ambiguity, review disagreements, and test amendments autonomously. Additional authority for external effects is not supplied by one-shot.

Prefer an isolated candidate worktree at `<main-repo>/.worktrees/<feature>`. Allocate distinct execution slugs for concurrent runs across records and images. Record the plan revision and reconcile unexpected changes. Keep shared records at the parent repository root. For native worker isolation, verify actual placement as described in the active adapter rather than promising unsupported placement.

Use autopilot TDD under [test integrity](../_workflow/testing.md), recording observed red and green outputs and test amendments. Verify actual integration and UI behavior under [verification](../_workflow/verification.md). Observable native independent review may satisfy the review requirement for boost. If no independent reviewer can run, disclose self-review and leave required independent review incomplete.

Cap failed implementation attempts and review-fix rounds at three each. If alternatives are exhausted, report an honest incomplete result without requesting design feedback. For in-place runs at the cap, restore modified candidate files to their pre-task state and record what failed. Maintain decisions, plan, progress, review, proof, and walkthrough in the single run document. Follow [handoff](../_workflow/handoff.md), report limitations, and leave publishing and the final target-branch commit to the user.
