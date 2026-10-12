# Project discovery

Inputs: repository, requested change, existing project guidance or profile.

1. Read applicable repository instructions and relevant scripts, CI configuration, manifests, and test configuration. Prefer directly observed facts over stale documentation; instructions still govern authorization and conventions.
2. Identify the commands and test tiers needed for this change, relevant test layout, hooks that rewrite files, and affected service or security boundaries. Inspect env file names and committed templates without reading local secret values.
3. Reuse a verified profile where useful, checking facts affected by configuration changes. If repeated discovery warrants a profile, use [the profile template](templates/profile.md); otherwise record relevant findings in the plan or run document. No separate confirmation gate is needed.
4. Read only the active harness adapter: [Codex](adapters/codex.md), [Antigravity](adapters/antigravity.md), [Claude Code](adapters/claude-code.md), or [generic](adapters/generic.md). Use available tools and check their schemas rather than guessing APIs.

Run a baseline once when it helps distinguish pre-existing failures. Calibrate an unfamiliar or suspect test runner with a deliberate failing test only when needed, in a disposable workspace. Do not require repeated suites or fresh installations merely to populate a profile.

Completion: relevant commands, constraints, service needs, and unverified facts are recorded sufficiently to plan the change.
