---
name: fast-track
description: >-
  Run a lightweight version of the workflow for a small, well-understood change such as a bugfix, with no spec or plan gates but the same isolated workspace, test-first rules, review and user-owned commit. Use only when the user explicitly asks for fast-track.
---

# Fast track

For small changes where a full spec would be ceremony. Load `workflow-core` first; every guardrail still applies.

## Fit check

Before starting, confirm the change fits. Use the limits in the project profile. If it sets none, use these:
- about 100 changed lines and 3 files or fewer, not counting lockfiles and generated files;
- no paths the profile lists as boundaries, such as auth, payments, migrations or infrastructure;
- no new dependencies;
- verification mode is test-first or characterization-first.

If the change doesn't fit, say why and suggest full-track.

## Steps

1. Run `project-discovery` if the profile is missing or stale.
2. Write a mini-spec in the taskboard: the problem in two or three sentences and numbered acceptance criteria. Show it to the user in one message before starting. It is a notice, not a gate, so continue unless they object.
3. Run `worktree-setup`.
4. Treat the change as one task. Follow `tdd-integrity` for red and green, then `independent-review`. A fresh-context review still matters for small changes, because small diffs are where a weakened test is easiest to miss.
5. Run `verification-evidence` in its short form: the proof with commands and outputs, plus manual check steps. Skip the full walkthrough unless the user asks.
6. Run `integration-handoff`.

## Escalation

If the change outgrows the fit check at any point:
1. Commit the current work in the workspace and record that commit in the taskboard as `fast-track-wip`.
2. Stop and tell the user what grew and why.
3. If they agree, switch to `full-track`, reusing the workspace and any red tests already written.
