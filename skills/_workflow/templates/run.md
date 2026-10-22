# One-shot run

Execution slug, executor, exact plan path, plan revision, persistent candidate checkout, branch, base revision, protected user edits, and evidence ownership:

Request, workspace, starting state, candidate identity, and status:

Explicit one-shot is autonomous and supports boost or non-boost execution without a separate planning phase or approval gates. Record the selected executor and do not silently switch. Native boost owns internal delegation; non-boost execution uses custom coordination where useful.

## Design and acceptance criteria

Record intended behavior, non-goals, and observable requirements.

## Design decisions

Update in place to reflect the active design. For each material choice, record the options considered, chosen behavior, reasons, assumptions, and tradeoffs. Summarize abandoned approaches briefly and move lengthy notes to `.agent-docs/archive/`.

## Plan and progress

Tasks, dependencies, attempt counts capped at 3 failed attempts per task, recorded red and green test evidence, outcomes, and blockers.

## Review

Method, round count capped at 3 review-fix rounds, findings, corrections, explicit acceptance or rejection of each test amendment, and whether review was independent.

## Proof

Reproducible verification commands, actual outputs, every logged test amendment with its reason, UI or manual evidence with embedded screenshots, candidate identity, and limitations. Follow [verification](../verification.md).

## Walkthrough

Resulting behavior, significant changes, manual verification steps with expected results, risks, and delivery location.

### Documentation impact

Link project guides created or updated and record unresolved documentation gaps or contradictions, or explain why no documentation changes were needed.

## Incomplete work

Include only when requirements remain unfulfilled. If an in-place run hit a retry cap, confirm that modified candidate files were restored to their pre-task state and explain the evidence and exhausted alternatives without asking for product feedback.
