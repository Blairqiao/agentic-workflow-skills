# Feature specification and implementation plan

## Execution identity and readiness

- Feature slug and execution identity, distinct for concurrent runs:
- Status, `draft`, `blocked`, `ready`, or `executing`:
- Parent repository and shared artifact root:
- Target checkout:
- Target branch:
- Starting revision:
- Protected user edits and ownership boundaries:
- Selected executor and testing style:
- Plan revision:
- Execution authorization reference:
- Unresolved blockers, `none` required for ready status:

## Problem and goals

## Non-goals

## Behavior and interfaces

Describe normal use, edge cases, failure handling, compatibility, and affected data or permissions. Include examples, interface sketches, or diagrams where they resolve ambiguity.

## Acceptance criteria

| ID | Observable requirement | Verification |
| --- | --- | --- |

## Design decisions and history

Keep the active design current. Record rationale, tradeoffs, and any delegated details. Summarize abandoned approaches and link lengthy history in `.agent-docs/archive/`.

## Tasks and ownership

Record task goals, acceptance criteria IDs, expected files, dependencies, risks, and red and green commands. Boost receives deliverables and constraints and owns internal scheduling. Workers receive the exact plan identity and their file boundaries.

## Dependencies and external effects

List additions, migrations, external operations, required permissions, and existing authorization. Unresolved consequential permissions block ready status.

## Verification strategy

Record relevant tests, integration checks, static checks, UI viewports when applicable, content provenance checks, and known baseline failures.

## Delivery

Record the final candidate checkout and artifacts in the parent repository's `.agent-docs/`, review evidence, limitations, and handoff method. Use the execution identity consistently for plan, proof, taskboard, and screenshot names. Builders must reconcile changed plan decisions before dependent work.

## Execution instruction

Provide a copyable instruction naming this exact ready plan, target checkout, and selected executor. For example, `Execute /.agent-docs/plans/<feature>.md using full-track in the named checkout. Follow its scope, checks, and ownership boundaries.` Boost requires its explicit native entry sequence from the harness adapter. Ready status alone is not authorization. Material scope changes return to the planning phase and require a new execution instruction.
