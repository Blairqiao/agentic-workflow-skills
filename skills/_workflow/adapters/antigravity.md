# Antigravity adapter

Use only tools and model identifiers exposed by the active runner. Do not invent a boost API or assume model controls exist.

## Native boost entry

For explicitly requested boosted plan execution, enter `/boost` in Antigravity and instruct the active session to execute the exact ready plan path. For boosted one-shot, enter `/boost` and explicitly invoke one-shot with the request. Record the executor and confirm the session is actually boosted through available runner evidence. Do not claim a skill activates a slash command. If boost is unavailable or inactive, stop that entry and offer full-track for non-boost execution; do not silently switch executors.

Boost owns its internal workstreams, workers, scheduling, and review rounds. Supply plan path, plan revision, execution slug, persistent candidate checkout, protected files, content sources, acceptance criteria, required checks, evidence locations, and completion format. Do not impose custom worker-per-task dispatch, model allocation, a mandatory taskboard, or duplicate review. Follow [execution](../execution.md), [observable independent review](../review.md), and [verification](../verification.md). A native review satisfies the requirement only when its independent role, scope, findings, and disposition are observable.

Follow [workspace preparation](../workspace.md). Native ephemeral worker locations are harness-managed; the final candidate belongs in the named repository-local persistent checkout. Verify actual containment and integration rather than asserting all native workers use repository-local worktrees. Keep workflow records directly at the main repository root. Live smoke validation remains required before claiming native behavior verified.

## Custom non-boost execution

Full-track mandates custom implementation delegation and does not require boost. Orchestration-track is automatically selected for large initiatives and mandates delegated vertical slices. Preserve the selected executor; optional boost requires explicit entry and observable session evidence. Non-boost one-shot delegates where coordination helps. Fast-track implements bounded defects directly and permits read-only investigation agents.

Select supported models through capability tiers:

- Lightweight scanning for bounded retrieval, file discovery, and symbols.
- Standard coding for scoped behavioral investigation and implementation.
- High reasoning for demanding investigations, architecture, independent review, and fix escalation after round two.

Use `invoke_subagent` for delegation, `view_file` for precise source reads, and `run_command` for terminal checks only when exposed by the active runner; inspect schemas before choosing arguments. Select research or implementation roles and capability tiers through supported controls rather than guessed APIs.

Use [discovery](../discovery.md#code-exploration-and-delegation) for focused read-only assignments. Give independent reviewers [the reviewer brief](../templates/reviewer-brief.md). Custom Antigravity coordinators use reactive wakeups on completion or background events rather than polling. Use available browser inspection tools for UI checks. Disclose unavailable delegation or model selection instead of guessing controls.

Use [common policy](../core.md) for supplied-context reuse, conditional phase loading, and authorization. Every interactive follow-up repair needs its own approved mini-spec before code or test edits. Explicit one-shot retains its autonomous exception with either executor.

The Antigravity installer discovers skill directories containing `SKILL.md` and places `_workflow` beside them in project `.agents/skills`, global `~/.gemini/config/skills` and `~/.gemini/antigravity-cli/skills` destinations. Models may automatically select orchestration-track, full-track, or fast-track by scope. One-shot requires explicit user invocation.
