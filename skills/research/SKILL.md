---
name: research
description: Use when explaining a project's documentation, auditing its codebase against documentation, or creating and maintaining missing project documentation. For project understanding and documentation, not general web research or code fixes.
---

# Research

Read repository guidance and locate existing project documentation and the domain dictionary. Identify the main repository and configure `.git/info/exclude` using [workspace preparation](../_workflow/workspace.md) before writing workflow records, especially when working in a linked worktree.

## Select a mode

- **Explain.** Use for requests to walk through a project, summarize documentation, or run `research explain`. Read [Explain](../_workflow/research-explain.md).
- **Audit.** Use for codebase re-audits, documentation cross-checks, documentation updates, or `research audit` requests. Read [Audit](../_workflow/research-audit.md).
- **Ambiguous requests.** Ask which mode the user wants before changing documentation, following the active track's ambiguity policy. One-shot selects and records the mode autonomously.

Load only the selected procedure. Explain bootstraps documentation through Audit when usable project documentation is absent, then returns to the explanation. Disclose that extra work before starting it, respect explicit read-only constraints, and report what cannot be created.

## Shared boundaries

Preserve established documentation locations. New project guides default to versioned `docs/`, while audit records belong in `<main-repo>/.agent-docs/research/` using [the research audit template](../_workflow/templates/research-audit.md). Keep the domain dictionary under [domain-modeling](../domain-modeling/SKILL.md) and apply [unslop](../unslop/SKILL.md) to authored prose.

Support claims with documentation or source links and distinguish verified behavior, documented intent, and inference. Report code defects as findings. This skill changes documentation, not application behavior.
