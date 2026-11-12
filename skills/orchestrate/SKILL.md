---
name: orchestrate
description: Run a plan from `planning`. As coordinator, it runs each phase's slices as parallel child orchestrators, merges them, and calls a strong-model review gate after every phase. As a slice orchestrator, it dispatches cheap implementers task by task, reviews each task, and escalates when one gets stuck. Use when the user says to run, execute, or orchestrate a plan.
---

# Orchestrate

You are the orchestrator and the per-task reviewer. Implementer subagents write the code: Gemini Flash or GPT-6.1 Terra, at the effort the plan sets. You keep the plan, dispatch tasks, review diffs, and decide what happens next. Don't do implementation work yourself beyond trivial fixes.

## Which mode

- **Coordinator** (the default): when the user starts a run, you're the coordinator. Follow [coordinate.md](coordinate.md) instead of the rest of this file.
- **Slice orchestrator** (the prompt says `as a slice`): build that one slice. Follow everything below.
- **Fixer** (the prompt says to fix review findings): the tasks are the blocking findings in the latest `Final review` entry in the index Notes. Work in the checkout the prompt names, reuse the baseline already recorded, and treat each finding as a task. Build each one as `terra` unless it's mechanical. Follow the per-task loop and Finish below, skipping the visual proof and the status change, and end with one line: `Fixes: <done or stuck>, head <sha>`.

## Before starting

1. Read the slice file the prompt names. Being asked to run it is the go-ahead.
2. Check that you're in the right checkout: the worktree and starting commit the prompt gives. Run `git status` and note any uncommitted user changes. Never overwrite them.
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

Each task's `Builder:` line picks the model. The hierarchy is `flash` (low) -> `flash medium` -> `terra`. For Flash, `low` effort is the default and `medium` is used for more complex tasks. Otherwise, tasks use Terra.

- **T3 Code.** Call `orchestrator_capabilities` once, then `delegate_task` with the target provider and model (Gemini Flash with low or medium effort, or Codex with Terra) and the effort level in `target.options`. If you're running in Codex, a Terra task can use native `spawn_agent` instead.
- **Provider routing.** If `~/.agents/routing.md` exists, read it before the first dispatch and use the provider instance it names for each model, plus its fallback rule. A provider instance named in your prompt overrides the file. Without a routing file or an instance in the prompt, a dispatch that fails on quota or auth stops the task. Tell the user.
- **Other harnesses.** Use the native subagent tool with the closest model available. Tell the user what you substituted.

Build each prompt from [implementer-prompt.md](implementer-prompt.md). Paste in the task text, the shared contracts, and the specific facts it needs. Implementers start with no context, so a bare "see the plan" doesn't work.

Run tasks with no dependencies and no shared files in parallel. Run everything else in order.

## Per-task loop

1. **Dispatch** the implementer.
2. **Gate.** An implementer may report `DONE` only after the task's tests, lint, and build pass. If the report shows failures, send it back. Don't review red work.
3. **Review** the task's uncommitted diff yourself. Start with `git diff --stat`, then read `git diff -- <files>` plus new files in full. Skip lockfiles, snapshots, and generated files, and check them instead:
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
   - On a pass, tick the task's boxes in the plan and commit the task (see below).

## Committing

Commit each task after it passes review. Never push or deploy. The user pushes.

- Stage only the task's files by name, never `git add -A` or `git add .`, so uncommitted user changes stay out of the commit.
- Message: `<feature>: <task title>`, with a short body if the change needs one.
- Don't amend, rebase, reset, or skip hooks with `--no-verify`. If a pre-commit hook fails, fix the cause or send it back to the implementer.
- `.agent-docs/` is excluded from git, so the plan and logs are never committed.

A commit per task gives the final reviewer a history to read, and lets a bad task be reverted on its own.

## Escalation ladder

Count failed rounds per task, where a round is a dispatch that comes back red or fails review. The hierarchy is `flash` (low) -> `flash medium` -> `terra`:

1. Flash at low fails 2 rounds: escalate to Flash at medium.
2. Flash at medium fails 2 rounds: move the task to Terra.
3. Terra fails 2 rounds: retry at high.
4. Still failing: stop that task. Write in the plan's Notes what was tried, the exact errors, and your best guess at the cause. Tell the user it needs a stronger model to debug.

Every escalation carries the failure notes forward. Never restart cold. If tasks fail for the same reason, the plan is probably wrong. Stop and say so instead of burning rounds.

Keep working on tasks that don't depend on a stuck one.

## Handing off

If the user says "hand off", or the session has run many tasks and grown large, save your state and stop:

1. Tick every passed task. Under `Handoff` in the plan's Notes, write the current task, its round count and builder, any open review findings, and anything you were in the middle of.
2. End with your one-line report, with status `handoff`. The coordinator starts a fresh slice orchestrator in the same worktree, and it resumes from your notes.

A fresh session that reads the plan costs less than compacting this one.

## Finish

1. Run the full test suite, lint, and build. Compare against the baseline from before you started.
2. If the UI changed, dispatch `visual-proof` to a cheap model. Screenshots and page snapshots are large, so they should fill its context, not yours. Read its proof file and look at the key screenshots yourself.
3. Commit anything left over, such as small fixes after the last task, the same way as task commits. Don't push or deploy.
4. Set the slice status to `ready for final review`. Add a short summary to the slice's Notes covering what was built, test and build results, escalations, deviations from the plan, and anything unverified.
5. End with exactly the one line the prompt asks for, giving your status, branch, and head SHA. The coordinator merges your branch and starts the review.

## Stop and ask when

To stop, write the question or problem in the slice's Notes and in chat, then end with your one-line report with status `stuck` or `blocked`. The coordinator takes it to the user.

- The plan is wrong, or a task needs a decision the plan doesn't cover.
- You need a new dependency, a migration, or a destructive operation.
- A task falls off the bottom of the escalation ladder.
