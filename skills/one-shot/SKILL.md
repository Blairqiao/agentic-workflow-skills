---
name: one-shot
description: >-
  Run the workflow autonomously from a single prompt, with no mid-run approval gates, autopilot TDD, an isolated workspace, independent review, a mandatory proof and a user-owned final commit. Use only when the user explicitly asks for one-shot.
---

# One-shot

The user trades mid-run feedback for speed. Load `workflow-core` first. Guardrails still apply, and unsupervised runs are where they matter most.

## What changes from full-track

- The user's request counts as approval for the spec and plan. Write both anyway, because review and evidence check against them, but don't wait at their gates.
- TDD runs in autopilot mode.
- The proof is mandatory. Unsupervised runs are where agents most often mark work done without checking it end to end. Write the walkthrough only if the user asked for it.
- The stop conditions in `workflow-core` still stop the run. Ask instead of guessing.

## Steps

1. Restate the request in two or three lines and confirm the user wants one-shot. This is the only upfront question.
2. Run `project-discovery` if needed. If the profile is new, list your assumptions in the final handoff instead of waiting for confirmation.
3. Write the spec and plan with `spec-alignment` and `implementation-planning`, skipping their gates.
4. Run `worktree-setup`, then the task loop in `task-dispatch`.
5. Run `verification-evidence`.
6. Run `integration-handoff`. Present the spec and plan next to the staged changes so the user can review everything at once.
