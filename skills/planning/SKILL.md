---
name: planning
description: Write an implementation plan that cheaper models can execute without guessing, as slices grouped into phases, with as many of each as the work needs. Use when the user asks for a plan or spec, or before multi-step work. Does not edit code.
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

Every plan is a set of **slices** grouped into **phases**. A coordinator runs the phases in order. Within a phase, it runs each slice as its own orchestrator in its own worktree, all in parallel. Then it merges them and sends the phase to an Opus or Astra review gate before the next phase starts.

- **Slice.** An ordered list of tasks that one orchestrator builds. Split the work into separate slices only where it divides cleanly by file ownership. Tasks that build on each other or share files belong in one slice.
- **Phase.** A checkpoint. Start a new phase where later work needs earlier code merged and reviewed first, such as after shared contracts land, or before wiring that touches files several slices needed. A slice may depend on code from earlier phases, never on code from its own phase.

Use as many phases and slices as the work needs, and no more. A small feature is one phase with one slice. Every phase costs a strong-model review, so don't add a phase that only splits work without protecting anything. If the user already described a shape, use it.

## 3. Write tasks a cheap model can't misread

Each task is a thin vertical slice that works end to end and touches a handful of files. Every task names:

- **Files.** Exact paths, marked create or modify.
- **Do.** Function, component, and type names, signatures, and data shapes. Point to an existing file to copy the pattern from ("follow `src/routes/users.ts`"). Add a code sketch when the interface would otherwise be ambiguous.
- **Done when.** Observable checks, not "works correctly".
- **Test.** One of:
  - `Test: <behavior>` for real logic, such as parsing, calculations, state transitions, data access, or a bug fix (write the regression test).
  - `Test: none. Verify by <how>` for UI, styling, config, glue, copy, and docs.

  Never plan tests that only check that a file, string, or mock exists. Follow the user's request if they asked for TDD or more coverage.
- **Builder.** The hierarchy is `flash` (low) -> `flash medium` -> `terra`:
  - `flash`: mechanical work (CRUD, UI, wiring, config, following an existing pattern). Default effort is `low`.
  - `flash medium`: more complex work (non-trivial glue, tricky branching, multi-constraint formatting).
  - `terra`: logic, algorithms, cross-file refactors, unfamiliar APIs, or tasks beyond Flash.
- **Gotchas.** Anything a newcomer would trip on, such as a stale cache, a generated file to leave alone, or an env var.

Prefer more, smaller tasks over fewer large ones. Flash does well on small, precise tasks and badly on vague ones.

## 4. Save

Before writing, add `.agent-docs/` to `.git/info/exclude` if it isn't already there. Don't touch `.gitignore`.

- **Index.** Save to `.agent-docs/plans/<feature>.md` using [index-template.md](index-template.md). It holds the goal, the shared contracts, the commands, and the phases.
- **Slices.** Save each slice to `.agent-docs/plans/<feature>/<n>-<slice>.md` using [plan-template.md](plan-template.md).

Each slice must stand alone: a session given only that file has everything it needs. No two slices in the same phase may modify the same file. Paste shared contracts, such as types or API shapes, verbatim into every slice that uses them, or put them in an earlier phase.

## 5. Hand off

In chat, give the goal, the phases and their slices (one line each), and the risks. Set the status to `ready`. Don't wait for approval and don't start building. The user will ask for changes if they want any, or start orchestration with the kickoff prompt.

Give one copy-paste kickoff prompt:

```text
Run the orchestrate skill on .agent-docs/plans/<feature>.md
```

It starts the coordinator, which runs every phase, slice, and review gate. Say it can run with Gemini Flash.

End your chat message with a clickable markdown link to the index on its own line, using the absolute path: `[<feature>.md](/abs/path/to/repo/.agent-docs/plans/<feature>.md)`. A bare or relative path isn't clickable.
