# Independent review brief

This brief is the complete reviewer contract. Supply the fields below to a fresh reviewer without the implementation conversation. Applicable repository guidance and relevant source and evidence remain available; the reviewer need not load the track, core, review procedure, taskboard template, proof template, or review record template to learn the checklist. Exclude the implementer's conversation history and internal reasoning.

## Candidate and requirements

- Exact plan path and revision, execution slug, selected executor, and evidence ownership:
- Workspace, candidate branch, and base revision:
- Candidate diff command or patch: `git diff <base-revision>` covering all candidate code, tests, configuration, and documentation. Include untracked candidate files separately because Git diff omits them. Identify the reviewed candidate state so later edits can be distinguished.
- Acceptance criteria: numbered observable requirements from the approved plan, fast-track record, or one-shot run document.
- Settled design decisions: approved architecture, non-goals, and authorized dependency or boundary changes.
- Domain dictionary: relevant canonical terms from `<main-repo>/.agent-docs/CONTEXT.md` when present, or state that no dictionary exists.

## Recorded verification evidence

- Red and green test outputs: Exact commands and verbatim failure and pass evidence with stable log paths and relevant excerpts.
- Test amendments: every test revision after red and every existing test expectation changed, with its reason, or explicitly state none.
- Suite and UI evidence: observed test runner, build, static check, and applicable browser verification outputs. State omitted checks and their reasons.

Keep lengthy evidence once in the existing proof or logs and provide direct references. Preserve full failure evidence; concise excerpts must not conceal failures.

## Review checklist

1. Check every acceptance criterion against the complete candidate diff and observed verification. Review interfaces and failure handling across affected integration boundaries. Verify domain terminology and affected documentation against source evidence; confirm requirements were not rewritten to hide defects. Report unrelated documentation gaps separately.
2. Audit all test changes against criteria and recorded red/green evidence. Look for weakened assertions, skipped cases, missing edge cases, fixture-specific production branches, and inappropriate mocks. Explicitly accept or reject every test amendment with reasons, including changes to existing expectations.
3. Review security where input handling, authentication, authorization, stored data, dependencies, or external boundaries change. Verify existing dependency authorization. Check migrations for data loss, locking, and rollback safety.
4. Reproduce commands when evidence is incomplete, suspect, or needed to confirm a finding. Missing red evidence cannot be reconstructed after implementation; a later passing run does not replace test-first proof. Identify the gap and request useful targeted checks. Mark review incomplete when required evidence or candidate scope cannot be verified. Do not invent evidence or claim an unobserved check passed.
5. Return the verdict below. Separate blocking defects from optional polish with exact file locations, consequences, and evidence. Resolve disputes through requirements and observed results.

## Required verdict

- Method and independence: independent subagent, independent session, observable native review, or disclosed self-review. Identify any loss of independence and covered scope. A native boost success label alone is insufficient.
- Candidate identity and base revision: identify exactly what was reviewed.
- Verdict: pass, blocking findings, or incomplete. A pass requires verified criteria, no unresolved blockers, and explicit disposition of every amendment.
- Criterion-by-criterion results: implementation locations and verification evidence for each requirement.
- Blocking findings and resolutions: exact file locations, consequences, and verification needed or observed for each fix.
- Amendment dispositions: accept or reject each logged amendment with its reason; state none when applicable.
- Security and test integrity findings: relevant checks and observed issues.
- Missing evidence and limitations: absent checks, unavailable evidence, and incomplete scope.
- Optional polish: omit when empty.

Return this record to the orchestrator for inclusion in the existing track record. No separate review file or numeric score is required.
