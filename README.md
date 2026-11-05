# Agentic workflow skills

Nine small, self-contained skills for coding agents. Each skill is one `SKILL.md`, plus at most a template or two in the same folder. Nothing loads shared files from elsewhere.

| Skill | What it does |
| --- | --- |
| [brainstorm](skills/brainstorm/SKILL.md) | Asks focused questions, offers 2 or 3 approaches with tradeoffs, and lets you pick. Includes an optional "grill me" stress test. |
| [planning](skills/planning/SKILL.md) | Writes either one linear plan or parallel slices that each run in their own session. Tags every task with a builder model and a test decision. |
| [orchestrate](skills/orchestrate/SKILL.md) | Dispatches cheap implementers task by task, reviews each diff, escalates stuck tasks, and stages the result. |
| [final-review](skills/final-review/SKILL.md) | One review of the whole change against the plan, by a strong model. |
| [walkthrough](skills/walkthrough/SKILL.md) | Plain-language tour of a project or a change. |
| [visual-proof](skills/visual-proof/SKILL.md) | Screenshots of the running app, embedded in `.agent-docs/proofs/<feature>.md`. |
| [research](skills/research/SKILL.md) | Audits docs against code and writes or fixes them. |
| [unslop](skills/unslop/SKILL.md) | Strips AI writing tells from authored repo artifacts, plans, and docs. |
| [caveman](skills/caveman/SKILL.md) | Terse, token-saving conversational responses in chat. Strips fluff while preserving code and technical precision verbatim. |

## Workflow and roles

```text
brainstorm (optional) -> planning -> orchestrate (one session, or one per slice) -> final-review
```

| Role | Default model | Can swap in |
| --- | --- | --- |
| Planner | Opus | GPT-6.1 Astra |
| Orchestrator and per-task reviewer | GPT-6.1 Sol, medium or high | |
| Implementer | Gemini Flash or GPT-6.1 Terra, medium or high (set per task in the plan) | |
| Escalation debugger | Opus | GPT-6.1 Astra |
| Final reviewer | Opus | GPT-6.1 Astra |

The expensive models plan once and review once. Cheap models do the implementation, plus the review of each task. Escalation goes Flash, then Terra, then high effort, then Opus or Astra. Small fixes skip the whole flow.

**Parallel slices.** `planning` can split a feature into slices that never touch the same file. Each slice gets its own plan file and kickoff prompt, and runs in its own session and worktree. `final-review` checks how the slices fit together.

**Open question.** Planners trust exploration reports from cheap subagents that cite `file:line`, and re-check only the claims a decision depends on. Whether that trust holds up hasn't been benchmarked yet.

## Testing philosophy

Tests are planned per task, not imposed everywhere. `planning` gives each task either `Test: <behavior>`, for real logic and bug fixes, or `Test: none. Verify by <how>`, for UI, config, glue, and docs. Implementers write exactly what the plan says. This is not strict TDD, and it skips red/green logging.

## Install

```sh
./install.sh --global                         # ~/.claude/skills and ~/.agents/skills
./install.sh --global --dir ~/.cursor/skills  # add any other provider's skills folder
./install.sh --project /path/to/repo          # copy into the repo
./install.sh --global --hooks                 # skills plus the block-git-push hook
./install.sh --global --uninstall             # add --hooks to remove the hook too
```

Global installs are symlinks, so edits in this repository take effect immediately. Installing also removes entries left over from earlier versions of this pack (`_workflow`, `fast-track`, `full-track`, `one-shot`, `grilling`, `domain-modeling`, `human-tdd`).

`~/.claude/skills` covers Claude Code. `~/.agents/skills` covers Codex, Gemini CLI, and opencode. In T3 Code, each provider reads its own location, so one global install covers every provider. The skills name the subagent tool for each harness: `Agent` in Claude Code, `spawn_agent` in Codex, and `delegate_task` in T3 Code when a different provider is needed.

### Hooks

`--hooks` installs [hooks/block-git-push.sh](hooks/block-git-push.sh), which stops agents from running `git push` while still allowing commits. The installer links the script to `~/.agents/hooks/` and registers it in each harness it finds:

| Harness | Config file |
| --- | --- |
| Claude Code | `~/.claude/settings.json` |
| Codex | `~/.codex/hooks.json` |
| Antigravity | `~/.gemini/config/hooks.json` |

The installer edits these files with `jq`, which it requires. It keeps your other settings and saves a `.bak` copy of each file first. Running it again replaces the hook entry instead of adding a duplicate. Codex asks you to trust a new hook the first time it loads. The hook only applies to commands an agent runs, so you can still push from your own terminal.

## Check

```sh
./check.sh
```

It checks that each skill's `name` matches its folder and has a description, that relative links resolve, and that the installer and hooks parse.

## Credits

Ideas borrowed from [obra/superpowers](https://github.com/obra/superpowers) (brainstorming, subagent-driven development) and [mattpocock/skills](https://github.com/mattpocock/skills) (grill-me decision trees, vertical-slice planning).
