# Antigravity agent guidelines

> Antigravity-specific rules that complement AGENTS.md without affecting other harnesses.

## Skill activation announcement

Whenever any skill is invoked or activated, such as `brainstorm`, `grilling`, `domain-modeling`, `human-tdd`, `research`, `orchestration-track`, `full-track`, `fast-track`, or `one-shot`, the agent must explicitly announce the skill activation in its chat response before executing steps:
`> 🛠️ **Skill Activated:** \`<skill-name>\` - <brief reason or scope>`

## Workflow invariants in boost mode

When running under an active `/boost` session, enforce all standard workflow invariants: keep candidate changes confined to `<main-repo>/.worktrees/<feature>`, or the workspace for fast-track, maintain workflow records in `/.agent-docs/`, capture verbatim red and green test evidence, and obtain independent review.
