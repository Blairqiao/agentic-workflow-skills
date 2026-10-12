---
name: tdd-integrity
description: >-
  Run red-green test-driven development with integrity rules that stop tests from being weakened, skipped or gamed, in any language, whether tests live in separate files, beside the code or inside source files. Use for every implementation task in the workflow, and whenever one agent writes both the tests and the code for a change.
---

# TDD with integrity

When one agent writes both the test and the code, the quickest route to green is bending the test. These rules make that visible to you, the reviewer and the user.

## Know where tests live

Read the profile's test layout. Test code includes separate test files, files beside the code, test modules inside source files such as Rust's `#[cfg(test)]` modules, doctests, fixtures, snapshots, shared helpers and runner config. Everything below applies to all of it, including the test parts of a source file.

## Baseline

Start from the baseline recorded at workspace setup, or run the task's tests now. Keep the list of test IDs and results for later comparison.

## Red

1. Add new tests for the task's acceptance criteria. Name or tag them with the AC IDs where the framework allows it.
2. Leave existing tests, fixtures, helpers and runner config unchanged. Watch for additions that change other tests: a new module-level mock, a global setup hook, or a skip or focus marker in an existing file alters existing tests even though the diff only adds lines.
3. If the code under test doesn't exist yet and the plan allows stubs, add one with the planned signature and a placeholder body, so the test can reach its assertion.
4. Run the new tests. They must fail for the expected reason, usually an assertion about behavior. A syntax error, import error, missing module or setup crash is not a valid red; fix the test or add the allowed stub.
5. Run the rest of the suite. Every test that passed at baseline must still pass.
6. Commit only the red changes as `test(red): <task-id> <AC-ids>`.

## Green

1. Write the smallest code change that makes the new tests pass.
2. Don't change test code, fixtures, snapshots, runner or CI config, test scripts in manifests, or dependency lists. If you believe a test is wrong, stop and ask for a revision instead of editing it. Each task gets one revision; a second request means the task is blocked.
3. Run the task's tests and the fast suite, then commit as `feat(green): <task-id> <AC-ids>`.

## Checks before calling it done

Run these yourself and show the commands and outputs:
- **The test diff between red and green is empty.** For separate test files, `git diff --stat <red>..<green> -- <test paths>` prints nothing. For tests inside source files, read the hunks and confirm none fall inside test regions.
- **No test went missing.** Every baseline test ID still runs, and none is newly skipped.
- **Clean-state run.** Run the tests with no uncommitted or untracked changes, so leftovers can't affect results. A fresh temporary worktree of the green commit is best. At minimum, `git status` must be clean.
- **No gaming.** The code doesn't detect that it's under test, special-case inputs that appear in tests, hardcode expected outputs, catch and hide assertion errors, or lower thresholds.

## Flaky tests

If a baseline-passing test fails, rerun it once from a clean state. A pass on rerun gets recorded as flaky in the taskboard, never hidden. A second failure blocks the task with both outputs attached.

## Changing existing tests on purpose

When the spec changes behavior that existing tests pin down, those tests have to change. Do it in a separate commit, `test(amend): <task-id> <AC-ids>`, only after the user approves, and cite the criterion that requires it.

## Human-guided mode

When the plan says human-guided, agree on test design with the user before red, using the plan's `[Specific]`, `[Intermediate]` and `[Global]` tags. If a behavior can only be tested with brittle mocks, propose a manual check in the evidence instead.

## Other verification modes

If the task's mode isn't test-first, follow the matching section of `references/other-modes.md`.
