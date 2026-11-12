# <Feature name>: slice <n>, <slice name>

**Goal.** One or two sentences on what the user gets. What this slice delivers and how it fits the whole.

**Approach.** How it works and why. One line each for rejected alternatives.

**Out of scope.** What this slice deliberately does not do.

**Base.** `<commit sha>`. Worktree: assigned by the coordinator

**Owns files.** The files this slice may create or modify. Touch nothing else.

**Shared contracts.** Types, API shapes, or interfaces this work must match, pasted verbatim.

**Commands.** test `<cmd>`, lint `<cmd>`, build `<cmd>`, run `<cmd>`

**Status.** ready | in progress | ready for final review | done

## Tasks

### 1. <Task name>

- **Files.** `path/to/file.ts` (modify), `path/to/new.ts` (create)
- **Do.** Names, signatures, data shapes. "Follow the pattern in `path/to/example.ts`."
- **Done when.** Observable checks.
- **Test.** `<behavior to test>` | none. Verify by `<how>`
- **Builder.** flash [low | medium] | terra
- **Gotchas.** none | ...
- **Depends on.** none | task N

- [ ] Implemented
- [ ] Reviewed

### 2. <Task name>

...

## Final check

The full test and build commands, a manual flow to try, and the screenshots to take with `visual-proof` if the UI changed.

## Notes

The orchestrator records the baseline (pass, fail, and skip counts, plus tests that already fail), escalations, deviations, follow-ups, and a `Handoff` entry if it stops mid-plan.
