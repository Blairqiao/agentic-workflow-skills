# Research audit record

Audited checkout, base revision, uncommitted candidate state, date, and requested audit scope:

## Subsystem coverage inventory

Assign every in-scope authored file to a maintained subsystem. Do not mark the audit complete while any in-scope subsystem remains partial or unreviewed.

| Subsystem | Paths | Responsibilities | Documentation counterpart | Status |
| --- | --- | --- | --- | --- |

## Exclusions

Record concrete exclusion reasons for third-party dependencies, generated outputs, binary assets, Git metadata, and worktrees.

| Excluded path or pattern | Reason | Maintained input inspected |
| --- | --- | --- |

## Classified findings and evidence

| Subsystem or location | Classification | Evidence and impact | Action taken |
| --- | --- | --- | --- |

## Documents created or updated

List versioned project guides created or updated in the checkout, and note whether `<main-repo>/.agent-docs/CONTEXT.md` was updated via domain-modeling.

## Verification commands and results

Record exact setup, build, test, link-check, or example verification commands run, their observed outputs, and any checks that could not run in the current environment.

## Unresolved contradictions and remaining work

List code defects, requirement mismatches preserved without silent rewrites, and any unreviewed batches remaining.
