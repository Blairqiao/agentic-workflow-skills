# Design and specification

Inputs: request, repository facts, selected track, and existing decisions.

1. Identify observable behavior, non-goals, and relevant failure cases. Consider compatibility, data, security, and performance when the change touches them.
2. When domain concepts are introduced, overloaded, or contested, invoke [domain-modeling](../domain-modeling/SKILL.md) and create or update `<main-repo>/.agent-docs/CONTEXT.md` inline so specifications and code share canonical terminology.
3. In full and fast, ask only about consequential unresolved choices. Use [grilling](../grilling/SKILL.md) when an interview would help, researching repository facts before asking. In one-shot, choose reasonable behavior autonomously and record material alternatives and reasons, including rejected options.
4. Write numbered acceptance criteria, one observable requirement each, and identify automated or manual verification. Add interfaces, examples, or diagrams where they resolve ambiguity.
5. Record the specification in the track's active document under `<main-repo>/.agent-docs/` using a short, stable `<feature>` slug:
   - **Full-track.** Write the specification sections directly in `<main-repo>/.agent-docs/plans/<feature>.md` using [the combined spec-and-plan template](templates/plan.md).
   - **Fast-track.** Confirm the linear single-session scope fit check and write a two to three sentence mini-spec and acceptance criteria in `<main-repo>/.agent-docs/fast-track/<feature>.md` using [the fast-track template](templates/fast-track.md).
   - **One-shot.** Record the design and decisions in `<main-repo>/.agent-docs/runs/<feature>.md` using [the run document](templates/run.md).

Update existing feature documents in place so main sections reflect the current decision, keeping a brief decision history and archiving lengthy superseded material in `.agent-docs/archive/`.

Completion: behavior, non-goals, domain terminology, material decisions, and testable acceptance criteria are documented. The approval gate happens once, after [planning](planning.md) for full or after the mini-spec for fast.
