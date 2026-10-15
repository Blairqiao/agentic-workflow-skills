# Antigravity adapter

Use the tools and model identifiers exposed in the active runner. Map subagent tasks by universal capability tier rather than hardcoded model IDs:

- **Lightweight scanning tier.** Use for bounded code retrieval, directory discovery, file searches, and symbol lookup.
- **Standard coding tier.** Use for scoped behavioral investigations and task implementation in `full-track` and `one-shot`. Fast-track permits read-only investigations, not implementation subagents.
- **High-reasoning tier.** Use for demanding investigations, architecture tradeoffs, independent review across all tracks, and fix escalations after round two.

Follow [discovery](../discovery.md#code-exploration-and-delegation) for read-only code exploration in every track. The orchestrator may read documentation directly. Select among supported models and reasoning settings according to the question's scope; use the shared fallback when delegation or explicit model selection is unavailable.

Give independent reviewers requirements, the candidate diff, and recorded test evidence in a fresh context using [the reviewer brief](../templates/reviewer-brief.md). Delegate implementation only when the selected track permits it and independent tasks justify coordination. Follow [repository-local worktree placement](../workspace.md), using a native worktree tool only when it accepts `<main-repo>/.worktrees/` and Git directly otherwise. Harness-owned directories are not fallback locations. Use available browser inspection tools for UI verification.

The installer supports the configured IDE and CLI user skill directories. Models may automatically select `full-track` or `fast-track` based on scope, whereas `one-shot` requires explicit user invocation.
