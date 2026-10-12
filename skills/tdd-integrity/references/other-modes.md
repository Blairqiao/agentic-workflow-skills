# Other verification modes

## characterization-first

1. Write tests that pass against the current code and pin its present behavior. Commit them as `test(characterize): <task-id>`.
2. Change the code. Characterization tests change only through an approved amendment, because their job is to catch behavior changes nobody asked for.

## property-based

- Write the properties in red. They should fail against the stub or the current code.
- Fix the random seed and the number of generated cases in the test or its config so runs are reproducible, and record both in the taskboard.

## snapshot

- New or updated snapshots go in their own commit, never in the commit that changes the code producing them.
- Show the user the snapshot diff, or a rendered before and after, and wait for approval.

## plan-diff

- Run the tool's plan, dry-run or diff command from the workspace against non-production targets only.
- Attach the output to the evidence. The user approves the plan output. Never apply changes to shared environments.

## evidence-only

- There is no automated gate. Produce clear evidence of the change, such as screenshots, before and after notes and the commands used, and let the user verify it.
