# Fast-track record

Feature, status, approval reference, base revision, and date:

## Mini-spec and acceptance criteria

Summarize the bug or adjustment in two to three sentences. State whether `.agent-docs/CONTEXT.md` was consulted or updated.

| ID | Observable requirement | Verification |
| --- | --- | --- |

## Workspace and tree snapshots

Current workspace state, pre-existing user changes, and temporary-index `git write-tree` hashes:

- `S0` before task edits:
- `S1` after red test:
- `S2` after green implementation:
- `git diff --stat "$S1" "$S2" -- <test-paths>` output:

## Test amendments

List every test revision made after `S1` with its snapshot hash and reason, or state that none occurred.

## Review

Review method, independence, findings, resolutions, explicit sign-off on any test amendments, and verdict.

## Proof and walkthrough

Reproducible commands, verbatim output excerpts, UI or manual verification steps, and staged candidate paths.

### Documentation impact

Link project guides created or updated and record unresolved documentation gaps or contradictions, or explain why no documentation changes were needed. This section stays in the fast-track record; do not create a separate walkthrough.
