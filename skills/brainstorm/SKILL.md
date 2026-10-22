---
name: brainstorm
description: Explore unclear ideas, requirements, and design alternatives through conversation, and write a complete plan for execution. Use when the user wants to brainstorm or work out what to build; clear implementation requests do not require an interview.
---

# Brainstorm

Help the user describe the problem, explore possible directions, and settle the design for a complete plan. Planning never edits implementation code or tests. Follow the [shared decision rules](../_workflow/design.md#shared-decision-rules), which apply before or during a track. Exploration alone does not select a track or authorize implementation.

## Ground the conversation

Read relevant code, documentation, and the domain dictionary before asking how the project currently works. Follow [discovery](../_workflow/discovery.md) for targeted fact checks. Read the feature's active brief or track document when one exists; a handed-off brief points to the authoritative track document. Check facts affected by repository changes and reuse settled decisions.

Establish the intended user, concrete problem, and desired outcome. Ask about a real situation when the purpose is unclear. Keep questions focused on consequential choices the user needs to make, rather than facts you can inspect or routine details the builder can decide.

## Explore and converge

Ask one focused steering question at a time by default. Once the purpose is clear, sketch two or three concrete directions when meaningful alternatives exist, explain tradeoffs, and recommend one. Do not invent options for a settled choice. Summarize the emerging design for correction as understanding develops, distinguishing user decisions from your recommendations and assumptions.

Use [domain-modeling](../domain-modeling/SKILL.md) when a concept is introduced, overloaded, or contested. Resolve meanings needed by the chosen direction before making dependent choices; independent branches can continue. Record settled definitions in the domain dictionary immediately. Keep uncertainties about deferred alternatives, out-of-scope areas, or paused branches in the brief.

Use [grilling](../grilling/SKILL.md) for a consequential decision needing deeper scrutiny or when the user requests stress-testing. Pass the named decision, its scope, settled prerequisites, and remaining uncertainty. Let grilling use its numbered frontier rounds, then resume this conversation with the resolved outcome. Do not require grilling for every brainstorm or repeat its questions.

Stop exploring when the intended outcome, chosen direction, constraints, and consequential domain meanings are clear enough for planning. State remaining delegated details and deferred questions explicitly. A paused session may retain unresolved active questions; it must identify which dependent choices cannot yet proceed. Completion of exploration does not imply permission to implement.

## Save and resume

Tentative ideas can remain in chat while exploring. Save the completed plan directly in `<main-repo>/.agent-docs/plans/<feature>.md` using [the plan template](../_workflow/templates/plan.md) and [planning](../_workflow/planning.md). Include scope, exclusions, acceptance criteria, expected files, checks, workspace, starting revision, protected edits, executor, permissions, and unresolved blockers. A blocked plan cannot be ready. Present the plan summary inline, provide the exact execution instruction, and place a direct clickable link to the plan file at the very bottom of the chat response.

Save paused or abandoned exploration to `<main-repo>/.agent-docs/briefs/<feature>.md` using [the brief template](../_workflow/templates/brief.md). Update that record in place. When its decisions become a complete plan, incorporate them once and mark the brief handed off with a link to the authoritative plan. Follow that link on resume. During an active track, update its authoritative record rather than creating another brief.

Before writing any artifact, identify the parent repository and follow [workspace preparation](../_workflow/workspace.md). Apply [execution identity rules](../_workflow/core.md#operation-routing-and-records) so concurrent plans and evidence cannot overwrite each other. An explicit chat-only request overrides persistence and keeps decisions and definitions inline. If no destination is known or writing is blocked, retain the summary inline and report incomplete persistence.

Saved briefs are local ignored workflow records. Do not claim they are shared across machines or available to another checkout without checking. Follow [core artifact guidance](../_workflow/core.md#operation-routing-and-records) for updates and archival.

## Track boundaries

Normal tracks use separate planning and implementation sessions. A ready plan alone is not authorization. The user's explicit instruction to execute that named plan authorizes execution within its scope, without repeating the initial plan approval. Every follow-up repair in interactive tracks requires new inline mini-spec approval before code or test edits under [core](../_workflow/core.md). Grilling confirms understanding without an extra gate. Material scope changes return to the planning phase. A request to plan authorizes plan preparation only.

In an explicitly selected `one-shot` run, use the shared decision rules autonomously, record alternatives and material assumptions in the run document, and continue the authorized work without interactive brainstorming, grilling, or feedback gates.

Completion: the ready plan or paused brief is saved, its status and next step are clear, and any explicit chat-only exception or blocked persistence is disclosed.
