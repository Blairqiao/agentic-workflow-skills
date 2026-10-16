# Antigravity agent guidelines

> Antigravity-specific rules that complement AGENTS.md without affecting other harnesses.

## Slash command guidance

1. **Boost recommendation.** The agent cannot run `/boost` directly. When an investigation involves subtle race conditions or complex architectural tradeoffs, or when a task implementation or review reaches round two of fix escalation, recommend that the user invoke `/boost` for that step.
2. **Workflow invariants in boost mode.** When executing under `/boost`, enforce all standard workflow invariants from `AGENTS.md`:
   - Keep candidate changes inside `<main-repo>/.worktrees/<feature>` for full-track and one-shot runs, or the current workspace for fast-track runs.
   - Maintain workflow records in `/.agent-docs/`.
   - Follow test integrity by capturing verbatim red failure and green pass outputs before and after implementation.
   - Require independent review packaged with the reviewer brief before handoff.
