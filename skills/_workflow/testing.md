# Test integrity

Inputs: acceptance criteria, relevant test layout, existing baseline, and selected testing style.

1. **Write and run the red test.** For a behavior change, add or update a test that expresses the requirement, whether in a dedicated test file or an inline test module. Run the targeted test command and observe the expected behavioral failure before writing implementation code. Fix syntax, import, or setup errors before counting the failure as red. Temporary signature stubs are acceptable when needed to reach the behavioral assertion. Record the exact command and verbatim red failure excerpt in the taskboard, fast-track record, or proof.
2. **Implement green without weakening tests.** Write the implementation to satisfy the requirement and rerun the targeted test command. Record the verbatim green passing output. During green implementation, do not weaken assertions, delete test cases, skip tests, alter fixtures to match buggy output, lower coverage or performance thresholds, or mock the unit under test just to obtain a pass.
3. **Log test amendments explicitly.** If an existing expectation is legitimately wrong, or if a test written during red needs a signature or setup adjustment during green, record the change under `Test amendments` in the proof, fast-track record, or run document with its reason. Demonstrate that the revised test still catches the intended defect. In human-guided mode, agree on changed test intent with the user; autopilot resolves it within the approved design. One-shot never opens a test-feedback gate.
4. **Run regression checks and audit test diffs.** Run relevant regression suites and inspect all test, fixture, snapshot, helper, and runner changes in the candidate diff against the base revision. Check for tests that stopped running, hardcoded fixture return values, test-detection branches in production code, or swallowed exceptions. Inline unit tests and doctests count as test code.
5. **Independent reviewer verification.** For native boost, observable independent review can use the same evidence contract without requiring a second custom review pipeline. Pass the candidate diff, acceptance criteria, recorded red failure output, green pass output, and logged test amendments to the reviewer using [the reviewer brief](templates/reviewer-brief.md). Do not create intermediate test or feat Git commits or temporary-index tree snapshots; red-green integrity is enforced by recorded terminal evidence and adversarial review of the final test diff.

Use characterization tests to establish legacy behavior before changing it. Property tests should record enough seed or counterexample information to reproduce failures. Inspect updated snapshots as requirements evidence rather than accepting them mechanically.

For documentation, visual work, or configuration changes where unit tests do not apply, use rendering checks, browser inspection, static analysis, or non-production dry runs instead of contrived tests. Keep temporary test scaffolding out of delivered work.

If test results vary across runs, investigate with targeted reruns and record the instability; a passing rerun does not erase an unexplained failure.

Completion: intended behavior is verified by recorded red and green test evidence or a suitable non-code alternative, all test amendments are logged with reasons, and test changes preserve the requirements.

Boost requests source logs for red and green evidence and test amendments as explicit deliverables. Missing red evidence cannot be reconstructed after implementation. Report the gap and obtain a targeted check where useful; a later passing run does not replace the missing test-first proof.
