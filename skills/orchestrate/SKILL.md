---
name: orchestrate
description: Execute a plan or slice by dispatching cheap implementer models task by task, reviewing each task yourself, and escalating when an implementer gets stuck. Ends ready for one final review by a stronger model. Use when the user says to run, execute, or orchestrate a plan from `planning`.
---

# Orchestrate

You are the orchestrator and the per-task reviewer. Implementer subagents write the code: Gemini Flash or GPT-6.1 Terra, at the effort the plan sets. You keep the plan, dispatch tasks, review diffs, and decide what happens next. Don't do implementation work yourself beyond trivial fixes.

## Before starting

1. Read the plan or slice file the user named. Being asked to run it is the go-ahead.
2. Check that you're in the right checkout. For a slice with a worktree, work in that worktree. Run `git status` and note any uncommitted user changes. Never overwrite them.
3. **Resuming?** If some tasks are already ticked, or the Notes have a `Handoff` entry, this is a resume. Skip the ticked tasks, reuse the baseline in Notes, and continue from the handoff point or the first unticked task. Skip step 4.
4. Run the plan's test, lint, and build commands once. In the plan's Notes, record the baseline: the pass, fail, and skip counts, and the names of tests that already fail.
5. Set the status to `in progress`.

## Reading command output

Long output stays in your context and gets re-read every turn. Don't paste whole logs into the conversation:

- Send output to a file: `<cmd> > .agent-docs/logs/<name>.log 2>&1; echo "exit $?"`.
- **Exit 0:** read the summary line, such as test counts, with `tail`.
- **Nonzero exit:** grep the whole log for failures (`FAIL|Error|error:` or the runner's marker) and read every failure block in full. Don't rely on `tail` alone, because the first error is often far above the end.
- **Compare with the baseline.** Fewer tests than before, new skips, or new warnings are red flags, even on a green run.

The log stays on disk. Read more of it whenever something looks off.

## Dispatching implementers

Each task's `Builder:` line picks the model. Medium effort is the default and high only when the plan says so.

- **T3 Code.** Call `orchestrator_capabilities` once, then `delegate_task` with the target provider and model (Gemini Flash, or Codex with Terra) and the effort level in `target.options`. If you're running in Codex, a Terra task can use native `spawn_agent` instead.
- **Other harnesses.** Use the native subagent tool with the closest model available. Tell the user what you substituted.

Build each prompt from [implementer-prompt.md](implementer-prompt.md). Paste in the task text, the shared contracts, and the specific facts it needs. Implementers start with no context, so a bare "see the plan" doesn't work.

Run tasks with no dependencies and no shared files in parallel. Run everything else in order.

## Per-task loop

1. **Dispatch** the implementer.
2. **Gate.** An implementer may report `DONE` only after the task's tests, lint, and build pass. If the report shows failures, send it back. Don't review red work.
3. **Review** the task's diff yourself. Start with `git diff --stat`, then read `git diff -- <files>` plus new files in full. Skip lockfiles, snapshots, and generated files, and check them instead:
   - A lockfile change needs a matching manifest change, such as in `package.json`, and a new dependency needs the user's approval.
   - A generated file that changed when its source didn't was probably edited by hand. Read it.
   - Otherwise, a passing build and typecheck verify the generated output.

   Then check:
   - It does what the task says. Nothing is missing, nothing extra was added, and the done-when checks hold.
   - There are no bugs, unhandled errors or edge cases, broken callers, or security holes at input or auth boundaries.
   - It reuses existing helpers and follows the codebase's patterns.
   - The tests match the `Test:` line and check real behavior, not mocks. No existing test was weakened.
   - Read the code. Don't trust the implementer's summary. If the summary and the diff disagree, read the whole change again more carefully.
4. **Fix or pass.**
   - A trivial issue, such as a typo, an import, or a few lines, you fix yourself.
   - A real issue goes back to the same implementer with file:line and what's wrong.
   - On a pass, tick the task's boxes in the plan.

## Escalation ladder

Count failed rounds per task, where a round is a dispatch that comes back red or fails review.

1. Flash at medium fails 2 rounds: retry at high, or move the task to Terra.
2. Terra fails 2 rounds: retry at high.
3. Still failing: stop that task. Write in the plan's Notes what was tried, the exact errors, and your best guess at the cause. Tell the user it needs a stronger model to debug.

Every escalation carries the failure notes forward. Never restart cold. If tasks fail for the same reason, the plan is probably wrong. Stop and say so instead of burning rounds.

Keep working on tasks that don't depend on a stuck one.

## Handing off

If the user says "hand off", or the session has run many tasks and grown large, save your state and stop:

1. Tick every passed task. Under `Handoff` in the plan's Notes, write the current task, its round count and builder, any open review findings, and anything you were in the middle of.
2. Give this prompt for a fresh session:

```text
Run the orchestrate skill on .agent-docs/plans/<feature>.md
```

A fresh session that reads the plan costs less than compacting this one. Resume picks up from the handoff.

## Finish

1. Run the full test suite, lint, and build. Compare against the baseline from before you started.
2. If the UI changed, dispatch `visual-proof` to a cheap model. Screenshots and page snapshots are large, so they should fill its context, not yours. Read its proof file and look at the key screenshots yourself.
3. Stage the changes with `git add`. Don't commit, push, or deploy.
4. Set the status to `ready for final review`. Add a short summary to the plan's Notes covering what was built, test and build results, escalations, deviations from the plan, and anything unverified.
5. In chat, give that summary, then a copy-paste kickoff prompt for the final review session in its own code block, with the real plan path filled in:

```text
Run the final-review skill on .agent-docs/plans/<feature>.md
```

For a parallel slice, point the prompt at the index (`.agent-docs/plans/<feature>.md`), not the slice file, and say which slices still need to finish before final review can start.

End your chat message with a clickable markdown link to the plan or slice file on its own line, using the absolute path: `[<feature>.md](/abs/path/to/repo/.agent-docs/plans/<feature>.md)`. A bare or relative path isn't clickable.

## Stop and ask when

- The plan is wrong, or a task needs a decision the plan doesn't cover.
- You need a new dependency, a migration, or a destructive operation.
- A task falls off the bottom of the escalation ladder.
