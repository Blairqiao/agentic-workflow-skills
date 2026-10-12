# Workspace preparation

Inputs: track, repository state, relevant configuration and service needs.

1. Inspect Git status, branch, existing worktrees, and user edits. Record the starting revision and pre-existing changes. Never stash, reset, or overwrite user work to make setup easier.
2. Fast-track uses the current workspace. Full/one-shot prefer a suitable existing repository-local worktree or create one using the placement rules below. A small task or explicit request can use the current checkout. If worktrees are unsuitable, use a local clone or copy and record the reason.
3. Base isolated work on the agreed target or current draft. If uncommitted work is part of the task, preserve it explicitly; a worktree created from HEAD does not include it automatically. Use unique paths and branch names following repository or harness conventions.
4. Install existing locked dependencies only when needed. Keep dependency directories separate; shared download caches are acceptable. If setup fails, diagnose rather than rewriting the lockfile reflexively.
5. Run relevant baseline checks when needed and record existing failures. Do not rerun a valid baseline merely because another procedure begins.

## Worktree placement and `.gitignore` rules

Use `<main-repo>/.worktrees/<run-id>`. Identify the main repository checkout from `git worktree list --porcelain`; when already in a linked worktree, its top-level directory is not the main repository root. Reuse an existing worktree only when its resolved path is inside that main repository's `.worktrees/` directory and it suits the task. Do not nest a new worktree under another linked worktree.

Whenever creating or updating a repository's `.gitignore` (and before creating a worktree or writing workflow `docs/`), ensure both `.worktrees` (`.worktrees/*`, `.worktrees`) and `docs` (`docs/*`, `docs`) are present in the main checkout's root `.gitignore`, preserving existing entries, so all files within `docs/` and `.worktrees/` remain hidden from Git. Verify exclusion of both folders with `git check-ignore` from that checkout. Keep this ignore-file edit visible in the handoff and include it in the candidate delivery without losing unrelated changes; do not make a setup commit. A global ignore rule or `.git/info/exclude` is not a substitute for the repository's `.gitignore`.

Use a native tool only if it accepts the required repository-local path. Otherwise use `git worktree add` with that explicit destination. Resolve symlinks before creation so the destination cannot escape the main repository. Never create worktrees in `.codex`, `.claude`, `.gemini`, or other harness-owned directories, even when that is a tool's default. If the permitted path is unavailable, resolve the access problem rather than silently switching to a harness directory.

## Conditional service setup

If the task starts an app or service, inventory the resources it uses. Create non-production config from committed templates or documented setup. If local credentials are needed, use an authorized mechanism that does not expose their values.

Allocate separate ports, service namespaces, and data paths when concurrent work or user resources could be affected. See [resource isolation](references/resource-isolation.md). Record allocations and cleanup commands. Check an allocation's identity before any migration, reset, or deletion; obtain required destructive-action authorization. Do not modify shared Git hooks or repository configuration to accommodate one workspace.

## Synchronization and cleanup

Sync isolated work when the target advances or before final verification, not before every task. Resolve conflicts according to the approved behavior and rerun affected checks. Keep uncertain changes visible in the record; one-shot resolves technical choices autonomously within its authority.

Keep the workspace until the user has committed or explicitly requests disposal. Prefer native archival when available. Otherwise preserve recoverable work before cleanup, and remove only recorded resources with authorization. Never delete another task's workspace, branch, or data.

Completion: the working location, starting state, required configuration, and any allocated resources are recorded and suitable for the task.
