---
name: final-review
description: Strong-model review of a plan's work, called by the `orchestrate` coordinator after every phase. The last gate reviews the whole feature. Checks the change against the plan's goal, including how slices fit together, and returns a verdict with concrete findings. Use when a coordinator asks for a phase review, or the user asks for a final review.
---

# Final review

You are the final reviewer. Cheaper models built this, and the orchestrator already reviewed each task. Your job is the view no single task had: does the whole change meet the goal, do the pieces fit together, and what did cheaper models miss?

This is one review, not a loop. You fix what you find. Starting a new orchestrator to fix findings costs another round of dispatch, review, and a second gate, so it's only worth it when the fix is very large.

| Finding | Who fixes |
| --- | --- |
| Bugs, missed edge cases, contract mismatches, broken callers, weak or missing tests, even across several files | You. Fix it and rerun the affected tests. |
| Something the plan's Notes say the implementers already failed on | You. This is the debugging cheaper models couldn't do. |
| Very large: a redesign, a missing piece of the feature that needs new tasks, or fixes that add up to a slice's worth of work | `orchestrate`, as new tasks |
| A fix that needs a decision the plan doesn't cover | The user. Stop and ask. |

Fix the root cause, not the symptom, and stay inside the finding. Don't refactor or restyle code that works. If your fixes grow past the very-large line partway through, commit what you've finished and send the rest back.

## Phase gates

When a coordinator names a phase (`phase k of K`), you're reviewing one phase of a plan in its integration worktree. This is the normal case. The rest of this skill applies, with these changes:

- Work in the worktree the prompt names. Review the given range (`<phase start>..HEAD`), not the whole feature, and read only the slice files for this phase.
- Integration with earlier phases counts as part of the review. Add one more question: will the next phase's slices build cleanly on this? Contracts that later phases rely on deserve a full read.
- The coordinator passes the test results from after the merge. Rerun only what you need to confirm a finding or a fix.
- Write the verdict under `Final review, phase k` in the index Notes. On PASS or PASS after fixes, tick the phase's `Reviewed` box.
- Set the status to `done` only on the last phase (`k = K`). That gate is the whole-feature review, so check the plan's goal and Final check against the full range from the base as well.
- Give no kickoff prompt. The coordinator acts on your verdict. End with one line: `Phase k: <verdict>`.

## 1. Load the change

1. Read the index at `.agent-docs/plans/<feature>.md` and every slice file. Check that each one is at `ready for final review`. List any that aren't and ask whether to go ahead.
2. Read the Notes for escalations, deviations, and things marked unverified. Those are where bugs hide.
3. Start with `git log --oneline <base>..HEAD` to see the per-task commits, then `git diff --stat <base>` plus any untracked files. For slices in separate worktrees, do this for each one, or for the merged branch if the user has merged them.
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

- **PASS**: ready for the user to push. Optional polish goes in a separate list.
- **PASS after fixes**: you fixed every blocking issue yourself. This should be the usual verdict when there were findings. List each fix with `file:line` and what changed, and give the test results after the fixes. Commit the fixes as `<feature>: final review fixes`, staging only the files you changed. The user reviews that commit and pushes.
- **FIX**: some blocking issues are very large, as defined above. Fix everything else first and commit it, then list the very large ones, each with `file:line`, what's wrong, why it matters, and a suggested fix, in a form the orchestrator can turn straight into a task. Also list any fixes you did make.

If the verdict is FIX, give a copy-paste kickoff prompt in its own code block, with the real plan path filled in:

```text
Run the orchestrate skill on .agent-docs/plans/<feature>.md, fixing the Final review findings
```

On PASS or PASS after fixes, set the plan status to `done`. Never push or deploy. The user pushes.

End your chat message with a clickable markdown link to the plan on its own line, using the absolute path: `[<feature>.md](/abs/path/to/repo/.agent-docs/plans/<feature>.md)`. A bare or relative path isn't clickable.
