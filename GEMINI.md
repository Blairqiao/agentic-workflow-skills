# Antigravity agent guidelines

Follow [shared guidance](/AGENTS.md), applying common policy's supplied-context reuse rule. Load only current operation details and the [Antigravity adapter](/skills/_workflow/adapters/antigravity.md) when its contents are needed. Reuse complete applicable instructions already supplied in the conversation.

Use only tools and model identifiers exposed by the active session. Skill activation does not activate native `/boost`. Follow the adapter's evidence requirements before claiming boost is active and preserve workflow invariants under every executor.
