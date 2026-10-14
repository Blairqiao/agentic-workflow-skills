# Design and specification

Inputs: request, repository facts, existing decisions or brief, and selected track when one exists.

## Shared decision rules

Apply these rules during standalone [brainstorming](../brainstorm/SKILL.md) and track design. They do not require starting a track or repeating an interview.

- Inspect relevant code, documentation, and the domain dictionary before asking about repository facts. Reuse settled decisions from the conversation and active feature record. If new evidence contradicts one, surface the conflict and revisit only affected decisions under the track's decision policy.
- Use [domain-modeling](../domain-modeling/SKILL.md) for new, overloaded, or contested domain concepts. Resolve and record meanings required by the chosen direction before making dependent choices. Continue independent branches; keep uncertainties about deferred alternatives, out-of-scope areas, and paused branches explicit in the active record. An explicit chat-only request keeps definitions in the conversation instead of writing files.
- In full, fast, or standalone interactive exploration, ask only about consequential unresolved choices. Use [grilling](../grilling/SKILL.md) for a decision needing deeper scrutiny, with a named scope and settled prerequisites. Its confirmation establishes shared understanding; the active track owns implementation approval.
- In one-shot, choose reasonable behavior autonomously and record material assumptions, alternatives, and reasons. Do not invoke interactive brainstorming or grilling.

## Specification in an active track

When a standalone brief exists, read it and incorporate its current decisions into the track's active document. Mark the brief handed off with a link to that document. Subsequent design changes belong in the track document. If the brief is paused, resolve consequential blockers under the selected track's decision policy before completing the specification. Use [brainstorm](../brainstorm/SKILL.md) only when further exploration would help; a sufficiently clear request or brief needs no new interview.

1. Identify observable behavior, non-goals, and relevant failure cases. Consider compatibility, data, security, and performance when the change touches them.
2. Apply the shared domain rules so specifications and code use canonical terminology. Record settled terms in `<main-repo>/.agent-docs/CONTEXT.md` or the relevant bounded-context dictionary.
3. Apply the shared decision rules to remaining consequential choices, preserving the selected track's interactive or autonomous policy.
4. Write numbered acceptance criteria, one observable requirement each, and identify automated or manual verification. Add interfaces, examples, or diagrams where they resolve ambiguity.
5. Record the specification in the track's active document under `<main-repo>/.agent-docs/` using a short, stable `<feature>` slug:
   - **Full-track.** Write the specification sections directly in `<main-repo>/.agent-docs/plans/<feature>.md` using [the combined spec-and-plan template](templates/plan.md).
   - **Fast-track.** Confirm the linear single-session scope fit check and write a two to three sentence mini-spec and acceptance criteria in `<main-repo>/.agent-docs/fast-track/<feature>.md` using [the fast-track template](templates/fast-track.md).
   - **One-shot.** Record the design and decisions in `<main-repo>/.agent-docs/runs/<feature>.md` using [the run document](templates/run.md).

Update existing feature documents in place so main sections reflect the current decision, keeping a brief decision history and archiving lengthy superseded material in `.agent-docs/archive/`.

Completion: behavior, non-goals, domain terminology, material decisions, and testable acceptance criteria are documented. The approval gate happens once, after [planning](planning.md) for full or after the mini-spec for fast.
