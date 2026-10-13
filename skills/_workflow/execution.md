# Execution and delegation

Inputs: approved full/fast plan or autonomous one-shot plan, workspace, verification commands.

1. Maintain [the taskboard](templates/taskboard.md) for full, [the fast-track record](templates/fast-track.md) for fast, or the progress section of [the one-shot run document](templates/run.md). Record task status, decisions, verification results, and blockers without copying whole logs into every entry.
2. Implement dependency-ready tasks. Fast-track performs all implementation as a single task in the current session. Full and one-shot can delegate independent tasks when the benefit justifies coordination; give simultaneous writers disjoint scopes and isolated resources.
3. For delegated work, provide [a scoped brief](templates/implementer-brief.md), requirements, workspace, and relevant commands. Model selection belongs to the active adapter. Do not create user-visible chats as an implementation mechanism unless requested.
4. Follow [test integrity](testing.md). Inspect returned changes and evidence rather than accepting unsupported success claims. Reproduce relevant results when evidence is missing, suspect, or the combined candidate changes; avoid repeating every suite after every handoff.
5. Resolve findings with concrete corrections, capping failed task implementation attempts at 3 and review-fix cycles at 3 rounds. Use [independent review](review.md) for the completed change and optionally earlier for high-risk portions. Record review results before marking requirements done.

Routine questions within the design are implementation decisions. Apply the track's decision, escalation, and authorization policy from [core](core.md) when scope changes or retry caps are reached. Continue independent tasks around blockers and use the same failure policy across implementation, tests, and review.

Completion: required tasks are implemented and reviewed, with remaining blockers accurately recorded.
