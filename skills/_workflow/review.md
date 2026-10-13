# Independent review

Inputs: requirements, candidate diff, task boundaries, and observed verification results. Exclude the implementer's conversation and rationale from the review brief; include design decisions needed to understand intended behavior.

1. Use a fresh review subagent, including on fast-track. If unavailable, try an independent session supported by the harness. If neither is available, full and fast ask before substituting self-review; one-shot performs self-review and clearly records the loss of independence.
2. Check each acceptance criterion against the implementation and its automated or manual evidence. Verify that new types, identifiers, and specifications respect `<main-repo>/.agent-docs/CONTEXT.md` when present. Review interfaces and failure behavior, and inspect the complete integration rather than isolated tasks only.
3. Audit test changes for weakened assertions, missing tests, fixture-specific implementation, or inappropriate mocks. For in-place runs, inspect `git diff "$S0" "$S2"` to isolate the agent's changes and verify `git diff --stat "$S1" "$S2" -- <test-paths>` is empty. Explicitly accept or reject every `test(amend)` commit or in-place test revision listed in the proof. Reproduce checks when evidence is suspect or a finding needs confirmation.
4. Review security when the change affects input handling, authorization, stored data, dependencies, or other identified boundaries. Verify dependency authorization already given rather than asking again. Check migrations for data loss, locking, and recovery.
5. Report blocking defects separately from optional polish, with locations and consequences. Resolve technical disputes using requirements and evidence. Cap review-fix cycles at 3 rounds before escalating to the user in full and fast or reporting an incomplete outcome in one-shot. Apply the track's decision policy when a product choice is needed; one-shot decides it autonomously.

Record the verdict in the taskboard, fast-track record, or run document using the fields in [the review template](templates/review.md). No separate review file or numeric score is required. Re-review corrections that affect findings; do not restart a full audit for unrelated wording changes.

Check affected project documentation against the resulting behavior and source evidence. Verify updated links and relevant instructions, and ensure intended requirements were not silently rewritten to hide code defects. Keep this check scoped to the change; record unrelated documentation gaps for a separate research audit.

Completion: blocking findings are resolved and verified, every test amendment is explicitly accepted or rejected, or unresolved findings explicitly prevent a complete outcome. The record states whether review was independent.
