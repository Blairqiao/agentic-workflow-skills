# Verification proof and change walkthrough

Execution slug, executor, exact plan path, plan revision, persistent candidate checkout, branch, base revision, protected user edits, and evidence ownership:

Candidate identity, base revision, date, and workspace state:

## Coverage

Map each acceptance criterion to the automated or manual check that verified it, and disclose any dependence on pre-existing user changes.

## Red and green test evidence

Record the targeted test commands, verbatim red failure excerpts observed before implementation, and verbatim green pass outputs observed after implementation.

## Verification commands and observed results

Record full suite, static check, and build commands in reproducible order with actual outputs or clearly marked excerpts. State the working directory and non-secret prerequisites.

## Test amendments

List every revision made to a test after observing red, or to an existing test expectation, along with its reason and reviewer sign-off, or state that none occurred.

## UI or manual evidence

Record interactive verification steps, expected results, desktop and mobile viewport checks, and embedded screenshots using `![<Descriptive Caption>](/.agent-docs/proofs/images/<execution-slug>-<image>.png)`.

## Walkthrough of what changed

Explain the resulting behavior and significant code changes by task or subsystem.

## Design decisions

Summarize key architectural choices and tradeoffs, or link the decision section in `<main-repo>/.agent-docs/plans/<feature>.md`.

## Documentation impact

Link project guides created or updated and record unresolved documentation gaps or contradictions, or explain why no documentation changes were needed.

## Limitations and remaining work

Record unrun checks, known baseline failures, unstable results, and any remaining risks.

## Delivery

Candidate location, staged paths or worktree merge command, and final commit or cleanup actions left to the user.

## Review and follow-up defects

Record independent review method, scope, findings, disposition, and test amendment sign-off. Observable native review may satisfy this section without a duplicate pipeline. Append fast-track defects, expected approved behavior, cause, correction, affected checks, review, and invalidated earlier evidence here. Missing evidence stays missing.
