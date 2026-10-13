---
name: research
description: Use when explaining a project's documentation, auditing its codebase against documentation, or creating and maintaining missing project documentation. For project understanding and documentation, not general web research or code fixes.
---

# Research

Read repository guidance and locate existing project documentation and the domain dictionary. Identify the main repository using [workspace preparation](../_workflow/workspace.md), especially when working in a linked worktree.

## Select a mode

- **Explain** for "walk me through this project", documentation summaries, or an explicit `research explain` request. Read [Explain](../_workflow/research-explain.md).
- **Audit** for codebase re-audits, documentation cross-checks, updates, or an explicit `research audit` request. Read [Audit](../_workflow/research-audit.md).
- When intent does not identify an outcome, ask which mode the user wants before changing documentation. Follow the active track's ambiguity policy; one-shot chooses and records the mode itself.

Load only the selected procedure. Explain bootstraps documentation through Audit when usable project documentation is absent, then returns to the explanation. Disclose that extra work before starting it; respect explicit read-only constraints and report what cannot be created.

## Shared boundaries

Preserve established documentation locations. New project guides default to versioned `docs/`; audit records belong in `<main-repo>/.agent-docs/research/`. Keep the domain dictionary under [domain-modeling](../domain-modeling/SKILL.md). Follow [workspace preparation](../_workflow/workspace.md) before writing workflow records and use [unslop](../unslop/SKILL.md) for authored prose.

Support claims with documentation or source links and distinguish verified behavior, documented intent, and inference. Report code defects as findings. This skill changes documentation, not application behavior.
