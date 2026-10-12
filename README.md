# Portable agentic workflow skills

A spec-to-commit development workflow, packaged as thirteen Agent Skills. They use the open `SKILL.md` format, so they load in Claude Code, Codex, Antigravity, Gemini CLI, opencode and other harnesses that read it.

The skills contain guidelines and checklists, not project-specific values. On first use, `project-discovery` records how your repository builds, tests and runs in `docs/agent-profile.md`, and every other skill reads from that file. To change how the workflow behaves in a repository, edit its profile rather than the skills.

## Skills

| Skill | What it does |
| --- | --- |
| `full-track` | Entry point: full workflow with spec and plan approval gates |
| `fast-track` | Entry point: small changes, no spec gates, same safety rules |
| `one-shot` | Entry point: autonomous run from one prompt, proof still mandatory |
| `workflow-core` | Phase map, guardrails, roles, state and resume rules |
| `project-discovery` | Profiles the codebase and calibrates its commands |
| `spec-alignment` | Focused questioning and numbered acceptance criteria |
| `implementation-planning` | Task slices, verification modes, TDD style |
| `worktree-setup` | Isolated workspace, env files, shared resources, sync, teardown |
| `tdd-integrity` | Red-green rules that stop tests being weakened or gamed |
| `task-dispatch` | Orchestration loop, taskboard, fresh contexts, limits |
| `independent-review` | Fresh-context verdicts with evidence, gaming and security checks |
| `verification-evidence` | Clean-checkout verification, proof and walkthrough |
| `integration-handoff` | Staged delivery, content check, user-owned commit, cleanup |

## Install

```sh
./install.sh --project /path/to/repo      # copy into the repo, commit to share
./install.sh --global                     # link into your user skill folders
./install.sh --global --harness claude,codex
```

Where each harness looks:

| Harness | Project level | User level |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Gemini CLI | `.agents/skills/` or `.gemini/skills/` | `~/.agents/skills/` or `~/.gemini/skills/` |
| opencode | `.agents/skills/`, `.opencode/skills/`, `.claude/skills/` | `~/.agents/skills/`, `~/.config/opencode/skills/`, `~/.claude/skills/` |
| Antigravity | `.agents/skills/` | `~/.gemini/config/skills/` for the IDE and 2.0, `~/.gemini/antigravity-cli/skills/` for the CLI |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |

A project install copies the skills into `.agents/skills/` and links `.claude/skills/` to those copies. A global install links to this folder, so updating this folder updates every harness. On Windows, run the script from Git Bash or WSL, or copy the folders under `skills/` by hand.

opencode reads both `.agents/skills/` and `.claude/skills/`, so with both installed it may list each skill twice. If it complains, rerun with `--harness` to leave one out.

## Keeping the entry skills manual-only

The three entry skills should start only when you ask for them. Harnesses handle that differently:

| Harness | How |
| --- | --- |
| Codex | Each entry skill ships `agents/openai.yaml` with `allow_implicit_invocation: false`. Invoke with `$full-track`. |
| Claude Code | The installer gives Claude Code its own copies of the entry skills with `disable-model-invocation: true`. Invoke with `/full-track`. |
| Gemini CLI | It asks for consent before activating any skill; decline one you didn't ask for. |
| Antigravity, opencode | The descriptions say to use them only on explicit request. Antigravity's CLI also exposes skills as slash commands. |

Shared copies keep only `name` and `description` in their frontmatter, the two fields every harness reads.

## What skills can and can't enforce

Skills are instructions; your harness provides enforcement. For the guardrails in `workflow-core` to hold even when a model slips:
- block `git push` and publishing commands with the harness's permission or policy rules;
- run the agent in the harness's sandbox, with network access limited where possible;
- keep production credentials out of the environment the agent runs in.

At the start of each run, `workflow-core` has the agent tell you which of these are active.

## Files a run creates

| Path | Written by |
| --- | --- |
| `docs/agent-profile.md` | `project-discovery` |
| `docs/spec/<feature>.md` | `spec-alignment` |
| `docs/plans/<feature>.md` | `implementation-planning` |
| `docs/taskboard/<feature>.md` | `task-dispatch` |
| `docs/proofs/<feature>-proof.md` | `verification-evidence` |
| `docs/walkthroughs/<feature>-walkthrough.md` | `verification-evidence` |

The profile can move any of these.

## Coming from v6

- Settings that lived in `.agent-verify.json`, such as commands, protected paths, boundaries and fast-track limits, now live in `docs/agent-profile.md`, discovered and confirmed per repository.
- The env allowlist and slot registry became the env and resource guidelines in `worktree-setup`.
- The JUnit and interval checks became the red and green rules in `tdd-integrity`, which work for any test layout.
- The supervisor scripts are gone. If you want hard enforcement on top of these skills, the kernel design in the v7 spec is the path for that.
