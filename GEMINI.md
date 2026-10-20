# Antigravity agent guidelines

Use [AGENTS.md](/AGENTS.md) and common policy for routing, supplied context, approval gates, evidence, and safety. Antigravity-specific entry, reactive wakeups, and native boost constraints live in the [Antigravity adapter](/skills/_workflow/adapters/antigravity.md). Load it only for this runner. Do not treat a skill as activating `/boost`; verify the active session and use observable evidence before claiming native behavior verified.
