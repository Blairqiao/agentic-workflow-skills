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
4. **Speak up on difficult tests.** If a behavior can only be tested with brittle mocks or excessive setup, stop and tell the user. Propose a manual check in [verification](../_workflow/verification.md) instead of a fragile test.

## Workflow

### 1. Grilling and alignment
Before writing any test code for a task:
- Agree on what the core value of the feature is and what really needs to be verified.
- Invoke [grilling](../grilling/SKILL.md) if testing assumptions or boundaries need stress-testing.
- Focus on dynamic behavior (e.g. data queries returning in expected timeframes, error recovery) rather than static details (e.g. exact UI text strings).

### 2. Categorize the tests
When proposing tests in the plan or task brief, tag each test idea:
- `[Specific]`: Localized component tests and focused edge cases for that module.
- `[Intermediate]`: Subsystem or domain-level interaction tests.
- `[Global]`: Critical system-level invariants and core user flows.

### 3. Red-green execution with integrity
- Follow [test integrity](../_workflow/testing.md) for red, green, and test revisions:
  - **In an isolated worktree (`full-track`):** Commit the failing test as `test(red): <task-id>`, write the minimal implementation to pass, commit as `feat(green): <task-id>`, and verify the test diff between red and green is strictly empty via `git diff --stat <red>..<green> -- <test-paths>`.
  - **In the current workspace (`fast-track` or in-place runs):** Do not make intermediate commits so `HEAD` and pre-existing user changes stay untouched. Capture temporary-index `git write-tree` snapshots `S0` at task start, `S1` after red, and `S2` after green, and verify `git diff --stat "$S1" "$S2" -- <test-paths>` prints nothing.
- Review the test code with the user to verify it remains clear, straightforward, and faithful to actual usage.
