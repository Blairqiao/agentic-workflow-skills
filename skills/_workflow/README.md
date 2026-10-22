# Shared workflow procedures

These internal procedures travel beside the installed skills and have no discoverable `SKILL.md`. [Core](core.md) owns routing, phase boundaries, authorization, records, and retry limits. Apply its supplied-context reuse policy and load current operation details only. Links are optional references unless a current step explicitly requires their contents.

| Procedure | Purpose |
| --- | --- |
| [Discovery](discovery.md) | Inspect project facts, terminology, commands, and relevant constraints |
| [Workspace](workspace.md) | Prepare candidate checkout and parent-root artifacts with safe isolation |
| [Design](design.md) | Resolve design phase decisions and observable requirements |
| [Planning](planning.md) | Write a ready plan and an explicit execution handoff |
| [Execution](execution.md) | Execute the adopted plan using the selected executor |
| [Testing](testing.md) | Capture meaningful red and green evidence and test amendments |
| [Review](review.md) | Assess candidate requirements, test integrity, and integration risks |
| [Verification](verification.md) | Check the actual candidate and write proof and walkthrough |
| [Handoff](handoff.md) | Stage scoped changes and provide usable integration instructions |
| [Research Explain](research-explain.md) | Explain project documentation with source evidence |
| [Research Audit](research-audit.md) | Audit documentation against maintained code and record coverage |

[Planning](../planning/SKILL.md), [brainstorm](../brainstorm/SKILL.md), and [grilling](../grilling/SKILL.md) operate in the planning phase and write settled planning directly to the [plan](templates/plan.md). A [brief](templates/brief.md) holds paused or abandoned exploration. [Domain-modeling](../domain-modeling/SKILL.md) owns the canonical dictionary.

The execution phase consumes a named ready plan when the user instructs execution. Boost owns its internal coordination; the custom layer supplies constraints and deliverables. Full-track uses custom non-boost delegation. Orchestration-track is automatically selected for large initiatives and mandates delegated vertical slices. Fast-track executes standalone fixes in a single chat. Every follow-up repair in interactive tracks requires new inline mini-spec approval before code or test edits, including repairs to parent-approved behavior. One-shot is the autonomous exception with either executor.

Keep procedure ownership clear and link shared rules instead of repeating them in every skill. Installed resources need relative links. Templates record the approval gates owned by core; they do not introduce independent gates. Rewrite instructional links for the destination when creating parent-root `.agent-docs` records. Concurrent runs use distinct execution identities.

The installer discovers directories containing `SKILL.md` and installs `_workflow` alongside them. Add a skill only for an independently invocable capability. Keep explicit-only invocation policy in supported metadata and prose rather than inventing runner APIs.
