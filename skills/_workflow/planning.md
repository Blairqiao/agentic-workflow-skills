# Implementation planning

Inputs: specification or one-shot design, discovered commands, and selected track.

1. For full and one-shot, divide the work into coherent tasks with a goal, acceptance criteria, expected files, dependencies, relevant risks, and verification. Add interface sketches only when they prevent incompatible implementations. Fast-track treats the change as a single linear execution in the current session recorded in `<main-repo>/.agent-docs/fast-track/<feature>.md`; if it requires multi-step implementation orchestration, implementation subagents, new dependencies, or migrations, escalate to full-track. Read-only code exploration under [discovery](discovery.md#code-exploration-and-delegation) does not trigger escalation.
2. Choose verification by behavior: meaningful failing tests for code changes, characterization for legacy behavior, and visual, dry-run, or document evidence where appropriate. Property-based and snapshot tests are techniques that support these approaches, not separate workflow modes.
3. Use autopilot testing unless the user requests [human-guided TDD](../human-tdd/SKILL.md). Record the choice once. One-shot always uses autopilot.
4. List new dependencies, migrations, external effects, and permissions needed. Existing approval remains valid; obtain additional authorization before operations outside it. For one-shot, prefer solutions within current authorization and ask only if the required operation cannot be avoided.
5. Record and present the plan according to the track:
   - **Full-track.** Complete the implementation plan sections in `<main-repo>/.agent-docs/plans/<feature>.md` using [the combined spec-and-plan template](templates/plan.md), present the spec and plan inline in chat, and pause for one combined approval.
   - **Fast-track.** Present the mini-spec, target files, and acceptance criteria in `<main-repo>/.agent-docs/fast-track/<feature>.md` inline in chat and pause for one approval before editing code.
   - **One-shot.** Record the plan in `<main-repo>/.agent-docs/runs/<feature>.md` and proceed without approval gates.

When adjusting an existing plan on retry or follow-up, edit the main sections of `<feature>.md` in place so they describe the current approach, keep a brief note on any previous attempt, and move lengthy superseded material to `.agent-docs/archive/`. Expected files are planning aids, not a ban on incidental supporting edits. Reopen full or fast approval for material scope or risk changes, not ordinary implementation details.

Include affected project documentation in the task's files and acceptance criteria when behavior, setup, interfaces, or architecture change. Reuse established documentation locations rather than expanding a focused task into a whole-project documentation bootstrap.

Completion: tasks, verification, dependencies, and authorization boundaries are clear; full has approval covering its combined spec and plan, and fast has approval covering its mini-spec.
