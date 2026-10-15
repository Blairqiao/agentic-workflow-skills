# Portable agentic workflow skills

Nine public skills run documented development tracks or provide standalone workflow tools. Shared phase procedures live in [skills/_workflow](skills/_workflow/README.md), which is installed alongside the skills by [install.sh](install.sh) and has no discoverable `SKILL.md`.

## Choose a track

| Track | Selection | Execution | Approval | Documentation |
| --- | --- | --- | --- | --- |
| `full-track` | User request or automatic model selection for multi-step work | Prefer a worktree; delegate independent tasks when useful | One combined spec-and-plan approval | `plans/<feature>.md`, `taskboard/<feature>.md`, and `proofs/<feature>.md` |
| `fast-track` | User request or automatic model selection for linear single-session work | Current workspace; single linear execution without implementation subagents | One mini-spec approval | Single `fast-track/<feature>.md` record |
| `one-shot` | Explicit user request only | Prefer a worktree; autonomous product and technical decisions | No feedback gates; pause only for critical access or authorization | Single `runs/<feature>.md` record |

Every track verifies the delivery candidate and requires [independent review](skills/_workflow/review.md) packaged with [the reviewer brief](skills/_workflow/templates/reviewer-brief.md). Fast-track retains an independent review subagent and escalates to `full-track` if scope outgrows linear single-session execution. Full-track and one-shot may use the current workspace for small tasks or explicit in-place requests. Failed task implementation attempts are capped at 3 and review-fix cycles are capped at 3 rounds. When an in-place run reaches a retry cap, the agent restores modified candidate files to their pre-task state while recording what was tried and what failed in `.agent-docs/`.

Worktrees belong in `<main-repo>/.worktrees/<feature>`, using a distinct `<run-id>` only when concurrent checkouts are needed. Before creating a worktree or writing files in `.agent-docs/`, add `.worktrees` and `.agent-docs` ignore rules to `<main-repo>/.git/info/exclude` without modifying `<main-repo>/.gitignore`, verify with `git check-ignore`, and add root-anchored `.worktrees` exclusions to glob-based project tool configs. Use a harness worktree tool only when it honors `<main-repo>/.worktrees/`; otherwise use Git directly. See [workspace preparation](skills/_workflow/workspace.md).

Behavior changes default to autopilot TDD, with human-guided TDD opt-in. Following [test integrity](skills/_workflow/testing.md), the agent runs the new or updated test first, records the verbatim red failure output before writing implementation code, implements the behavior without weakening assertions, records the verbatim green pass output, and logs any post-red test revisions under `Test amendments` for explicit reviewer acceptance. No intermediate `test(red)` or `feat(green)` Git commits or temporary-index tree snapshots are created. During in-place runs, the agent enforces a no-commits rule and stages candidate changes during [handoff](skills/_workflow/handoff.md), leaving publishing and the final target-branch commit to the user.

## Standalone tools

- [brainstorm](skills/brainstorm/SKILL.md): explore unclear ideas and design alternatives, save completed or paused briefs, and carry decisions into the chosen track.
- [domain-modeling](skills/domain-modeling/SKILL.md): build, challenge, and sharpen the project's shared domain dictionary in `<main-repo>/.agent-docs/CONTEXT.md`.
- [grilling](skills/grilling/SKILL.md): stress-test thinking, architectural decisions, and tradeoffs in structured rounds, bounded to the supplied decision scope when one is given.
- [human-tdd](skills/human-tdd/SKILL.md): agree on meaningful `[Specific]`, `[Intermediate]`, and `[Global]` tests before implementation.
- [unslop](skills/unslop/SKILL.md): cut AI tells, filler, buzzwords, em dashes, prose parentheses, and decorative emojis from authored prose across user-facing documentation and internal `.agent-docs/` artifacts while preserving verbatim code blocks and command output.
- [research](skills/research/SKILL.md): explain project documentation or audit the maintained codebase against it, creating missing guides and updating supported factual descriptions.

## Explore an idea before choosing a track

Use `brainstorm` to work out the intended outcome and compare directions. It checks relevant repository facts first, asks focused steering questions, uses domain-modeling for unclear concepts, and calls grilling when a scoped decision needs deeper scrutiny. Unresolved meanings block dependent choices while independent branches continue. Settled decisions carry forward without repeating the interview.

Every completed brainstorm and paused session is saved, including short ones, unless the user explicitly requests chat-only exploration. Before a track exists, the record lives in `.agent-docs/briefs/<feature>.md`. During a track, the design goes directly into its existing plan, fast-track record, or one-shot run document. When a standalone brief feeds a track, it is marked handed off and links to the authoritative track document. These ignored records persist locally; they are not automatically shared across machines.

Exploration alone does not start an execution track. When implementation planning or implementation is requested, the agent selects or reuses the appropriate track. Full and fast retain their approval gates; one-shot applies the shared design rules autonomously without an interactive interview. A sufficiently clear request can proceed directly to track design.

## Project research and documentation

Request `research explain` to walk through the project's purpose, architecture, key flows, and setup with links to documentation and source files. Request `research audit` to examine the maintained codebase, cross-check its documentation, and create or update project guides. Clear natural-language requests select the same modes, while ambiguous requests are clarified under the active track's decision policy.

Explain uses existing documentation and targeted source checks. When usable project documentation is absent, it discloses the need to bootstrap guides through Audit before explaining the project, while respecting explicit read-only constraints. Audit records subsystem coverage, exclusions, command evidence, and unresolved intent conflicts in `<main-repo>/.agent-docs/research/` using [the research audit template](skills/_workflow/templates/research-audit.md); it reports code defects without fixing them or rewriting requirements to match them.

Existing documentation stays in its established location. New project guides default to versioned `docs/` in the audited checkout, while the domain dictionary remains under domain-modeling. During development, update documentation affected by the change and record its impact in the walkthrough.

## Install and uninstall

```sh
./install.sh --project /path/to/repo
./install.sh --global
./install.sh --global --harness claude,codex,antigravity
./install.sh --uninstall --project /path/to/repo
./install.sh --uninstall --global
```

Use `install.sh` rather than single-skill fetchers such as `npx skills` or `gemini skills install`. The entry tracks read shared procedures in `_workflow` and invoke sibling tool skills, which single-directory fetchers do not bundle together.

The installer preserves existing destinations unless `--force` is supplied. Supplying `--force` replaces matching installed entries, including `_workflow`. Supplying `--uninstall` removes the installed workflow skills, `_workflow`, and retired entries from the earlier sixteen-skill bundle while leaving unrelated custom skills untouched.

| Harness | Project location | User location |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Antigravity | `.agents/skills/` | `~/.gemini/config/skills/` and `~/.gemini/antigravity-cli/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `.agents/skills/` | `~/.agents/skills/` |
| opencode | `.agents/skills/` | `~/.agents/skills/` |

Project installations copy the bundle into `.agents/skills/`. When both Claude and a shared harness are selected, Claude's skills and `_workflow` link to the shared project copies, except `one-shot`, which is copied to inject Claude's manual-invocation metadata. Claude-only installations are self-contained. Global installations link to this repository, with a copied `one-shot` entry for Claude.

## Invocation policy and adapters

Models may automatically select `full-track` or `fast-track` for requested implementation planning or implementation based on task scope, while `one-shot` requires explicit user invocation. `brainstorm` is discoverable for exploration without selecting a track. In Codex, `skills/one-shot/agents/openai.yaml` sets `allow_implicit_invocation: false`; in Claude Code, the installed `one-shot` copy adds `disable-model-invocation: true`. Shared skill frontmatter contains only `name` and `description`.

[Harness adapters](skills/_workflow/adapters/) map subagent roles to universal capability tiers across Codex, Antigravity, Claude Code, and generic runners: lightweight scanning for discovery, standard coding for scoped implementation, and high-reasoning for independent review and escalated fixes.

[Code exploration](skills/_workflow/discovery.md#code-exploration-and-delegation) defaults broad code reading to scoped read-only subagents in every track, including fast-track. The orchestrator may read documentation and make purposeful small code reads directly. It chooses supported models and reasoning settings by capability: lightweight retrieval, standard investigation, or demanding reasoning. Reports retain evidence, exceptions, uncertainties, and search coverage; findings require verification only when they support critical decisions. Focused follow-up and capability escalation preserve evidence quality while stronger-model usage remains a soft target. The shared procedure defines fallbacks when delegation is unavailable. The policy is adopted without a benchmark prerequisite; context and usage savings have not been measured.

## Workflow artifacts and archival

All workflow documentation belongs in the parent repository at `<main-repo>/.agent-docs/`, never inside a worktree. Keep `<feature>` slugs short and stable in `kebab-case`, and edit active records in place so main sections reflect the current approach while moving lengthy superseded history into `<main-repo>/.agent-docs/archive/`:

- `<main-repo>/.agent-docs/CONTEXT.md` and `<main-repo>/.agent-docs/CONTEXT-MAP.md` for the shared domain dictionary.
- `<main-repo>/.agent-docs/briefs/<feature>.md` for completed or paused exploration before a track starts, using [the brief template](skills/_workflow/templates/brief.md).
- `<main-repo>/.agent-docs/plans/<feature>.md` for the combined `full-track` specification and implementation plan.
- `<main-repo>/.agent-docs/taskboard/<feature>.md` for `full-track` task orchestration and review status.
- `<main-repo>/.agent-docs/proofs/<feature>.md` for the combined `full-track` verification proof and walkthrough.
- `<main-repo>/.agent-docs/fast-track/<feature>.md` for the single-file `fast-track` record.
- `<main-repo>/.agent-docs/runs/<feature>.md` for the single-file `one-shot` record.
- `<main-repo>/.agent-docs/research/<feature-or-run-id>.md` for `research audit` coverage and evidence.
- `<main-repo>/.agent-docs/archive/` for archived plans, detailed completed taskboards, and abandoned attempt details.

Start each session by reading the feature's active brief before a track exists, or its active plan and unfinished tasks during a track. Follow handed-off briefs to their authoritative document, consulting `.agent-docs/archive/` only when historical context is directly needed.

## Extending the suite

Add a skill when users need an independently invocable capability. Keep its trigger narrow and place reusable phase instructions in `_workflow` behind relative links. [Shared workflow procedures](skills/_workflow/README.md) explains the inputs and completion boundaries. For a new manual-only entry point, add its adapter metadata and append its name to `ENTRY_SKILLS` in `install.sh`.

## Upgrading from the sixteen-skill bundle

The following former skills now live in `_workflow` procedures: `workflow-core`, `project-discovery`, `spec-alignment`, `implementation-planning`, `worktree-setup`, `tdd-integrity`, `task-dispatch`, `independent-review`, `verification-evidence`, and `integration-handoff`. Run `./install.sh --uninstall` followed by a fresh install, or pass `--force` to refresh the nine public skills and `_workflow`.

## Verification

```sh
python3 -m unittest discover -s tests -v
bash -n install.sh
```

Integration tests verify fresh project installation across supported targets, paths containing spaces, manual-invocation metadata on `one-shot`, automatic invocation availability on `full-track` and `fast-track`, `--uninstall` cleanup, template and link integrity, and preservation of existing destinations.
