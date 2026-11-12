# Agent guidelines

## Skills

| Skill | Use when |
| --- | --- |
| [brainstorm](/skills/brainstorm/SKILL.md) | The idea or approach is unclear, or the user wants options or wants to be grilled |
| [planning](/skills/planning/SKILL.md) | Multi-step work needs a plan before building |
| [orchestrate](/skills/orchestrate/SKILL.md) | The user wants a plan built by cheap implementer models |
| [final-review](/skills/final-review/SKILL.md) | The coordinator gates a phase, or the user asks for a final review |
| [walkthrough](/skills/walkthrough/SKILL.md) | The user wants a project or change explained |
| [visual-proof](/skills/visual-proof/SKILL.md) | A UI changed, or the user wants screenshots as proof |
| [research](/skills/research/SKILL.md) | Docs need auditing against the code, or need writing |
| [learn](/skills/learn/SKILL.md) | The user wants to learn from past chat logs, or cut work they keep repeating |
| [unslop](/skills/unslop/SKILL.md) | Authored repo artifacts: plans, specs, docs, proofs, PRs, and comments |
| [caveman](/skills/caveman/SKILL.md) | Chat conversation: terse, token-saving responses without conversational fluff |

Typical flow: `brainstorm` (optional), then `planning` (Opus or Astra), then one `orchestrate` session on the index. That session is the coordinator (Flash). It runs every slice with a Sol orchestrator that dispatches Flash or Terra, and it calls `final-review` (Opus or Astra) after each phase itself. Run `visual-proof` during orchestration if the UI changed. Small, clear fixes skip all of it. Make the change directly, run the relevant tests, commit, and report.

When you start using a skill, say so in one line: `> **Skill:** <name>. <reason>`

## Rules

- Commit finished work by default: one commit per logical change, staging only the files you changed, by name. If a file you changed also has the user's uncommitted edits, leave it unstaged and say so. Never push or deploy; a hook blocks `git push`, and the user pushes.
- Ask before adding dependencies, running migrations, or anything destructive.
- Don't overwrite uncommitted user changes.
- Workflow files go in `.agent-docs/`, listed in `.git/info/exclude` and not in `.gitignore`.
- In `.agent-docs/`, `docs/`, and this file, use repository-rooted links (`/skills/...`), never absolute machine paths. In chat, the reverse applies: link files with absolute paths so they're clickable.
- Report honestly. Say what you didn't run or couldn't verify.
