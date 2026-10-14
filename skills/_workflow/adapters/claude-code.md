# Claude Code adapter

Use the active session's tools and supported subagent configuration. Follow [repository-local worktree placement](../workspace.md). Use native worktree support only when it accepts `<main-repo>/.worktrees/`; otherwise use Git directly. Do not use a Claude-owned directory as a fallback. Give independent reviewers a fresh context using [the reviewer brief](../templates/reviewer-brief.md).

The installer allows automatic model selection for `full-track` and `fast-track`, while creating a Claude-specific copy of `one-shot` with `disable-model-invocation: true` so `one-shot` remains manual-only. Shared skill sources keep only `name` and `description`. Other skills and shared documentation are linked or copied according to the installation mode.

Select subagent models by universal capability tier: lightweight scanning for exploration, standard coding for scoped implementation, and high-reasoning for independent review and escalated fixes. Use available browser inspection tools for UI verification, and honor the harness's sandbox and permission controls.
