# Project discovery

Inputs: repository, requested change, and existing project guidance or profile.

1. Read applicable repository instructions, `<main-repo>/.agent-docs/CONTEXT.md` or `<main-repo>/.agent-docs/CONTEXT-MAP.md` when present, existing project guides, and relevant scripts, CI configuration, manifests, and test configuration. Follow the token-saving reading rule in [core](core.md): read only the active `.agent-docs/` records for the feature and skip `.agent-docs/archive/` unless historical context is directly needed. Cross-check documentation relevant to the requested change against source and record gaps or contradictions. Prefer directly observed facts over stale documentation, while instructions and the shared domain dictionary govern authorization, canonical terminology, and conventions.
2. Identify the commands and test tiers needed for this change, relevant test layout, hooks that rewrite files, and affected service or security boundaries. Inspect environment variable file names and committed templates without reading local secret values.
3. Reuse a verified profile where useful, checking facts affected by configuration changes. If repeated discovery warrants a profile, use [the profile template](templates/profile.md); otherwise record relevant findings in the combined plan, fast-track record, or one-shot run document. No separate confirmation gate is needed.
4. Read only the active harness adapter: [Codex](adapters/codex.md), [Antigravity](adapters/antigravity.md), [Claude Code](adapters/claude-code.md), or [generic](adapters/generic.md). Use available tools and check their schemas rather than guessing APIs.

Run a baseline once when it helps distinguish pre-existing failures. Calibrate an unfamiliar or suspect test runner with a deliberate failing test only when needed, in a disposable workspace. Do not run repeated suites or fresh installations merely to populate a profile.

Use [research](../research/SKILL.md) when project explanation or documentation audit is requested. Routine discovery checks the affected area; it does not automatically bootstrap all project documentation or audit the whole repository. Missing documentation outside the change's scope is a recorded gap.

Completion: relevant commands, domain terminology, constraints, service needs, and unverified facts are recorded sufficiently to design and plan the change.
