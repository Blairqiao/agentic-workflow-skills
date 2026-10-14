---
name: human-tdd
description: >-
  Collaborative, intentional test-driven development. Use when the user requests human-tdd or human-guided TDD, wants to test intentionally, or asks for collaborative alignment, test grilling, and [Specific], [Intermediate], [Global] test categorization before writing code.
---

# Human-guided TDD

Collaborative, intentional testing workflow that contrasts with autopilot mode. Use this skill when the user wants to be directly involved in deciding what and how to test.

## Core principles

1. **Intentionality over volume.** Do not write tests just to write tests. Every test must have a clear purpose and verify behavior that matters.
2. **Model actual usage.** Tests should reflect how a user or caller interacts with the feature, not internal implementation details.
3. **Simplicity.** Tests must be easy to read. Their intent should be obvious from the code without convoluted setups or assertions.
4. **Speak up on brittle tests.** If a behavior can only be tested with heavy mocks or fragile setup, stop and tell the user. Propose a manual check in [verification](../_workflow/verification.md) instead of a brittle automated test.

## Workflow

### 1. Grilling and alignment

Before writing test code for a task:

- Agree on the core value of the feature and what needs verification.
- Invoke [grilling](../grilling/SKILL.md) if testing assumptions or boundaries need stress-testing.
- Focus on dynamic behavior, such as query behavior and error recovery, rather than static details like exact UI strings.

### 2. Categorize the tests

When proposing tests in the plan or task brief, tag each test idea:

- `[Specific]`: Localized component tests and focused edge cases for that module.
- `[Intermediate]`: Subsystem or domain-level interaction tests.
- `[Global]`: System-level invariants and core user flows.

### 3. Red-green execution with integrity

- Follow [test integrity](../_workflow/testing.md) for red execution, green implementation, and logged test amendments.
- Run the new or updated test first, record the verbatim red failure output, implement the minimal code to pass, and record the verbatim green pass output.
- Review the test code with the user to confirm it remains clear, direct, and faithful to actual usage.
