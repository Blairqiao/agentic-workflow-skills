# Workspace preparation

Inputs: track, repository state, relevant configuration and service needs.

1. Inspect Git status, branch, existing worktrees, and user edits. Record the starting revision and pre-existing changes. Never stash, reset, or overwrite user work to make setup easier.
2. Fast-track uses the current workspace. Full/one-shot prefer a suitable existing repository-local worktree or create one using the placement rules below. A small task or explicit request can use the current checkout. If worktrees are unsuitable, use a local clone or copy and record the reason.
3. Base isolated work on the agreed target or current draft. If uncommitted work is part of the task, preserve it explicitly; a worktree created from HEAD does not include it automatically. Use unique paths and branch names following repository or harness conventions.
4. Install existing locked dependencies only when needed. Keep dependency directories separate; shared download caches are acceptable. If setup fails, diagnose rather than rewriting the lockfile reflexively.
5. Run relevant baseline checks when needed and record existing failures. Do not rerun a valid baseline merely because another procedure begins.

## Worktree placement, documentation location, and ignore rules

Use `<main-repo>/.worktrees/<run-id>`. Identify the main repository checkout from `git worktree list --porcelain`; when already in a linked worktree, its top-level directory is not the main repository root. Reuse an existing worktree only when its resolved path is inside that main repository's `.worktrees/` directory and it suits the task. Do not nest a new worktree under another linked worktree.

Before creating a worktree or writing workflow artifacts in `.agent-docs/`, ensure both `.worktrees` (`.worktrees/*`, `.worktrees`) and `.agent-docs` (`.agent-docs/*`, `.agent-docs`) are present in `<main-repo>/.gitignore` and `<main-repo>/.git/info/exclude`, preserving existing entries. Writing the patterns to `.git/info/exclude` ensures linked worktrees immediately inherit the ignore rules even before `.gitignore` is committed. Verify exclusion of both folders with `git check-ignore` from `<main-repo>`. Keep the `.gitignore` edit visible in the handoff without making a setup commit.

All workflow documentation (`spec/`, `plans/`, `taskboard/`, `proofs/`, `walkthroughs/`, `runs/`, `fast-track/`, `CONTEXT.md`, and `CONTEXT-MAP.md`) must reside in the parent repository at `<main-repo>/.agent-docs/`, never as isolated files inside `<main-repo>/.worktrees/<run-id>/`. Do not create a symlink to `.agent-docs` inside a worktree. Always read and write `<main-repo>/.agent-docs/...` directly by path so no stray symlink can be staged by `git add -A` and no documentation is lost when a worktree is cleaned up.

When creating a worktree in a repository whose linters, typecheckers, or test runners discover files by directory globs rather than Git, add a root-anchored `.worktrees` exclusion to the project's tool ignore configuration, such as `.worktrees/**` in `tsconfig.json` and ESLint, `<rootDir>/.worktrees/` in Jest, or `norecursedirs = [".worktrees"]` in `pytest`. Never use an unanchored `**/.worktrees/**` or substring `.worktrees` pattern that matches the worktree's own absolute path and silences checks run inside `<main-repo>/.worktrees/<run-id>`. Verify that tool discovery works from both `<main-repo>` and `<main-repo>/.worktrees/<run-id>`.

Use a native tool only if it accepts the required repository-local path. Otherwise use `git worktree add` with that explicit destination. Resolve symlinks before creation so the destination cannot escape the main repository. Never create worktrees in `.codex`, `.claude`, `.gemini`, or other harness-owned directories, even when that is a tool's default. If the permitted path is unavailable, resolve the access problem rather than silently switching to a harness directory.

## Conditional service setup

If the task starts an app or service, inventory the resources it uses. Create non-production config from committed templates or documented setup. If local credentials are needed, use an authorized mechanism that does not expose their values.

Allocate separate ports, service namespaces, and data paths when concurrent work or user resources could be affected. See [resource isolation](references/resource-isolation.md). Record allocations and cleanup commands. Check an allocation's identity before any migration, reset, or deletion; obtain required destructive-action authorization. Do not modify shared Git hooks or repository configuration to accommodate one workspace.

## Synchronization and cleanup

Sync isolated work when the target advances or before final verification, not before every task. Resolve conflicts according to the approved behavior and rerun affected checks. Keep uncertain changes visible in the record; one-shot resolves technical choices autonomously within its authority.

Keep the workspace until the user has committed or explicitly requests disposal. Prefer native archival when available. Otherwise preserve recoverable work before cleanup, and remove only recorded resources with authorization. Never delete another task's workspace, branch, or data.

Completion: the working location, starting state, required configuration, and any allocated resources are recorded and suitable for the task.
