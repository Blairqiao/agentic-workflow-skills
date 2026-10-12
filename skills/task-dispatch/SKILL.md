---
name: task-dispatch
description: >-
  Orchestrate the per-task execution loop: keep the taskboard, sync and baseline the workspace, hand each task to a fresh implementer with the right context, verify its claims yourself, route it to review, and enforce retry and stop limits. Use in the execute phase of any workflow track, or when resuming a workflow run from a taskboard.
---

# Task dispatch

You are the orchestrator. Implementers do the work; you keep state, check claims and decide what happens next.

## Taskboard

Create it from the plan with `assets/taskboard-template.md` at the profile's location, by default `docs/taskboard/<feature>.md`.
- Only the orchestrator edits it. Implementers and reviewers may read it.
- Keep it dense: status, commits, attempts and one-line notes. Narrative belongs in the walkthrough.
- Move finished tasks to the Done section so the active part stays short.

Statuses: `todo`, `active`, `red`, `green`, `review`, `done`, `blocked`.

## Running a role in a fresh context

Use the first option your harness supports, and note which one in the taskboard:
1. **Native subagent** with its own context.
2. **Separate headless session** of this harness or another, started from the shell with the brief as its prompt.
3. **Same session.** Write the brief to a file and work strictly from it. Tell the user that review independence is reduced in this mode.

## Per-task loop

1. **Sync and baseline.** Merge the target branch into the workspace as `worktree-setup` describes, then confirm the baseline. Failures at this point belong to the base. Report them and don't start the task on a broken base.
2. **Brief.** Build the implementer's brief from `assets/implementer-brief.md`: the task slice, the full text of its criteria, files in scope, the red expectation, profile commands, the `tdd-integrity` rules and what to return. Point it at the spec, plan and taskboard as read-only context, because shared context prevents conflicting decisions between tasks.
3. **Questions.** If the implementer asks something the spec and plan don't answer, ask the user. Don't guess on their behalf.
4. **Red, then green.** The implementer follows `tdd-integrity`. After each step, check it yourself: rerun the checks, read the diff, confirm the commit. Never accept "tests pass" without your own run.
5. **Review.** Send the task to `independent-review`. On failure, pass the findings to an implementer and repeat green.
6. **Close.** Mark the task done with its commits, then pick the next task whose dependencies are done.

## Limits

- At most 5 attempts at red or green, and 3 review rounds per task. After that, mark the task `blocked`, record why, and ask the user.
- A blocked task stops only the tasks that depend on it. Keep going with independent tasks, but don't start verification or handoff until every required task is done.
- Run tasks in parallel only in separate workspaces with separately allocated resources, and only when they touch different files.

## Scope drift

If an implementer needs files outside its scope, a new dependency, a migration or a boundary path the plan didn't list, stop that task and ask the user. It usually means the plan needs an amendment.
