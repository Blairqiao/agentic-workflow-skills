# Agent Guidelines: Agentic Workflow Skills

> These rules enforce rigorous behavior, planning, verification, and multi-harness portability across this repository.

## Core Behaviors

1. **Evidence Over Assertions:** Never claim a bug is fixed or a feature works without running the relevant test or command and observing the output. Provide the terminal proof.
2. **Design First:** Do not write implementation code for complex features without a plan. Read `CONTEXT.md`, and if architectural decisions are needed, trigger a `/grill-me` session or use the `domain-modeling` skill. For small, well-understood changes (≤100 LOC, ≤3 files), use `fast-track`.
3. **No Phantom Edits:** Preserve all existing comments, docstrings, and unrelated logic when making edits. Only modify what is strictly in scope.
4. **Testing Modes & Integrity:** Before writing tests, explicitly ask the user if they want "Autopilot TDD" or "Human-Guided TDD" (unless in `one-shot`). Enforce `tdd-integrity`: separate `test(red)` and `feat(green)` commits; the test code diff between red and green must be strictly empty (`git diff --stat <red>..<green> -- <tests> == 0`).
5. **Clean Handoff & Git Safety:** Never commit directly to the target branch, deploy, or run `git push`. Stage candidate changes and present verification proof for the user to make the final commit.

## Multi-Harness Skill Authoring & Standards

1. **Open `SKILL.md` Format:** In all shared `SKILL.md` files under `skills/`, keep YAML frontmatter minimal: only `name` and `description`. Put harness-specific extensions (such as `agents/openai.yaml` or Claude Code settings) in their respective adapters.
2. **Subagent Model Tiering:** When dispatching subagents in Antigravity or multi-agent runners:
   - **Task Implementer:** `"flash"` (fast generation, low thinking overhead, strictly scoped to one task).
   - **Explorer / Scanner:** `"flash_lite"` (minimal reasoning, directory scans, symbol grepping).
   - **Task Reviewer & Auditor:** `"inherit"` or `"pro"` (high reasoning budget, adversarial spec compliance, anti-gaming checks).
   - **Fix Escalation:** Promoted to `"inherit"` / `"pro"` after round 2.
3. **Multimodal UI Verification:** For any web or UI tasks, do not rely solely on compiler or build passes (`tsc --noEmit`). Use `agent-browser` with accessibility snapshots (`agent-browser snapshot -i`) and annotated screenshots (`agent-browser screenshot --annotate`) to verify layout, mobile viewports (390x844), and interactive elements.
4. **Portable Commands:** Avoid hardcoding environment-specific paths or package managers. Read from `docs/agent-profile.md` (via `project-discovery`).

## Transparency & Honesty

1. **Admit Knowledge Gaps:** If you don't know how to do something, or if the documentation is missing, be honest. Do not hallucinate APIs or guess.
2. **Disclose Shortcuts & Debt:** If you take a shortcut to accomplish a goal, or if your solution introduces technical debt or performance risks, explicitly flag it.
3. **No Silent Assumptions:** If a requirement is vague, stop and ask. If you must proceed, explicitly state your assumptions first.
4. **No "Yes-Man" Behavior:** If a suggested approach is flawed, insecure, or violates our architecture, respectfully push back and explain why before implementing it.

## Guardrails & Safety

1. **No Placeholders:** Write complete code. Never leave `// TODO`, `/* implement here */`, or truncated snippets unless explicitly told we are prototyping.
2. **Dependency Discipline:** Do not install new dependencies or third-party packages without prior confirmation and justification.
3. **Destructive Action Safety:** Never run destructive git operations (`git reset --hard`, `git push --force`), drop databases, or delete directories without explicit user confirmation.
