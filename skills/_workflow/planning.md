# Implementation planning

Inputs: spec or one-shot design, discovered commands, selected track.

1. For full and one-shot, divide the work into coherent tasks with a goal, acceptance criteria, expected files, dependencies, relevant risks, and verification. Add interface sketches only when they prevent incompatible implementations. Fast-track treats the change as a single focused task recorded in `<main-repo>/.agent-docs/fast-track/<feature>.md`; if it requires multiple tasks, new dependencies, or migrations, escalate to full-track.
2. Choose verification by behavior: meaningful failing tests for code changes, characterization for legacy behavior, and visual, dry-run, or document evidence where appropriate. Property-based and snapshot tests are techniques that can support these approaches, not separate workflow modes.
3. Use autopilot testing unless the user requests [human-guided TDD](../human-tdd/SKILL.md). Record the choice once. One-shot always uses autopilot.
4. List new dependencies, migrations, external effects, and permissions needed. Existing approval remains valid; obtain additional authorization before operations outside it. For one-shot, prefer solutions within current authorization and ask only if the required operation cannot be avoided.
5. Full uses [the plan template](templates/plan.md) at `<main-repo>/.agent-docs/plans/<feature>.md` and presents spec and plan together for one approval. Fast presents its mini-spec and acceptance criteria in `<main-repo>/.agent-docs/fast-track/<feature>.md` for one approval before editing code. One-shot records its plan and proceeds without approval gates.

Expected files are planning aids, not a ban on incidental supporting edits. Reopen full or fast approval for material scope or risk changes, not ordinary implementation details.

Include affected project documentation in the task's files and acceptance criteria when behavior, setup, interfaces, or architecture change. Reuse its established location; create a focused guide when needed rather than expanding a small task into a whole-project documentation bootstrap.

Completion: tasks, verification, dependencies, and authorization boundaries are clear; full has approval covering spec and plan, and fast has approval covering its mini-spec.
