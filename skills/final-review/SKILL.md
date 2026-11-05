---
name: final-review
description: One final review of a finished feature by a strong model, run once after `orchestrate`. Checks the whole change against the plan's goal, including how parallel slices fit together, and returns a verdict with concrete findings. Use when the user asks for a final review or a plan's status is "ready for final review".
---

# Final review

You are the final reviewer. Cheaper models built this, and the orchestrator already reviewed each task. Your job is the view no single task had: does the whole change meet the goal, do the pieces fit together, and what did cheaper models miss?

This is one review, not a loop. Don't rewrite the code. Sort each blocking finding:

| Finding | Who fixes |
| --- | --- |
| Local: one or two files, obvious fix, about 20 lines or fewer | You. Fix it and rerun the affected tests. |
| Something the plan's Notes say the implementers already failed on | You. This is the debugging cheaper models couldn't do. |
| Spread across files, a redesign, or a missing piece of the feature | `orchestrate`, as new tasks |

Keep the cap strict. If your fixes start to grow, stop and send the rest back to `orchestrate`.

## 1. Load the change

1. Read the plan at `.agent-docs/plans/<feature>.md`. For parallel slices, read the index and every slice file. Check that each one is at `ready for final review`. List any that aren't and ask whether to go ahead.
2. Read the Notes for escalations, deviations, and things marked unverified. Those are where bugs hide.
3. Start with `git diff --stat <base>` plus untracked new files. For slices in separate worktrees, do this for each one, or for the merged branch if the user has merged them.
4. Pick what to read. Read the diffs of risky files in full: data, auth, concurrency, money, migrations, shared contracts, and anything that got escalated. Skim the rest. The orchestrator already read every task diff, so your reading goes to risk and integration.
5. Don't read lockfiles, snapshots, or generated files. Check them instead:
   - A lockfile change needs a matching manifest change.
   - A generated file that changed when its source didn't was probably edited by hand. Read it.

## 2. Verify

Run the full test, lint, and build commands once, each sent to a file: `<cmd> > .agent-docs/logs/<name>.log 2>&1; echo "exit $?"`. Don't load the whole log into context:

- **Exit 0:** read the summary line.
- **Nonzero exit:** grep the whole log for failures and read every failure block in full.

Trust mechanical signals such as exit codes, typecheck, and test counts. Spend your reading on judgment. Read in full when you see a red flag:

- The test count dropped compared with the baseline in Notes.
- There are new skips or new warnings.
- A generated file or lockfile changed without its source.
- The orchestrator's summary doesn't match the diff.

## 3. Review

Review the files you picked in step 1. Read more if anything below looks off.

- **Goal.** Does the whole thing do what the plan's goal says? Walk the final-check flow in your head, or run it.
- **Integration.** Do slices and tasks agree on the shared contracts? Are there duplicated helpers, mismatched names, or conflicting assumptions across files?
- **Correctness.** Look for bugs, unhandled errors, edge cases, race conditions, and broken callers outside the changed files.
- **Security.** Check input validation, authorization, secrets, and injection at the boundaries.
- **Tests.** Do planned tests check real behavior? Were any existing tests weakened or skipped?
- **Fit.** Is there needless complexity, dead code, or a mismatch with codebase patterns? Report this only when it matters.

## 4. Report

Add the verdict to the plan's Notes under `Final review`, and say it in chat:

- **PASS**: ready for the user to commit. Optional polish goes in a separate list.
- **PASS after fixes**: you fixed every blocking issue yourself. List each fix with `file:line` and what changed, stage it with `git add`, and give the test results after the fixes. The user reviews your diff and commits.
- **FIX**: some blocking issues are too big to fix yourself. List them, each with `file:line`, what's wrong, why it matters, and a suggested fix, in a form the orchestrator can turn straight into a task. Also list any fixes you did make.

If the verdict is FIX, give a copy-paste kickoff prompt in its own code block, with the real plan path filled in:

```text
Run the orchestrate skill on .agent-docs/plans/<feature>.md, fixing the Final review findings
```

On PASS or PASS after fixes, set the plan status to `done`. Don't commit. The user commits.

End your chat message with a clickable markdown link to the plan on its own line, using the absolute path: `[<feature>.md](/abs/path/to/repo/.agent-docs/plans/<feature>.md)`. A bare or relative path isn't clickable.
