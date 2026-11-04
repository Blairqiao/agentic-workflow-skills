---
name: planning
description: Write an implementation plan that cheaper models can execute without guessing, either as one linear plan or as parallel slices that each run in their own session. Use when the user asks for a plan or spec, or before multi-step work. Does not edit code.
---

# Planning

You are the planner. Cheaper models execute your plan: an orchestrator dispatches implementer subagents (Gemini Flash or GPT-6.1 Terra) and reviews each task. Every gap you leave turns into a wrong guess, a review round, or an escalation back to an expensive model. Spend effort here so execution is mechanical.

Do not edit code or tests. If the direction is unclear, run `brainstorm` first. If the request is clear, plan without an interview.

## 1. Gather facts

Find out:

- Which code the change touches.
- What tests already cover it.
- The exact test, lint, build, and run commands, from `package.json`, `Makefile`, `pyproject.toml`, or CI config.
- The base commit, from `git rev-parse --short HEAD`.

For broad reading, send cheap read-only subagents and require `file:line` citations for every claim. Trust cited reports. Re-check only a claim that a key decision depends on, such as "nothing else calls this". Read small, targeted files yourself.

Ask the user only about decisions you can't make from the code. Ask them in one batch, each with a recommended answer.

## 2. Choose the shape

- **Linear.** One plan with ordered tasks, run by one session. Use it when tasks build on each other or share files, or when the feature is small (up to about 6 tasks).
- **Parallel slices.** Independent slices, each run in its own session and worktree. Use it when the work splits cleanly by file ownership and slices don't need each other's unfinished code. Slices may depend on an interface you define in the plan, but not on code another slice is writing.

Recommend one shape and say why. If the user already picked, use that.

## 3. Write tasks a cheap model can't misread

Each task is a thin vertical slice that works end to end and touches a handful of files. Every task names:

- **Files.** Exact paths, marked create or modify.
- **Do.** Function, component, and type names, signatures, and data shapes. Point to an existing file to copy the pattern from ("follow `src/routes/users.ts`"). Add a code sketch when the interface would otherwise be ambiguous.
- **Done when.** Observable checks, not "works correctly".
- **Test.** One of:
  - `Test: <behavior>` for real logic, such as parsing, calculations, state transitions, data access, or a bug fix (write the regression test).
  - `Test: none. Verify by <how>` for UI, styling, config, glue, copy, and docs.

  Never plan tests that only check that a file, string, or mock exists. Follow the user's request if they asked for TDD or more coverage.
- **Builder.** One of:
  - `flash`: mechanical work. CRUD, UI, wiring, config, following an existing pattern.
  - `terra`: logic, algorithms, cross-file refactors, unfamiliar APIs.
  - Add `high` effort only for genuinely tricky tasks. The default is medium.
- **Gotchas.** Anything a newcomer would trip on, such as a stale cache, a generated file to leave alone, or an env var.

Prefer more, smaller tasks over fewer large ones. Flash does well on small, precise tasks and badly on vague ones.

## 4. Save

Before writing, add `.agent-docs/` to `.git/info/exclude` if it isn't already there. Don't touch `.gitignore`.

- **Linear.** Save to `.agent-docs/plans/<feature>.md` using [plan-template.md](plan-template.md).
- **Parallel.** Save an index to `.agent-docs/plans/<feature>.md` with the goal, shared interfaces, the slice list, file ownership, and merge order. Save each slice to `.agent-docs/plans/<feature>/<n>-<slice>.md` using the same template. Each slice must stand alone: a session given only that file has everything it needs. No two slices may modify the same file. Shared contracts, such as types or API shapes, either go in a slice 0 that runs first or get pasted verbatim into each slice that uses them.

## 5. Hand off

In chat, give the goal, the shape, the tasks or slices (one line each), and the risks. Set the status to `ready`. Don't wait for approval and don't start building. The user will ask for changes if they want any, or start orchestration with the kickoff prompt.

Give a copy-paste kickoff prompt for each session:

```text
Run the orchestrate skill on .agent-docs/plans/<feature>.md
```

For parallel slices, give one kickoff prompt per slice and say which slices can start now and which must wait for slice 0.

End your chat message with a clickable markdown link to the plan (the index, for parallel slices) on its own line, using the absolute path: `[<feature>.md](/abs/path/to/repo/.agent-docs/plans/<feature>.md)`. A bare or relative path isn't clickable.
