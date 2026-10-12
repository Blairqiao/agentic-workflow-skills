---
name: implementation-planning
description: >-
  Break an approved spec into small, ordered task slices that each name their acceptance criteria, files in scope, verification mode and expected failing tests. Use in the plan phase of the full-track or one-shot workflow, or when the user asks for an implementation plan for an approved spec.
---

# Implementation planning

A good plan makes each task small enough for one fresh agent to finish and for a reviewer to judge in one pass.

## Task slices

Each task has:
- **ID and goal.** One behavior, in one sentence.
- **Criteria.** The AC IDs it satisfies.
- **Scope.** Files or globs it may change. Needing anything outside scope is a signal to stop, not to improvise.
- **Interfaces.** Signatures or contracts it adds or changes, a few lines at most.
- **Verification mode.** One of the modes below.
- **Red expectation.** Which tests get added and how they should fail at first, usually on an assertion. If the code under test doesn't exist yet, say whether signature stubs are allowed so the test can reach its assertion.
- **Depends on.** Task IDs that must finish first.
- **Risk.** Boundary paths, migrations or new dependencies it involves.

Split a task likely to change more than about 300 lines or 5 files; adjust that to what your models handle well. Keep code out of the plan apart from short interface sketches, so implementers make detailed choices against the spec rather than copying a draft.

## Verification modes

| Mode | Use for |
| --- | --- |
| test-first | Most features and bugfixes in code with a runnable test suite |
| characterization-first | Untested legacy code: first pin current behavior with tests, then change it |
| property-based | Parsers, algorithms, invariants |
| snapshot | UI output, serializers, generated files; snapshot updates get their own commit for user approval |
| plan-diff | Infrastructure, config, migrations: the tool's plan or dry-run output is what gets approved |
| evidence-only | Visual polish, docs, exploration: the user verifies from the evidence |

## TDD style

Ask the user to choose:
- **Autopilot.** Implementers design, write and run tests on their own.
- **Human-guided.** Agree on test design with the user first. Tag each test idea `[Specific]` for a single case, `[Intermediate]` for a behavior across cases, or `[Global]` for system-level properties. Propose a manual check in the evidence for anything that would need brittle mocks.

## Dependencies and migrations

List every new dependency with what it is and why it's needed. New dependencies, schema migrations and boundary-path changes each need the user's explicit approval as part of the plan.

## Gate

Save with `assets/plan-template.md` to the profile's plan location, by default `docs/plans/<feature>.md`. Show it and ask for approval together with the TDD style. After approval the plan is frozen; changes go in Amendments and need approval. In one-shot runs, skip the gate and use autopilot.
