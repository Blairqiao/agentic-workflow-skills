# Codex adapter

Use tools exposed in the current session and inspect their schemas. Follow [repository-local worktree placement](../workspace.md). Use a native worktree tool only if it can create inside `<main-repo>/.worktrees/`; otherwise use Git directly. Do not use Codex's managed directory as a fallback. Follow the active branch convention, normally `codex/` when no repository preference overrides it.

Use native subagents for delegated implementation and independent review. Reviewers need fresh context with the requirements and artifacts, not the implementation conversation. Choose available models by task needs; do not translate another harness's model aliases into guessed model IDs. Do not create sidebar chats as subagents.

Entry skills keep `agents/openai.yaml` with `allow_implicit_invocation: false`. Shared frontmatter remains portable. The installer places the documentation beside the installed skills.

Use available browser tools for UI verification. Existing user authorization remains subject to the session's permission controls. Report an actual permission block when it occurs rather than requesting blanket confirmation of known settings.
