# Independent review brief

Provide this brief to a fresh review subagent or independent session. Exclude the implementer's conversation history and internal reasoning.

## Candidate context

- **Workspace and base revision.**
- **Candidate diff command or patch.** Pass `git diff <base-revision>` covering all candidate code, test, configuration, and documentation edits.
- **Domain dictionary.** Relevant canonical terms from `<main-repo>/.agent-docs/CONTEXT.md` when present.

## Requirements and design decisions

- **Acceptance criteria.** Numbered observable requirements from the approved plan, fast-track record, or one-shot run document.
- **Settled design decisions.** Approved architectural choices, non-goals, and authorized dependency or boundary changes.

## Recorded verification evidence

- **Red and green test outputs.** Exact commands and verbatim failure and pass excerpts recorded during execution.
- **Test amendments.** Every test revision made after red, or to an existing test expectation, with its stated reason.
- **Suite and UI evidence.** Observed test runner, build, static check, and browser verification outputs.

## Reviewer instructions

Follow [independent review](../review.md) and return the verdict using [the review record template](review.md):

1. Check every acceptance criterion against the candidate diff and observed verification output.
2. Audit all test changes against the recorded red and green outputs for weakened assertions, skipped cases, fixture hardcoding, or inappropriate mocks, and explicitly accept or reject each logged test amendment.
3. Check domain terminology compliance and relevant security, data, or migration boundaries.
4. Reproduce commands directly when evidence is incomplete or suspect, and separate blocking defects from optional polish with exact file locations.
