---
name: brainstorm
description: Explore unclear ideas, requirements, and design alternatives through conversation, and save a design brief for later planning. Use when the user wants to brainstorm or work out what to build; clear implementation requests do not require an interview.
---

# Brainstorm

Help the user describe the problem, explore possible directions, and settle enough of the design for the next step. Follow the [shared decision rules](../_workflow/design.md#shared-decision-rules), which apply before or during a track. Exploration alone does not select a track or authorize implementation.

## Ground the conversation

Read relevant code, documentation, and the domain dictionary before asking how the project currently works. Follow [discovery](../_workflow/discovery.md) for targeted fact checks. Read the feature's active brief or track document when one exists; a handed-off brief points to the authoritative track document. Check facts affected by repository changes and reuse settled decisions.

Establish the intended user, concrete problem, and desired outcome. Ask about a real situation when the purpose is unclear. Keep questions focused on consequential choices the user needs to make, rather than facts you can inspect or routine details the builder can decide.

## Explore and converge

Ask one focused steering question at a time by default. Once the purpose is clear, sketch two or three concrete directions when meaningful alternatives exist, explain tradeoffs, and recommend one. Do not invent options for a settled choice. Summarize the emerging design for correction as understanding develops, distinguishing user decisions from your recommendations and assumptions.

Use [domain-modeling](../domain-modeling/SKILL.md) when a concept is introduced, overloaded, or contested. Resolve meanings needed by the chosen direction before making dependent choices; independent branches can continue. Record settled definitions in the domain dictionary immediately. Keep uncertainties about deferred alternatives, out-of-scope areas, or paused branches in the brief.

Use [grilling](../grilling/SKILL.md) for a consequential decision needing deeper scrutiny or when the user requests stress-testing. Pass the named decision, its scope, settled prerequisites, and remaining uncertainty. Let grilling use its numbered frontier rounds, then resume this conversation with the resolved outcome. Do not require grilling for every brainstorm or repeat its questions.

Stop exploring when the intended outcome, chosen direction, constraints, and consequential domain meanings are clear enough for planning. State remaining delegated details and deferred questions explicitly. A paused session may retain unresolved active questions; it must identify which dependent choices cannot yet proceed. Completion of exploration does not imply permission to implement.

## Save and resume

Tentative ideas can remain in chat while exploring. Always save a completed brief, even a short one, and checkpoint decisions and open questions when the user pauses. Present a concise version inline and link the saved record. An explicit chat-only request overrides persistence; do not write the brief or domain dictionary in that case, and include settled definitions in the chat summary instead.

Before writing any workflow artifact, identify the main repository and follow the ignore setup in [workspace preparation](../_workflow/workspace.md). This does not require creating a worktree or starting an execution track. If no repository or destination is known, ask where to save and keep the summary inline until resolved. If a write is blocked, report that persistence is incomplete and retain the summary inline.

- **Before a track exists.** Save to `<main-repo>/.agent-docs/briefs/<feature>.md` using [the brief template](../_workflow/templates/brief.md). Use a short, stable slug and update the same record in place. Use status `paused` for an interrupted exploration or `ready for planning` when consequential design questions are settled.
- **During a track.** Write directly into its active `plans/<feature>.md`, `fast-track/<feature>.md`, or `runs/<feature>.md` document. Preserve existing plan, progress, approval, and evidence sections. Do not create a competing brief.
- **On handoff.** When the user requests implementation planning or implementation, select or reuse the appropriate track, incorporate the brief into its active artifact, and mark the standalone brief `handed off` with a link to that document. The track document owns subsequent design updates. On resume, follow that link rather than treating the old brief as current.

Saved briefs are local ignored workflow records. Do not claim they are shared across machines or available to another checkout without checking. Follow [core artifact guidance](../_workflow/core.md#artifact-naming-in-place-updates-and-archival) for updates and archival.

## Track boundaries

Full and fast retain their existing implementation approval gates. Grilling confirms shared understanding; it adds no separate implementation approval. Reuse existing authorization within its scope. A request to plan authorizes preparation of the plan, not product implementation.

In an explicitly selected `one-shot` run, use the shared decision rules autonomously, record alternatives and material assumptions in the run document, and continue the authorized work without interactive brainstorming, grilling, or feedback gates.

Completion: the brief is saved or incorporated into the active track artifact, its status and next step are clear, and any explicit chat-only exception or blocked persistence is disclosed.
