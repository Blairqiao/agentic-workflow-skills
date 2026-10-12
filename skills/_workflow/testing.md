# Test integrity

Inputs: acceptance criteria, relevant test layout, existing baseline, selected testing style.

1. For a behavior change, add or adapt a test that expresses the requirement. Run it and observe the expected behavioral failure. Fix syntax, import, or setup errors before calling the result red. Temporary signature stubs are acceptable when needed to reach the behavior assertion.
2. Implement the behavior and run the targeted tests. Preserve test intent during green: do not weaken assertions, skip tests, alter fixtures, lower thresholds, or mock the unit under test just to obtain a pass.
3. If an existing expectation is legitimately wrong or the approved behavior changed, revise the test with the reason recorded. Demonstrate that the revised test detects the intended defect. In human-guided mode, agree on changed intent with the user; autopilot resolves it within the approved design. One-shot never opens a test-feedback gate.
4. Run relevant regression checks and inspect test, fixture, snapshot, helper, and runner changes. Check for tests that stopped running, hardcoded fixture answers, test-detection branches, or hidden exceptions. Tests embedded in source files and doctests count as test code too.
5. Record actual commands and results, applying track-aware commit and diff rules:
   - **In an isolated worktree (`full-track`, `one-shot`):** Commit the failing test as `test(red): <task-id>` and the passing implementation as `feat(green): <task-id>`. Verify that the test diff between red and green is strictly empty (`git diff --stat <red>..<green> -- <test-paths>` prints nothing, or no hunks touch test regions for inline tests). Legitimate test revisions require an explicit `test(amend): <task-id>` commit with the reason recorded.
   - **In the current workspace (`fast-track` or in-place runs):** Do not make intermediate commits so `HEAD` and pre-existing user changes stay untouched. Verify red and green via terminal output and rely on independent review to audit the test diff against the acceptance criteria.

Use characterization tests to establish legacy behavior before changing it. Property tests should record enough seed/case information to reproduce failures. Inspect changed snapshots as requirements evidence rather than accepting them mechanically.

For documentation, visual work, or configuration, use relevant rendering, manual interaction, static checks, or non-production dry runs instead of contrived tests. Keep unfinished scaffolding out of delivered work.

If results vary, investigate with targeted reruns and record the instability; a passing rerun does not erase the failure. Escalate verification scope only when changes or unresolved concerns justify it.

Completion: intended behavior is verified by meaningful tests or suitable alternative evidence, and test changes preserve the requirements.
