# Portable agentic workflow skills

Six public skills start documented workflows or provide standalone tools. Internal procedures live in [skills/_workflow](skills/_workflow/README.md), which is installed alongside the skills but has no discoverable `SKILL.md`.

## Choose a track

| Track | Execution | Approval | Documentation |
| --- | --- | --- | --- |
| `full-track` | Prefer a worktree; delegate independent implementation when useful | One combined spec-and-plan approval | Detailed spec, plan, taskboard, proof, walkthrough |
| `fast-track` | Current workspace; one implementer, no implementation subagents | Same as full-track | Same as full-track |
| `one-shot` | Prefer a worktree; autonomous product and implementation decisions | No feedback gates; pause only for critical access or additional authorization | Run document with design decisions, plan, progress, proof, walkthrough |

Every track verifies the actual candidate and requires independent review when available. Fast-track retains a review subagent. Full-track and one-shot may use the current workspace for small tasks or explicit in-place requests. One-shot makes reasonable product choices itself, records the reasons, and reports an incomplete result honestly if technical alternatives are exhausted.

Worktrees belong in `<main-repo>/.worktrees/<run-id>`. Whenever creating or updating `.gitignore` (and before creating a worktree or writing workflow `docs/`), ensure both `.worktrees` (`.worktrees/*`, `.worktrees`) and `docs` (`docs/*`, `docs`) are added to the main repository's `.gitignore` and verify that Git ignores all files inside both directories. Use a harness tool only when it can honor that location; otherwise use Git directly. Do not create worktrees under Codex, Claude Code, Antigravity, or other harness directories. See [workspace preparation](skills/_workflow/workspace.md).

Behavior changes default to autopilot TDD (with human-guided TDD opt-in):
- **In isolated worktrees (`full-track`, `one-shot`):** Use `test(red)` and `feat(green)` commits and verify that the test diff between red and green is strictly empty (`git diff --stat <red>..<green> -- <tests> == 0`).
- **In the current workspace (`fast-track` or in-place runs):** Avoid intermediate commits so `HEAD` and pre-existing user changes stay untouched; verify red and green via terminal output and rely on independent review to audit the test diff.

Publishing and the final target-branch commit belong to the user.

## Standalone tools

- [grilling](skills/grilling/SKILL.md): stress-test thinking, architectural decisions, and tradeoffs in structured rounds (`❓ Q1 / ➡️`).
- [human-tdd](skills/human-tdd/SKILL.md): agree on meaningful tests (`[Specific]`, `[Intermediate]`, `[Global]`) before implementation.
- [unslop](skills/unslop/SKILL.md): cut AI tells, filler, and buzzwords from specs, plans, walkthroughs, and code.

## Install

```sh
./install.sh --project /path/to/repo
./install.sh --global
./install.sh --global --harness claude,codex,antigravity
```

The installer preserves existing destinations unless `--force` is supplied. That flag replaces matching installed entries, including `_workflow`; review local customizations first. Installation does not prune retired or unrelated skills.

| Harness | Project location | User location |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Antigravity | `.agents/skills/` | `~/.gemini/config/skills/` and `~/.gemini/antigravity-cli/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `.agents/skills/` | `~/.agents/skills/` |
| opencode | `.agents/skills/` | `~/.agents/skills/` |

These are the destinations supported by this installer. Project installations copy the bundle. With both Claude and shared harnesses selected, Claude's non-entry skills and documentation link to the shared project copies. Claude-only installations are self-contained.

Global installations link to this repository, except Claude's three entry skills, which are copied to add its manual-invocation metadata. Refresh those copies when the entry skills change. Use Git Bash or WSL on Windows, or copy the bundle manually with `_workflow` beside the six skill directories.

Some harnesses search several skill locations and may display duplicates. Select the required destinations with `--harness`; already installed entries in other locations remain until you remove them.

## Explicit entry points and adapters

Invoke the three tracks explicitly. Codex adapters set `allow_implicit_invocation: false`; Claude-specific installed copies add `disable-model-invocation: true`. Other harnesses follow the explicit-invocation descriptions where no adapter enforces them. Shared skill frontmatter contains only `name` and `description`.

[Harness adapters](skills/_workflow/adapters/) contain model and tool guidance for Codex, Antigravity, Claude Code, and generic runners. Actual capabilities come from the active session. Skills provide instructions, while the harness supplies sandbox and permission enforcement.

## Workflow artifacts

All workflow documentation belongs in the parent (main) repository at `<main-repo>/docs/`—never as isolated files inside a worktree. When working in `.worktrees/<run-id>`, either write directly to `<main-repo>/docs/` or symlink `<worktree>/docs` to `<main-repo>/docs` (`ln -s ../../docs <worktree>/docs`). Full-track and fast-track produce documentation at these default locations:

- `<main-repo>/docs/spec/<feature>.md`
- `<main-repo>/docs/plans/<feature>.md`
- `<main-repo>/docs/taskboard/<feature>.md`
- `<main-repo>/docs/proofs/<feature>-proof.md`
- `<main-repo>/docs/walkthroughs/<feature>-walkthrough.md`

One-shot uses `<main-repo>/docs/runs/<feature>.md`, including its material design decisions, proof, and walkthrough. Split it when readability warrants it. A reusable project profile is optional; inspect relevant repository configuration directly when no profile exists. Follow established artifact locations or repository storage requirements.

## Extending the suite

Add a skill when users need an independently invocable capability. Keep its trigger narrow and place reusable procedures behind relative links. [Procedure extraction](skills/_workflow/README.md) explains the inputs and completion boundaries. The installer automatically discovers directories with `SKILL.md` and carries shared documentation alongside them.

For a new manual-only entry point, add its native adapter metadata and update `ENTRY_SKILLS` in `install.sh` for Claude's generated copy. Internal procedure documents need neither frontmatter nor a public invocation name.

## Upgrading from the sixteen-skill bundle

The following former skills now live in `_workflow` documentation: `workflow-core`, `project-discovery`, `spec-alignment`, `implementation-planning`, `worktree-setup`, `tdd-integrity`, `task-dispatch`, `independent-review`, `verification-evidence`, and `integration-handoff`.

Inspect existing installations for these entries and preserve custom edits before explicitly removing or moving them out of skill search directories. Refresh the six public entries and `_workflow` together. The installer does not delete old entries because it cannot distinguish an earlier install from user-owned skills. Do not remove similarly named skills from other suites.

## Verification

```sh
python3 -m unittest discover -s tests -v
bash -n install.sh
```

Integration tests exercise fresh project installation for the supported targets, paths containing spaces, manual-only metadata, shared documentation availability, and preservation of existing destinations. Native harness execution needs separate validation in each product.
