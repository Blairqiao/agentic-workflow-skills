# Independent review

Inputs: requirements, candidate diff, task boundaries, and observed verification results. Exclude the implementer's conversation and rationale from the review brief; include design decisions needed to understand intended behavior.

1. Use a fresh review subagent, including on fast-track. If unavailable, try an independent session supported by the harness. If neither is available, full/fast ask before substituting self-review; one-shot performs self-review and clearly records the loss of independence.
2. Check each acceptance criterion against the implementation and its automated or manual evidence. Review interfaces and failure behavior, and inspect the complete integration rather than isolated tasks only.
3. Audit test changes for weakened assertions, missing tests, fixture-specific implementation, or inappropriate mocks. Reproduce checks when evidence is suspect or a finding needs confirmation.
4. Review security when the change affects input handling, authorization, stored data, dependencies, or other identified boundaries. Verify dependency authorization already given rather than asking again. Check migrations for data loss, locking, and recovery.
5. Report blocking defects separately from optional polish, with locations and consequences. Resolve technical disputes using requirements and evidence. Apply the track's decision policy when a product choice is needed; one-shot decides it autonomously.

Record the verdict in the taskboard or run document using the fields in [the review template](templates/review.md). No separate review file or numeric score is required. Re-review corrections that affect findings; do not restart a full audit for unrelated wording changes.

Completion: blocking findings are resolved and verified, or explicitly prevent a complete outcome. The record states whether review was independent.
