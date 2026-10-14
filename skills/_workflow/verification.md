# Verification and evidence

Inputs: reviewed candidate, relevant commands, acceptance criteria, and latest workspace and target state.

1. **Identify the candidate.** Record the base revision and candidate state under test. In a shared checkout, distinguish pre-existing user edits from the candidate and disclose any verification dependence on them.
2. **Run verification checks.** Execute relevant tests, static checks, and builds. Use a fresh checkout or exported candidate when packaging, installation, contamination, or CI parity requires it. Verify the actual working tree edits rather than testing `HEAD` when candidate changes are uncommitted. Install locked dependencies only when needed.
3. **Verify UI behavior.** For changed UI behavior, exercise interactive flows and inspect applicable desktop and mobile viewports using available browser inspection tools, accessibility snapshots, and screenshots. A compiler or build pass alone does not verify UI behavior. Record unavailable checks and suitable alternatives. Embed all referenced screenshot proofs in Markdown documentation using image syntax, `![<Descriptive Caption>](<path-to-image.png>)`, rather than raw file paths or plain text links.
4. **Record combined proof and walkthrough.** Write the verification evidence and walkthrough in `<main-repo>/.agent-docs/` using a short, stable `<feature>` slug:
   - **Full-track.** Write `<main-repo>/.agent-docs/proofs/<feature>.md` using [the combined proof-and-walkthrough template](templates/proof.md). Include exact reproducible commands, observed red and green outputs or clearly marked excerpts, logged test amendments with reasons, UI evidence, what changed, design decisions, manual verification steps, documentation impact, and limitations.
   - **Fast-track.** Complete the proof, walkthrough, and documentation impact sections inside `<main-repo>/.agent-docs/fast-track/<feature>.md`.
   - **One-shot.** Complete the proof, walkthrough, and documentation impact sections inside `<main-repo>/.agent-docs/runs/<feature>.md`.

Update active proof documents in place so the summary reflects the current candidate, moving lengthy superseded output to `.agent-docs/archive/` when needed. Reuse valid evidence from the unchanged candidate rather than rerunning suites solely to format a document. Recheck affected behavior whenever implementation, tests, configuration, dependencies, or target branch integration changes after verification. Evidence-only documentation edits do not invalidate code checks; validate those edits for accuracy and working links.

Completion: the delivery candidate has reproducible verification evidence, embedded visual proof where applicable, and a complete walkthrough with explicit limitations and documentation impact.
