---
name: planning
description: Consolidate the entire planning phase under /planning. Explores problem framing with brainstorm, models domain terms with domain-modeling, stress-tests architecture with grilling when needed, and finalizes with an authoritative plan at /.agent-docs/plans/<feature>.md with link placed at the bottom.
---

# Planning phase

Apply supplied-context reuse from [workflow core](../_workflow/core.md). Load [planning procedure](../_workflow/planning.md) for plan authoring and [design rules](../_workflow/design.md) when requirements or architectural decisions need exploration. Links alone do not require recursive loading.

## Purpose and boundaries

The planning phase consolidates exploratory problem framing, domain terminology modeling, architectural stress-testing, and plan authoring into a focused session. Planning never edits implementation code or tests.

A clear request can proceed directly to plan drafting. An exploratory or ambiguous request uses iterative discovery.

## Workflow sequence

1. **Problem framing and discovery.** When requirements need exploration, explore user needs and boundaries by invoking [brainstorm](../brainstorm/SKILL.md). When new or conflicting domain terminology arises, invoke [domain-modeling](../domain-modeling/SKILL.md) to record canonical domain definitions in `<main-repo>/.agent-docs/CONTEXT.md`.
2. **Architectural stress-testing.** When architectural choices, trade-offs, security considerations, or failure modes require deep scrutiny, invoke [grilling](../grilling/SKILL.md) across the decision frontier to eliminate silent assumptions.
3. **Author authoritative plan.** Synthesize settled decisions directly into `<main-repo>/.agent-docs/plans/<feature>.md` using [the plan template](../_workflow/templates/plan.md). Include execution identity, starting revision, target checkout, target branch, protected user edits, selected executor, non-goals, interfaces, and numbered acceptance criteria. A plan with unresolved consequential blockers cannot be marked ready.
4. **Finalize and hand off.** When the plan is ready for implementation:
   - Present scope, affected files, strategy, and acceptance criteria inline in chat.
   - Provide the copyable execution instruction specifying the exact plan path and target checkout for the execution phase, such as [full-track](../full-track/SKILL.md) or harness-specific execution under [the Antigravity adapter](../_workflow/adapters/antigravity.md).
   - **Link placement rule:** Always place a direct, clickable file link to the authoritative plan artifact at the very bottom of the chat response for immediate user access.
