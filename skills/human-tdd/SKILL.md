---
name: human-tdd
description: >-
  Collaborative, intentional test-driven development (human-guided TDD). Use when the user requests human-tdd or human-guided TDD, wants to test intentionally, or asks for collaborative alignment, test grilling, and [Specific], [Intermediate], [Global] test categorization before writing code.
---

# Human-guided TDD

Collaborative, intentional testing workflow that contrasts with autopilot mode. Use this when the user wants to be deeply involved in deciding what and how to test.

## Core principles

1. **Intentionality over volume.** Do not write tests just to write tests. Every test must have a clear purpose and test something that actually matters.
2. **Model actual usage.** Tests should reflect how a user or system actually interacts with the feature, not internal implementation details.
3. **Simplicity.** Tests must be easily understandable. Their intentions should be obvious just from looking at the code. Avoid convoluted setups or assertions.
4. **Speak up on difficult tests.** If a behavior can only be tested with brittle mocks or excessive setup, stop and tell the user. Propose a manual check in `verification-evidence` instead of a fragile test.

## Workflow

### 1. Grilling and alignment
Before writing any test code for a task:
- Agree on what the core value of the feature is and what really needs to be verified.
- Invoke the `grilling` skill if testing assumptions or boundaries need stress-testing.
- Focus on dynamic behavior (e.g. data queries returning in expected timeframes, error recovery) rather than static details (e.g. exact UI text strings).

### 2. Categorize the tests
When proposing tests in the plan or task brief, tag each test idea:
- `[Specific]`: Localized component tests and focused edge cases that run when working on that specific module.
- `[Intermediate]`: Subsystem or domain-level tests that run when working within a broader area of the codebase.
- `[Global]`: Critical regression tests that must run every time the suite runs (core business invariants, vital user flows).

Ensure test files, directory structure, or test tags reflect these categories so the fast suite and full suite can run them accordingly.

### 3. Red-green execution with integrity
- Follow `tdd-integrity`: write the red test first, commit as `test(red): <task-id> <AC-ids>`, and verify it fails on behavior rather than syntax or imports.
- Write the minimal code to pass the test, commit as `feat(green): <task-id> <AC-ids>`.
- Verify the test diff between red and green is strictly empty (`git diff --stat <red>..<green> -- <tests> == 0`).
- Review the test code with the user to verify it remains clear, straightforward, and faithful to actual usage.
