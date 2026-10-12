# Verification and evidence

Inputs: reviewed candidate, relevant commands, acceptance criteria, latest workspace/target state.

1. Establish the exact candidate under test. Record a commit when available, or a base revision plus candidate diff/snapshot when changes are uncommitted. In a shared checkout distinguish pre-existing changes from the candidate and disclose any verification dependence on them.
2. Run relevant tests, checks, and builds. Use a fresh checkout or exported candidate when packaging, installation, contamination, or CI parity needs that check. Include uncommitted candidate files; do not verify HEAD and claim it proves edits outside HEAD. Install locked dependencies only when needed.
3. For changed UI behavior, exercise interactions and inspect applicable desktop/mobile layouts with accessibility snapshots and screenshots when tools support them. Choose viewports relevant to the product. A compiler pass alone does not verify UI behavior. Record unavailable checks and any suitable alternatives.
4. Write [proof](templates/proof.md) with exact commands, observed output or clearly marked excerpts, the candidate identity, coverage, and limitations. Keep commands reproducible. Reuse valid evidence from the same candidate rather than rerunning checks to produce a new document.
5. Write [the walkthrough](templates/walkthrough.md) with changes, design decisions, risks, and manual steps with expected results. Full/fast produce separate proof and walkthrough files. One-shot includes both sections in its run document.

Use configured artifact paths. Defaults for full/fast are `docs/spec/`, `docs/plans/`, `docs/taskboard/`, `docs/proofs/`, and `docs/walkthroughs/`. One-shot defaults to `docs/runs/<feature>.md`. Use external storage when artifacts are sensitive or repository guidance requires it; do not invent another preference gate.

Recheck affected behavior if implementation, tests, config, dependencies, or target integration changes after verification. Evidence-only edits do not recursively invalidate the code checks; validate those edits for accuracy and links.

Completion: the actual delivery candidate has sufficient reproducible evidence, with proof and walkthrough complete and limitations explicit.
