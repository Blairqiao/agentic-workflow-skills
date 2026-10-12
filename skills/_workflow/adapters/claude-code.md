# Claude Code adapter

Use the active session's tools and supported subagent/model configuration. Follow [repository-local worktree placement](../workspace.md). Use native worktree support only when it accepts `<main-repo>/.worktrees/`; otherwise use Git directly. Do not use a Claude-owned directory as a fallback. Reviewers receive a fresh context with requirements and artifacts.

The installer creates Claude-specific copies of the three entry skills and adds `disable-model-invocation: true` to those copies. Shared sources keep only `name` and `description`. Other skills and shared documentation may be linked or copied depending on the installation mode.

Do not prescribe model IDs in portable procedures. Select among supported models by task needs. Use available browser tools for UI verification, and honor the harness's sandbox and permission controls.
