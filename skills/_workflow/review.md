# Independent review

The orchestrator dispatches and resolves review. Keep the reviewer checklist in that contract, [the reviewer brief](templates/reviewer-brief.md), and populate it with candidate identity, approved criteria and decisions, relevant domain terms, diff access, red/green evidence, and every test amendment. Exclude implementation conversation history and internal reasoning.

## Dispatch

Native independent review can satisfy explicitly boosted plan execution and boosted one-shot when its independent role, reviewed candidate scope, findings, and disposition are observable. A boost success label alone is insufficient. Obtain targeted independent review for missing scope or mark review incomplete; do not automatically add a duplicate pipeline.

For non-boost execution, including fast-track, use a fresh review subagent covering the patch and affected integration boundary. Select a high-reasoning tier when supported. If subagents are unavailable, use an independent session supported by the harness. If neither exists, interactive tracks ask the user before substituting self-review; one-shot performs self-review and records the loss of independence.

Provide the populated reviewer contract, applicable repository guidance, and access to relevant source and evidence. Reviewers do not need the orchestrator's track, core, taskboard, proof, or review templates to learn their duties. Store long evidence once in existing proof or logs, with direct references and concise excerpts that preserve access to full failures.

## Resolution and recording

Resolve technical disputes through requirements and observed evidence. Record the candidate identity, independence, criterion results, findings and their disposition, missing evidence, and explicit acceptance or rejection of every test amendment in the existing taskboard, compact boost proof, parent proof for a follow-up, standalone fast-track record, or one-shot run document. The optional [review record template](templates/review.md) is a recording aid for the orchestrator. No separate review file or numeric score is required.

Re-review code changes addressing blocking findings, with the updated diff and verification; minor wording edits do not restart a full audit. Do not mark review complete while blockers, undecided amendments, or required missing evidence remain. Cap review-fix cycles at 3 rounds. At the cap, apply [core's failure policy](core.md): restore modified candidate files to their pre-task state for in-place runs while preserving prior user edits, retain isolated candidates for inspection, and record attempts and failures. Interactive tracks record a bounded blocker; one-shot reports an incomplete outcome. Any follow-up repair remains subject to the track's approval policy before code or test edits.
