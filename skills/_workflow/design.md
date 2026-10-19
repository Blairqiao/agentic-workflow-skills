# Design and specification

Inputs: planning phase request, repository facts, existing decisions or brief, and selected executor when known. The planning phase owns design and plan writing; the execution phase adopts the completed plan.

## Shared decision rules

Apply these rules during standalone [brainstorming](../brainstorm/SKILL.md) and track design. They do not require starting a track or repeating an interview.

- Inspect relevant code, documentation, and the domain dictionary before asking about repository facts. Reuse settled decisions from the conversation and active feature record. If new evidence contradicts one, surface the conflict and revisit only affected decisions under the planning policy.
- Use [domain-modeling](../domain-modeling/SKILL.md) for new, overloaded, or contested domain concepts. Resolve and record meanings required by the chosen direction before making dependent choices. Continue independent branches; keep uncertainties about deferred alternatives, out-of-scope areas, and paused branches explicit in the active record. An explicit chat-only request keeps definitions in the conversation instead of writing files.
- In interactive exploration, ask only about consequential unresolved choices. Use [grilling](../grilling/SKILL.md) for a decision needing deeper scrutiny, with a named scope and settled prerequisites. Its confirmation establishes shared understanding. The execution phase requires an explicit execution instruction for the ready plan.
- In one-shot, choose reasonable behavior autonomously and record material assumptions, alternatives, and reasons. Do not invoke interactive brainstorming or grilling.

## Specification in planning

When a standalone brief exists, read it and incorporate its current decisions into the active plan. Mark the brief handed off with a link to that document. Subsequent design changes belong in the track document. If the brief is paused, resolve consequential blockers under the planning policy before completing the specification. Use [planning](../planning/SKILL.md) or [brainstorm](../brainstorm/SKILL.md) only when further exploration would help; a sufficiently clear request or brief needs no new interview.

1. Identify observable behavior, non-goals, and relevant failure cases. Consider compatibility, data, security, and performance when the change touches them.
2. Apply the shared domain rules so specifications and code use canonical terminology. Record settled terms in `<main-repo>/.agent-docs/CONTEXT.md` or the relevant bounded-context dictionary.
3. Apply the shared decision rules to remaining consequential choices, preserving the selected track's interactive or autonomous policy.
4. Write numbered acceptance criteria, one observable requirement each, and identify automated or manual verification. Add interfaces, examples, or diagrams where they resolve ambiguity.
5. Record the specification in the active plan under `<main-repo>/.agent-docs/` using a short, stable `<feature>` slug:
   - **Interactive tracks.** Write directly in `<main-repo>/.agent-docs/plans/<feature>.md` using [the combined spec-and-plan template](templates/plan.md). Full, boost, and experimental orchestration share this planning handoff. A standalone fast-track fix executes in a single chat using a lean mini-spec; a follow-up defect within approved behavior continues in execution with its parent plan and proof.
   - **One-shot.** Record design and decisions in `<main-repo>/.agent-docs/runs/<feature>.md` using [the run document](templates/run.md), under either chosen executor.

Update existing feature documents in place so main sections reflect the current decision, keeping a brief decision history and archiving lengthy superseded material in `.agent-docs/archive/`.

Completion: behavior, non-goals, domain terminology, material decisions, and testable acceptance criteria are documented. Complete [planning](planning.md) and hand off to execution. A ready plan requires explicit execution authorization; execution does not repeat the interview or approval. Always place a direct clickable link to the authoritative plan artifact at the very bottom of the chat response.
