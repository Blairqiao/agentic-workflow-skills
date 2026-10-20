# Antigravity agent guidelines

> Antigravity-specific rules that complement AGENTS.md without affecting other harnesses.

## Skill activation announcement

Whenever any skill is invoked or activated, such as `planning`, `brainstorm`, `grilling`, `domain-modeling`, `human-tdd`, `research`, `full-track`, `fast-track`, or `one-shot`, the agent must explicitly announce the skill activation in its chat response before executing steps:
`> **Skill Activated:** \`<skill-name>\` - <brief reason or scope>`

## Two-phase workflow and link placement

The planning phase produces the complete plan. The execution phase executes the named ready plan when explicitly instructed by the user, without repeating approval gates. A plan with consequential blockers cannot be ready. Material scope changes return to the planning phase. Fast-track repairs approved behavior and appends evidence to the parent proof when available; standalone fixes execute in a single chat after inline mini-spec approval.

Whenever finalizing or presenting a plan, mini-spec, or approval gate, always place a direct clickable link to the authoritative artifact at the very bottom of the chat response.

## Workflow invariants in boost mode

When running under an active `/boost` session, enforce all standard workflow invariants: keep candidate changes confined to `<main-repo>/.worktrees/<feature>`, or the workspace for fast-track, maintain workflow records in `/.agent-docs/`, capture verbatim red and green test evidence, and obtain independent review.
