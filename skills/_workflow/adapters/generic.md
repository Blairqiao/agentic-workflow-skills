# Generic harness adapter

Inspect the current harness's tools and permissions. Use available Git/worktree, test, and browser capabilities rather than inventing platform APIs or model identifiers. Follow [repository-local worktree placement](../workspace.md); if native tooling cannot honor that location, use Git directly instead of a harness-owned directory.

For review, prefer a native fresh-context agent, then an available independent session. If neither exists, apply the selected track's fallback in [review](../review.md). Keep implementation delegation conditional on the track and task independence.

Entry skills require explicit user invocation. If the harness cannot enforce manual invocation through metadata, follow their descriptions. Documentation lives beside the skill folders and can be read directly by relative path.
