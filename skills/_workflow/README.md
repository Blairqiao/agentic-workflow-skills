# Shared workflow procedures

This directory contains internal workflow procedures rather than discoverable skills. Entry skills select or confirm the track, while [core](core.md) owns shared policy, phase ordering, artifact lifecycle, and retry rules. Read only the procedure for the active phase rather than loading the entire directory at once.

| Procedure | Inputs | Completion |
| --- | --- | --- |
| [Discovery](discovery.md) | Repository and task | Relevant commands, terminology, and constraints identified |
| [Workspace](workspace.md) | Track and repository state | `.git/info/exclude` configured, safe working location prepared, and baseline recorded |
| [Design](design.md) | Request and discovered facts | Specification sections and domain terms recorded |
| [Planning](planning.md) | Specification and commands | Ordered tasks, verification strategy, and approval completed |
| [Execution](execution.md) | Plan and workspace | Required tasks implemented or rolled back and documented on cap exhaustion |
| [Testing](testing.md) | Behavior and existing tests | Recorded red and green command evidence and logged test amendments |
| [Review](review.md) | Requirements, diff, and test evidence | Findings resolved or escalated after three rounds |
| [Verification](verification.md) | Reviewed candidate | Reproducible checks, embedded UI evidence, and combined proof and walkthrough |
| [Handoff](handoff.md) | Verified candidate and records | In-place changes staged or worktree merge command provided without target-branch commits |
| [Research Explain](research-explain.md) | Project documentation and learning goal | Source-linked project explanation, bootstrapping missing guides via Audit when permitted |
| [Research Audit](research-audit.md) | Codebase and current documentation | Maintained guides updated and coverage record written in `.agent-docs/research/` |

## Extracting a procedure into a skill

Keep each procedure's purpose, inputs, steps, and completion criteria in one file. Link to [core](core.md), [workspace](workspace.md), [testing](testing.md), and [handoff](handoff.md) instead of duplicating shared policy. Use relative links so the installed bundle works outside this repository.

To expose a procedure as an independently invocable skill, add a directory under `skills/` with a focused `SKILL.md` that links to the procedure. The installer automatically discovers directories containing `SKILL.md` while copying or linking `_workflow` alongside them. Add manual-invocation adapter metadata only when the skill must never be selected automatically by a model.

[Templates](templates/) define artifact structure and omit empty sections when unused. Resolve links relative to the installed bundle while reading templates, and rewrite or omit instructional links when writing files under `<main-repo>/.agent-docs/`. [Adapters](adapters/) hold harness-specific mechanics while shared procedures stay portable.
