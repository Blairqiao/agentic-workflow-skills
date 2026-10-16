# Antigravity adapter

Use the tools and model identifiers exposed in the active runner. Map subagent tasks by universal capability tier rather than hardcoded model IDs:

- **Lightweight scanning tier.** Use for bounded code retrieval, directory discovery, file searches, and symbol lookup.
- **Standard coding tier.** Use for scoped behavioral investigations and task implementation in `full-track` and `one-shot`. Full-track mandates subagents for task implementation. Fast-track permits read-only investigations, not implementation subagents.
- **High-reasoning tier.** Use for demanding investigations, architecture tradeoffs, independent review across all tracks, and fix escalations after round two.

Follow [discovery](../discovery.md#code-exploration-and-delegation) for read-only code exploration in every track. The orchestrator may read documentation directly. Select among supported models and reasoning settings according to the question's scope; use the shared fallback when delegation or explicit model selection is unavailable.

Give independent reviewers requirements, the candidate diff, and recorded test evidence in a fresh context using [the reviewer brief](../templates/reviewer-brief.md). Delegate implementation in full-track where subagents are mandated for task implementation, and in one-shot when independent tasks justify coordination. Follow [repository-local worktree placement](../workspace.md), using a native worktree tool only when it accepts `<main-repo>/.worktrees/` and Git directly otherwise. Harness-owned directories are not fallback locations. Use available browser inspection tools for UI verification.

Recommend that the user invoke `/boost` for demanding investigations, subtle concurrency or race conditions, and fix escalations after round two. When running inside an active `/boost` session, enforce all standard workflow invariants: keep changes confined to `<main-repo>/.worktrees/<feature>` for full-track and one-shot runs or the current workspace for fast-track runs, record decisions in `/.agent-docs/`, enforce red and green test evidence capture, and obtain independent review. Do not permit `/boost` to bypass test discipline or make unverified direct edits.

The installer supports the configured IDE and CLI user skill directories. Models may automatically select `full-track` or `fast-track` based on scope, whereas `one-shot` requires explicit user invocation.
