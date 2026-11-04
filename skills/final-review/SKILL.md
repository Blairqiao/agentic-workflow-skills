---
name: final-review
description: One final review of a finished feature by a strong model, run once after `orchestrate`. Checks the whole change against the plan's goal, including how parallel slices fit together, and returns a verdict with concrete findings. Use when the user asks for a final review or a plan's status is "ready for final review".
---

# Final review

You are the final reviewer. Cheaper models built this, and the orchestrator already reviewed each task. Your job is the view no single task had: does the whole change meet the goal, do the pieces fit together, and what did cheaper models miss?

This is one review, not a loop. Report findings. Don't rewrite the code. Fixes go back to `orchestrate` so the cheaper models do the work. Fix something yourself only if it's a few lines, or if the plan's Notes say the implementers already failed on it.

## 1. Load the change

1. Read the plan at `.agent-docs/plans/<feature>.md`. For parallel slices, read the index and every slice file. Check that each one is at `ready for final review`. List any that aren't and ask whether to go ahead.
2. Read the Notes for escalations, deviations, and things marked unverified. Those are where bugs hide.
3. Get the full diff against the plan's `Base` commit: `git diff <base>` plus untracked new files. For slices in separate worktrees, review each one's diff, or the merged branch if the user has merged them.

## 2. Verify

Run the full test, lint, and build commands once. Trust the orchestrator's per-task results unless something looks off.

## 3. Review

Read the diff, prioritizing the riskiest code: data, auth, concurrency, money, migrations, and anything that got escalated.

- **Goal.** Does the whole thing do what the plan's goal says? Walk the final-check flow in your head, or run it.
- **Integration.** Do slices and tasks agree on the shared contracts? Are there duplicated helpers, mismatched names, or conflicting assumptions across files?
- **Correctness.** Look for bugs, unhandled errors, edge cases, race conditions, and broken callers outside the changed files.
- **Security.** Check input validation, authorization, secrets, and injection at the boundaries.
- **Tests.** Do planned tests check real behavior? Were any existing tests weakened or skipped?
- **Fit.** Is there needless complexity, dead code, or a mismatch with codebase patterns? Report this only when it matters.

## 4. Report

Add the verdict to the plan's Notes under `Final review`, and say it in chat:

- **PASS**: ready for the user to commit. Optional polish goes in a separate list.
- **FIX**: blocking issues, each with `file:line`, what's wrong, why it matters, and a suggested fix. Put each one in a form the orchestrator can turn straight into a task.

If the verdict is FIX, give the next step:

```text
Run the orchestrate skill on .agent-docs/plans/<feature>.md, fixing the Final review findings
```

On PASS, set the plan status to `done`. Don't commit. The user commits.

End your chat message with a clickable markdown link to the plan on its own line, using the absolute path: `[<feature>.md](/abs/path/to/repo/.agent-docs/plans/<feature>.md)`. A bare or relative path isn't clickable.
