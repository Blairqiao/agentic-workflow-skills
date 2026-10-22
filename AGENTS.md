# Agent guidelines for the agentic workflow

Read [common policy](/skills/_workflow/core.md), applying its supplied-context reuse rule. Load current operation details and only the active harness adapter. Links are references, not a recursive reading checklist. Applicable project guidance and `/.agent-docs/CONTEXT.md` govern local constraints and terminology.

## Routing

Select the track automatically when implementation planning or execution is requested:

- [Orchestration-track](/skills/orchestration-track/SKILL.md) for large multi-part initiatives, project jumpstarts, complex multi-service features, and full codebase audits or refactors, with delegated vertical slices in an isolated worktree.
- [Full-track](/skills/full-track/SKILL.md) for isolated features and subsystem debugging, with mandated implementation delegation.
- [Fast-track](/skills/fast-track/SKILL.md) for a single bounded small fix or simple addition, without implementation subagents. Escalate when scope outgrows one linear task.
- [One-shot](/skills/one-shot/SKILL.md) only on explicit request, with autonomous planning and execution.

Use [planning](/skills/planning/SKILL.md) for implementation planning, [brainstorm](/skills/brainstorm/SKILL.md) for exploratory framing, [grilling](/skills/grilling/SKILL.md) for consequential decisions, [domain-modeling](/skills/domain-modeling/SKILL.md) for shared terminology, and [research](/skills/research/SKILL.md) for project explanation or documentation audits. Clear requests need no ceremonial interview. Exploration and ready status alone never authorize implementation.

Interactive approval gates, including every follow-up repair, follow core's inline mini-spec and explicit approval policy before code or test edits. One-shot retains its autonomous exception. End every gate response with the direct authoritative artifact link.

## Repository constraints

- Announce a skill's first activation before using it with `> **Skill Activated:** \`<skill-name>\` - <reason>`. Apply [unslop](/skills/unslop/SKILL.md) to all authored prose. Reusing the same active instructions needs no repeat announcement.
- Follow [workspace preparation](/skills/_workflow/workspace.md) before creating worktrees or writing `.agent-docs/`. Keep records in the parent repository, use `.git/info/exclude` exclusively for workflow ignores, and preserve protected edits.
- In authored `.agent-docs/`, `docs/`, and `AGENTS.md`, use repository-rooted internal links and image embeds. Never use host-absolute paths. Embed screenshot proof as `![Caption](/.agent-docs/proofs/images/<image>.png)`.
- Follow [test integrity](/skills/_workflow/testing.md), [independent review](/skills/_workflow/review.md), and [handoff](/skills/_workflow/handoff.md) when those operations apply. Record terminal proof before claiming success. Stage changes for user-owned commits; never commit, push, or deploy during execution.
- Ask about consequential ambiguous requirements in interactive tracks. Record one-shot decisions and rationale autonomously. Disclose missing evidence, shortcuts, and debt. Explain flawed approaches before implementing them.
- Obtain explicit authorization for new third-party dependencies and destructive operations. Never overwrite unrelated work or silently change approved scope.
