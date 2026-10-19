# Antigravity adapter

Use the tools and model identifiers exposed in the active runner. Map subagent tasks by universal capability tier rather than hardcoded model IDs:

- **Lightweight scanning tier.** Use for bounded code retrieval, directory discovery, file searches, and symbol lookup.
- **Standard coding tier.** Use for scoped behavioral investigations and task implementation in `orchestration-track` with vertical slices dispatched to `flash` or `flash_lite`, `full-track`, and `one-shot`. Orchestration-track and full-track mandate subagents for task implementation. Fast-track permits read-only investigations, not implementation subagents.
- **High-reasoning tier.** Use for demanding investigations, architecture tradeoffs, independent review across all tracks, and fix escalations after round two, such as `pro`.

Follow [discovery](../discovery.md#code-exploration-and-delegation) for read-only code exploration in every track. The orchestrator may read documentation directly. Select among supported models and reasoning settings according to the question's scope; use the shared fallback when delegation or explicit model selection is unavailable. Antigravity orchestrators rely on automatic reactive wakeups upon subagent completion, background task events, or scheduled timers, and must never poll or loop on task status.

Give independent reviewers requirements, the candidate diff, and recorded test evidence in a fresh context using [the reviewer brief](../templates/reviewer-brief.md). Delegate implementation in orchestration-track with vertical slices dispatched to Flash subagents, in full-track where subagents are mandated for task implementation, and in one-shot when independent tasks justify coordination. Follow [repository-local worktree placement](../workspace.md), using a native worktree tool only when it accepts `<main-repo>/.worktrees/` and Git directly otherwise. Harness-owned directories are not fallback locations. Use available browser inspection tools for UI verification.

When running under an active `/boost` session, enforce all standard workflow invariants: keep candidate changes confined to `<main-repo>/.worktrees/<feature>`, or the workspace for fast-track, maintain workflow records in `/.agent-docs/`, capture verbatim red and green test evidence, and obtain independent review. Do not permit `/boost` to bypass test discipline or make unverified direct edits.

The installer supports the configured IDE and CLI user skill directories. Models may automatically select `orchestration-track`, `full-track`, or `fast-track` based on scope, whereas `one-shot` requires explicit user invocation.
