# Audit and maintain project documentation

Inputs: repository, current source state, existing documentation or its absence, and requested audit scope.

## Establish scope and coverage

Identify the main repository and configure `<main-repo>/.git/info/exclude` using [workspace preparation](workspace.md). Record the checkout being audited, base revision, relevant uncommitted changes, and user-specified scope. Inspect candidate files in the working tree rather than `HEAD` alone when edits are present, preserving pre-existing user work.

Locate existing documentation and enumerate maintained source, tests, scripts, configuration, schemas, manifests, and authored assets. Use Git's tracked and untracked file lists alongside searches like `rg --files`, reconciling ignored directories with repository guidance so first-party modules are not skipped. Inspect committed configuration templates without reading local secret values.

An entire-codebase audit covers every maintained subsystem. Build a coverage inventory with paths, responsibilities, documentation counterparts, and statuses: reviewed, partial, unreviewed, or excluded. Assign every in-scope authored file to a subsystem and inspect it, recording concrete exclusion reasons for third-party dependencies, generated output, binary assets, Git metadata, and worktrees. Inspect maintained inputs to generated outputs. Do not claim complete coverage from a directory listing or sample. Large repositories may be audited in batches; preserve the inventory in the audit record and report incomplete coverage until all batches are examined.

Record the audit in `<main-repo>/.agent-docs/research/<feature-or-run-id>.md` using [the research audit template](templates/research-audit.md). Update ongoing working notes in place, or use a date-prefixed `<run-id>` snapshot when preserving an audit tied to a specific commit. New project guides belong in the audited checkout's `docs/` directory, while existing README and guide locations remain in place.

## Cross-check and document

Partition substantial code inspection by subsystem under the research skill's [depth and delegation policy](../research/SKILL.md#depth-and-delegation). Each assignment covers implementation, interfaces, relevant tests, and configuration, identifying inspected paths and remaining gaps against the coverage inventory. A summary alone does not establish complete coverage. The orchestrator reconciles findings with documentation and traces entry points and key flows across subsystem boundaries. Support claims about responsibilities, data, setup, commands, integrations, and behavior with source and command evidence. Tests express expectations, but their presence alone does not prove they pass.

Classify findings before editing:

| Finding | Action |
| --- | --- |
| Missing documentation | Write the guide or section supported by inspected source and available checks |
| Outdated factual description | Update the description and link the supporting source or command evidence |
| Code conflicts with requirements, canonical domain terms, or documented intent | Record the discrepancy and possible code defect; preserve the intended requirement and label current behavior separately |
| Missing evidence, rationale, or access | Record the unknown and verification limit without guessing |

Keep application code unchanged. Route unresolved terminology through [domain-modeling](../domain-modeling/SKILL.md) under the active track's decision policy. Populate `<main-repo>/.agent-docs/CONTEXT.md` only with settled domain definitions, keeping implementation mechanics in project guides. Do not invent historical architecture rationale from current code alone.

Write a clear documentation index and only the guides the project needs, such as architecture, development setup, and subsystem flows. Preserve valid existing content and examples. Link source files and symbols using repository-relative paths that remain valid after merge, avoiding temporary worktree paths in versioned guides. Apply [unslop](../unslop/SKILL.md) to all authored documentation and the audit record.

## Verify and hand off

Validate links and examples. Run relevant documented setup, test, build, or interface checks when safe in the current environment, reusing valid evidence from the same source state. Inspect scripts before executing them, and respect authorization boundaries for dependencies and external or destructive operations. Record exact commands, observed outputs, and checks that could not run. Never claim runtime verification from static reading alone.

Complete `<main-repo>/.agent-docs/research/<feature-or-run-id>.md` with the source identity, scope and coverage inventory, exclusions, classified findings, documents created or updated, command results, unresolved contradictions, and remaining work.

Present the updated documentation, material findings, coverage status, and audit record link. Follow the active development track's review and [handoff](handoff.md) rules when invoked inside a track. Standalone research leaves documentation changes uncommitted for user review; do not start a development track, fix reported code defects, or publish documentation implicitly.

Completion: every in-scope subsystem has been examined, supported documentation updates are written, and links and applicable checks are verified or their limits recorded. Unreviewed source prevents a complete-audit claim, and unresolved intent conflicts remain visible.
