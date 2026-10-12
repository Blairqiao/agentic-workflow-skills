# Execution and delegation

Inputs: approved full/fast plan or autonomous one-shot plan, workspace, verification commands.

1. Maintain the [taskboard](templates/taskboard.md) for full/fast or progress section of the one-shot run document. Record task status, decisions, verification results, and blockers without copying whole logs into every entry.
2. Implement dependency-ready tasks. Fast-track performs all implementation in the current session. Full/one-shot can delegate independent tasks when the benefit justifies coordination; give simultaneous writers disjoint scopes and isolated resources.
3. For delegated work, provide [a scoped brief](templates/implementer-brief.md), requirements, workspace, and relevant commands. Model selection belongs to the active adapter. Do not create user-visible chats as an implementation mechanism unless requested.
4. Follow [test integrity](testing.md). Inspect returned changes and evidence rather than accepting unsupported success claims. Reproduce relevant results when evidence is missing, suspect, or the combined candidate changes; avoid repeating every suite after every handoff.
5. Resolve findings with concrete corrections. Use [independent review](review.md) for the completed change and optionally earlier for high-risk portions. Record review results before marking requirements done.

Routine questions within the design are implementation decisions. Apply the track's decision and authorization policy from [core](core.md) when scope changes. Continue independent tasks around blockers and use the same failure policy across implementation, tests, and review.

Completion: required tasks are implemented and reviewed, with remaining blockers accurately recorded.
