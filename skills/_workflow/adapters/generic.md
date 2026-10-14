# Generic harness adapter

Inspect the current harness's tools and permissions. Use available Git, worktree, test, and browser inspection capabilities rather than inventing platform APIs or model identifiers. Follow [repository-local worktree placement](../workspace.md); if native tooling cannot honor `<main-repo>/.worktrees/`, use Git directly instead of a harness-owned directory.

For review, prefer a native fresh-context subagent packaged with [the reviewer brief](../templates/reviewer-brief.md), then an available independent session. If neither exists, apply the selected track's fallback in [review](../review.md). Map subagents by universal capability tier: lightweight scanning for exploration, standard coding for scoped implementation, and high-reasoning for review and escalated fixes. Keep implementation delegation conditional on the track and task independence.

Models may automatically select between `full-track` and `fast-track` based on scope, while `one-shot` requires explicit user invocation. Documentation lives beside the skill folders and can be read directly by relative path.
