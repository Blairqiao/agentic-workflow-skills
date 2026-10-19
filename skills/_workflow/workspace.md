# Workspace preparation

Inputs: track, repository state, relevant configuration, and service needs.

1. Identify the main repository checkout from `git worktree list --porcelain`; when already inside a linked worktree, its top-level directory is not the main repository root.
2. Before creating a worktree or writing any file in `<main-repo>/.agent-docs/`, ensure both `.worktrees` and `.agent-docs` are ignored in `<main-repo>/.git/info/exclude`, preserving existing entries:
   ```text
   .worktrees/*
   .worktrees
   .agent-docs/*
   .agent-docs
   ```
   Do not modify `<main-repo>/.gitignore`. Writing the patterns to `<main-repo>/.git/info/exclude` keeps the tracked working tree clean while applying the ignore rules across `<main-repo>` and all linked worktrees. Verify exclusion of both paths with `git check-ignore` from `<main-repo>`.
3. Inspect Git status, branch, existing worktrees, and user edits. Record the starting revision and pre-existing changes so in-place runs can restore candidate files cleanly if retry caps are reached. Never stash, reset, or overwrite user work to simplify setup.
4. Fast-track follows up in the existing candidate workspace. Full, boost, experimental orchestration, and one-shot prefer an isolated worktree at `<main-repo>/.worktrees/<feature>`, or `<main-repo>/.worktrees/<run-id>` when a second concurrent checkout is needed. Use the checkout named in the authorized plan. Reuse an existing worktree only when its resolved path sits inside `<main-repo>/.worktrees/` and suits the task; never nest a worktree inside another linked worktree.
5. Base isolated work on the agreed target or current draft. If uncommitted work is part of the task, copy or apply it into the worktree explicitly because `git worktree add` from `HEAD` does not include uncommitted edits.
6. Install existing locked dependencies only when needed. Keep dependency directories separate, though shared download caches are acceptable. If setup fails, diagnose the cause rather than rewriting the lockfile reflexively.
7. Run relevant baseline checks once when needed and record existing failures. Do not rerun a valid baseline merely because another phase begins.

## Worktree placement, documentation location, and tool exclusions

All workflow documentation in `.agent-docs/` must reside in `<main-repo>/.agent-docs/` directly by path, never as isolated files or symlinks inside `<main-repo>/.worktrees/<feature>/`. Reading and writing `<main-repo>/.agent-docs/...` directly prevents stray symlinks from being staged and preserves documentation when a worktree is removed. In all repository documentation under `.agent-docs/`, `docs/`, and `AGENTS.md`, links to files must use repository-rooted local paths starting with `/` such as `/.agent-docs/...` and `/src/...`, never host-absolute `file:///` URLs.

When creating a worktree in a repository whose linters, typecheckers, or test runners discover files by directory globs rather than Git, add a root-anchored `.worktrees` exclusion to the project's tool ignore configuration, such as `.worktrees/**` in `tsconfig.json` and ESLint, `<rootDir>/.worktrees/` in Jest, or `norecursedirs = [".worktrees"]` in `pytest`. Never use an unanchored `**/.worktrees/**` or substring `.worktrees` pattern that matches the worktree's own absolute path and silences checks run inside the worktree. Verify that tool discovery works from both `<main-repo>` and the worktree.

For persistent custom worktrees, use a harness worktree tool only if it accepts `<main-repo>/.worktrees/<feature>`. Otherwise run `git worktree add` with that explicit path. Resolve symlinks before creation so the destination cannot escape the main repository. Never create persistent custom candidate worktrees in `.codex`, `.claude`, `.gemini`, or other harness-owned directories.

Boost native ephemeral workers are harness-managed and may use different locations. Do not promise repository-local placement for every native internal worker. Keep the final candidate in the named persistent checkout. Verify actual worker containment, ownership of changed files, integration into that checkout, and absence of writes to protected user resources. Record unknown native placement or isolation as an operational limitation and require a live runner smoke test before claiming it verified. Native worker paths do not change the main-root documentation rule.

Use one execution slug across plan, proof, taskboard, images, and workspace references. Allocate a distinct slug for each concurrent run and record its plan revision. Workers receive the exact plan path and revision; they must not overwrite another run's plan.

## Conditional service setup

If the task starts an app or service, inventory the resources it uses. Create non-production configuration from committed templates or documented setup. If local credentials are needed, use an authorized mechanism that does not expose secret values.

Allocate separate ports, service namespaces, and data paths when concurrent work or user resources could be affected. See [resource isolation](references/resource-isolation.md). Record allocations and cleanup commands. Verify an allocation's identity before any migration, reset, or deletion, and obtain destructive-action authorization when required. Do not modify shared Git hooks or repository configuration to accommodate one workspace.

## Synchronization and cleanup

Sync isolated work when the target branch advances or before final verification, not before every task. Resolve conflicts according to the approved behavior and rerun affected checks. Keep uncertain changes visible in the record; one-shot resolves technical choices autonomously within its authority.

Keep the workspace until the user commits or explicitly requests disposal. Prefer native archival when available. Otherwise preserve recoverable work before cleanup, and remove only recorded resources with authorization. Never delete another task's workspace, branch, or data.

Completion: `<main-repo>/.git/info/exclude` is verified, and the working location, starting state, required configuration, and allocated resources are recorded and ready for the task.
