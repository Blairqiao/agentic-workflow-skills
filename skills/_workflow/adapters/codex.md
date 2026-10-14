# Codex adapter

Use tools exposed in the current session and inspect their schemas. Follow [repository-local worktree placement](../workspace.md). Use a native worktree tool only if it can create checkouts inside `<main-repo>/.worktrees/`; otherwise use Git directly. Do not use Codex's managed directory as a fallback. Follow the active branch convention, normally `codex/` when no repository preference overrides it.

Use native subagents for delegated implementation and independent review. Give reviewers a fresh context with [the reviewer brief](../templates/reviewer-brief.md) rather than the implementation conversation. Select available models by universal capability tier: lightweight scanning for discovery, standard coding for scoped tasks, and high-reasoning for independent review and escalated fixes. Do not create sidebar chats as subagents.

Models may automatically invoke `full-track` and `fast-track` based on task scope, whereas `one-shot` keeps `agents/openai.yaml` with `allow_implicit_invocation: false`. Shared frontmatter remains portable, and the installer places `_workflow` beside the installed skills.

Use available browser inspection tools for UI verification. Existing user authorization remains subject to the session's permission controls. Report an actual permission block when it occurs rather than requesting blanket confirmation of known settings.
