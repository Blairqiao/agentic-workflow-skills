---
name: independent-review
description: >-
  Review a finished task in a fresh context: check each acceptance criterion with file and line evidence, audit for test gaming, run a security pass on boundary paths and new dependencies, and return a pass or fail verdict without a numeric score. Use after every implementation task in the workflow, or whenever the user wants an independent check of agent-written changes.
---

# Independent review

A reviewer who has seen the implementer's reasoning tends to inherit its blind spots. Review from the artifacts only.

## Setup

- Use a fresh context. If your harness lets you choose the model, a different model family from the implementer's adds independence on high-risk tasks.
- Inputs: the task's diff from task start to green, the full text of its acceptance criteria, the task slice, and the test results the orchestrator recorded. Not the implementer's conversation or notes.
- Rerun the fast checks yourself if anything looks off.

## Spec compliance

For each criterion the task claims, decide pass or fail. A pass needs the file and line where the behavior lives and the test that proves it. A criterion with no proving test fails, unless the plan says it is verified manually.

## Gaming audit

Look for:
- code that detects it is under test, through environment variables, test framework globals or similar signals;
- branches that special-case inputs or values that appear only in tests or fixtures;
- hardcoded expected outputs;
- caught and hidden assertion errors, or broad exception swallowing around tested code;
- weakened, skipped, focused or deleted tests, and changed fixtures, snapshots or runner config;
- mocks of the very unit under test.

## Security pass

Run it when the diff touches a boundary path from the profile, adds a dependency, or handles user input, authentication or stored data. Check authorization, input validation and injection, secrets handling and error leakage. For migrations, check reversibility, locking and data loss. For each new dependency, confirm it is the intended, established package and not a lookalike name, and flag it for the user's approval.

## Verdict

Write it with `assets/verdict-template.md`. Separate blocking issues from polish. Polish never fails a review; it goes to the taskboard. Give no numeric score, because scale points drift between reviewers and invite rounding up.

## Rounds

At most 3 rounds per task. After the third failure, the orchestrator marks the task blocked and asks the user. If the implementer disputes a finding with a reason, the user decides.
