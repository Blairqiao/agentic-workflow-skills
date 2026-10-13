# Audit and maintain project documentation

Inputs: repository, current source state, existing documentation or its absence, requested audit scope.

## Establish scope and coverage

Identify the main repository with [workspace preparation](workspace.md). Record the checkout being audited, base revision, relevant uncommitted changes, and any user-specified scope. Inspect the candidate files, not just HEAD when changes are present. Preserve pre-existing work.

Locate existing documentation and enumerate maintained source, tests, scripts, configuration, schemas, manifests, and authored assets. Use Git's tracked and relevant untracked inventory and file searches such as `rg --files`; reconcile ignored directories with repository guidance so first-party modules are not omitted just because a search skipped them. Inspect committed configuration templates without reading local secret values.

A request to audit the entire codebase includes every maintained subsystem. Build a coverage inventory with paths, responsibilities, documentation counterparts, and statuses: reviewed, partial, unreviewed, or excluded. Assign every in-scope authored file to a subsystem and inspect it; record concrete exclusion reasons for dependencies, generated output, binary assets, Git metadata, and unrelated worktrees. Inspect maintained inputs to generated outputs. Do not infer complete coverage from a directory listing or representative sample. Large repositories can be audited in batches; preserve the inventory and report incomplete coverage until the remaining batches are examined.

Follow workspace ignore rules before creating the audit record at `<main-repo>/.agent-docs/research/<run-id>.md`. The record stays in the parent repository even when the candidate is in a worktree. New project guides belong in the audited checkout's `docs/`, so they travel with its candidate changes. Reuse existing README or documentation locations instead of relocating or duplicating them.

## Cross-check and document

For each subsystem, read its implementation, interfaces, relevant tests, configuration, and documentation. Trace entry points and important flows across subsystem boundaries. Verify claims about responsibilities, data, setup, commands, integrations, and behavior against the appropriate evidence. Tests show expectations; their existence alone does not prove they pass.

Classify findings before editing:

| Finding | Action |
| --- | --- |
| Missing documentation | Write the explanation supported by inspected source and available checks. |
| Outdated factual description | Update it and link the evidence that supports the correction. |
| Code conflicts with requirements, canonical domain terms, or documented intent | Record the discrepancy and possible implementation defect. Preserve the intended requirement and label current behavior separately. |
| Missing evidence, rationale, or access | Record the unknown and verification limit; do not invent an answer. |

Keep application code unchanged. Route unresolved terminology through [domain-modeling](../domain-modeling/SKILL.md) under the active track's decision policy. Populate its dictionary only with settled domain definitions; implementation mechanics belong in project guides. Do not invent historical architecture decisions from current code.

When creating documentation, write a useful index and only the guides the project needs, such as architecture, development setup, and subsystem or flow explanations. Keep the README as an entry point where appropriate. Preserve valid existing content, comments, and examples. Link source using paths and symbols that remain usable after integration; avoid temporary worktree paths in versioned guides. Keep audit evidence in the run record rather than making versioned guides depend on ignored audit records.

## Verify and hand off

Validate links and examples. Run relevant documented setup, test, build, or interface checks when feasible and safe in the available environment; reuse valid evidence from the same source state. Inspect a command's scripts before executing it, and follow existing authorization for dependencies and external or destructive effects. Record exact commands, results, and checks that could not run. Do not claim runtime verification from static reading alone.

Finish the audit record with the source identity, scope and coverage inventory, exclusions, findings and their evidence, documents created or updated, command results, unresolved contradictions, and remaining work. Distinguish a completed review of maintained source from unverified runtime behavior. Documentation may be useful even when unavailable services prevent some checks; report that limitation.

Present the updated documentation, material findings, coverage status, and record link. Follow the active development track's review and [handoff](handoff.md) requirements when invoked within a run. Standalone research leaves changes reviewable and uncommitted; do not start a development track, fix reported code defects, or publish documentation implicitly.

Completion: every in-scope subsystem has been examined, supported documentation updates are written, and links and applicable checks are verified or their limits recorded. Unreviewed source prevents a complete-audit claim. Unresolved intent conflicts remain visible rather than being rewritten to match the implementation.
