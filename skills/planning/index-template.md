# <Feature name>

**Goal.** One or two sentences on what the user gets.

**Approach.** How it works and why. One line each for rejected alternatives.

**Out of scope.** What this feature deliberately does not do.

**Base.** `<commit sha>`

**Shared contracts.** Types, API shapes, or interfaces more than one slice must match, pasted verbatim. Or "none".

**Commands.** test `<cmd>`, lint `<cmd>`, build `<cmd>`, run `<cmd>`

**Orchestrator effort.** medium | high

**Status.** ready | in progress | done

## Phases

Phases run in order. Slices within a phase run in parallel and never modify the same file. Name each phase for what it protects.

### Phase 1: <name>

Why this is its own phase: <what the review gate protects, such as "contracts land before anyone builds on them">

| Slice | File | Owns files |
| --- | --- | --- |
| 1-<slice> | `<feature>/1-<slice>.md` | `src/...`, `src/...` |

Merge order: 1. Start: <sha, filled in by the coordinator>

- [ ] Slices done
- [ ] Merged
- [ ] Reviewed

### Phase 2: <name>

...

## Final check

The full test and build commands, a manual flow to try, and the screenshots to take with `visual-proof` if the UI changed.

## Notes

The coordinator records the integration worktree, the baseline, and in-flight state under `Coordinator`. Each review gate adds its verdict under `Final review, phase <k>`.
