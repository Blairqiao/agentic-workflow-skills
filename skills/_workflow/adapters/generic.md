# Generic harness adapter

Inspect the current harness's tools and permissions. Use available Git, worktree, test, and browser inspection capabilities rather than inventing platform APIs or model identifiers. Follow [repository-local worktree placement](../workspace.md); if native tooling cannot honor `<main-repo>/.worktrees/`, use Git directly instead of a harness-owned directory.

Use available subagents for read-only code exploration under [discovery](../discovery.md#code-exploration-and-delegation), including in fast-track. Documentation may be read directly by the orchestrator. Map supported models and reasoning settings by universal capability tier: lightweight scanning for bounded retrieval, standard coding for scoped investigations and permitted implementation, and high-reasoning for demanding investigations, architectural reasoning, review, and escalated fixes. Use discovery's fallback when subagents or explicit model selection are unavailable. Keep implementation delegation conditional on the track and task independence.

For review, prefer a native fresh-context subagent packaged with [the reviewer brief](../templates/reviewer-brief.md), then an available independent session. If neither exists, apply the selected track's fallback in [review](../review.md).

Models may automatically select between `full-track` and `fast-track` based on scope, while `one-shot` requires explicit user invocation. Documentation lives beside the skill folders and can be read directly by relative path.
