---
name: full-track
description: >-
  Run the complete spec-to-commit workflow with user approval gates on spec and plan, an isolated workspace, test-first tasks, independent review, evidence and a user-owned final commit. Use only when the user explicitly asks for full-track or for the full workflow on a feature.
---

# Full track

For features and changes that deserve a spec and a plan. Start by loading `workflow-core`, and keep its guardrails in force for the whole run.

## Steps

1. **Discover.** If `docs/agent-profile.md` is missing or marked stale, run `project-discovery` and have the user confirm the profile.
2. **Align.** Run `spec-alignment`. Do not continue until the user approves the spec.
3. **Plan.** Run `implementation-planning`. Ask the user to choose autopilot or human-guided TDD as part of plan approval. Do not continue until the user approves the plan.
4. **Isolate.** Run `worktree-setup`, then create the taskboard from the plan as `task-dispatch` describes.
5. **Execute.** Work through the tasks in dependency order with `task-dispatch`. Each task uses `tdd-integrity` for red and green and `independent-review` before it counts as done.
6. **Verify.** When every required task is done, run `verification-evidence`.
7. **Hand off.** Run `integration-handoff`. Stop once the changes are staged or the branch is ready, and let the user commit.

## Stop conditions

Pause and ask the user when:
- a task is blocked and no remaining task is independent of it;
- the work needs a change to the approved spec or plan;
- a new dependency, a schema migration or a boundary-path change appears that the plan did not list.
