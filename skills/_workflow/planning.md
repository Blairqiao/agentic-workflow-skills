# Implementation planning

Inputs: spec or one-shot design, discovered commands, selected track.

1. Divide the work into coherent tasks with a goal, acceptance criteria, expected files, dependencies, relevant risks, and verification. Add interface sketches only when they prevent incompatible implementations.
2. Choose verification by behavior: meaningful failing tests for code changes, characterization for legacy behavior, and visual, dry-run, or document evidence where appropriate. Property-based and snapshot tests are techniques that can support these approaches, not separate workflow modes.
3. Use autopilot testing unless the user requests [human-guided TDD](../human-tdd/SKILL.md). Record the choice once. One-shot always uses autopilot.
4. List new dependencies, migrations, external effects, and permissions needed. Existing approval remains valid; obtain additional authorization before operations outside it. For one-shot, prefer solutions within current authorization and ask only if the required operation cannot be avoided.
5. Full/fast use [the plan template](templates/plan.md), then present spec and plan together for one approval. One-shot records its plan and proceeds without approval gates.

Expected files are planning aids, not a ban on incidental supporting edits. Reopen full/fast approval for material scope or risk changes, not ordinary implementation details. No fixed line count determines task boundaries.

Completion: tasks, verification, dependencies, and authorization boundaries are clear; full/fast have approval covering spec and plan.
