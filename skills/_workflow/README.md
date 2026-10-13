# Shared workflow procedures

This directory is documentation, not a discoverable skill. Entry skills select the track; [core](core.md) owns shared policy and sequencing. Read the procedure for the current phase rather than loading this entire directory.

| Procedure | Inputs | Completion |
| --- | --- | --- |
| [Discovery](discovery.md) | Repository and task | Relevant commands and constraints identified |
| [Design](design.md) | Request and discovered facts | Spec and decisions recorded |
| [Planning](planning.md) | Spec | Ordered tasks and verification defined |
| [Workspace](workspace.md) | Track and repository state | Safe working location and baseline recorded |
| [Execution](execution.md) | Plan and workspace | Required tasks implemented or honestly blocked |
| [Testing](testing.md) | Behavior and existing tests | Meaningful red/green evidence or suitable alternative |
| [Review](review.md) | Requirements and candidate diff | Findings resolved or explicitly reported |
| [Verification](verification.md) | Reviewed candidate | Relevant checks and reproducible proof |
| [Handoff](handoff.md) | Verified changes and artifacts | Candidate delivery ready for the user |
| [Research Explain](research-explain.md) | Project documentation and learning goal | Linked project explanation; missing documentation bootstrapped when permitted |
| [Research Audit](research-audit.md) | Codebase and current documentation | Documentation maintained with coverage, evidence, and unresolved findings recorded |

## Extracting a procedure into a skill

Keep each procedure's purpose, inputs, steps, and completion criteria together. Reference shared policy instead of copying it. Use relative links so the installed bundle works outside this repository.

To expose a procedure independently, add a sibling skill with a focused `name` and `description`, and have it read the existing procedure. Move the procedure only if ownership changes, then update its callers and validate installed links. The installer discovers any directory containing `SKILL.md`; `_workflow` remains ordinary documentation. Add manual-only adapter metadata only when that entry point should require explicit invocation.

[Templates](templates/) describe artifact contents, not mandatory empty sections. Resolve template links against the installed bundle while reading them; rewrite or omit those instructional links when creating an artifact in another directory. [Adapters](adapters/) hold harness mechanics; shared procedures describe outcomes. Source files here are maintained once and installed beside the public skills.
