# Design and specification

Inputs: request, repository facts, selected track, existing decisions.

1. Identify observable behavior, non-goals, and relevant failure cases. Consider compatibility, data, security, and performance when the change touches them.
2. In full/fast, ask only about consequential unresolved choices. Use [grilling](../grilling/SKILL.md) when an interview would help; research facts before asking. In one-shot, choose reasonable behavior autonomously and record material alternatives and reasons, including rejected options.
3. Write numbered acceptance criteria, one observable requirement each, and identify automated or manual verification. Add interfaces, examples, or diagrams where they resolve ambiguity.
4. For full/fast, use [the spec template](templates/spec.md) and keep the spec comprehensive. For one-shot, put design and decisions in [the run document](templates/run.md).

Completion: behavior, non-goals, material decisions, and testable acceptance criteria are documented. The approval gate happens once, after [planning](planning.md); this procedure does not create a separate gate.
