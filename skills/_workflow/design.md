# Design and specification

Inputs: request, repository facts, selected track, existing decisions.

1. Identify observable behavior, non-goals, and relevant failure cases. Consider compatibility, data, security, and performance when the change touches them.
2. When domain concepts are introduced, overloaded, or contested, invoke [domain-modeling](../domain-modeling/SKILL.md) and create or update `<main-repo>/.agent-docs/CONTEXT.md` inline so specifications and code share canonical terminology.
3. In full and fast, ask only about consequential unresolved choices. Use [grilling](../grilling/SKILL.md) when an interview would help; research facts before asking. In one-shot, choose reasonable behavior autonomously and record material alternatives and reasons, including rejected options.
4. Write numbered acceptance criteria, one observable requirement each, and identify automated or manual verification. Add interfaces, examples, or diagrams where they resolve ambiguity.
5. For full, use [the spec template](templates/spec.md) at `<main-repo>/.agent-docs/spec/<feature>.md` and keep the spec comprehensive. For fast, confirm the scope fit check and write a two to three sentence mini-spec and acceptance criteria in `<main-repo>/.agent-docs/fast-track/<feature>.md` using [the fast-track template](templates/fast-track.md). For one-shot, put design and decisions in `<main-repo>/.agent-docs/runs/<feature>.md` using [the run document](templates/run.md).

Completion: behavior, non-goals, domain terminology, material decisions, and testable acceptance criteria are documented. The approval gate happens once, after [planning](planning.md) for full or after the mini-spec for fast.
