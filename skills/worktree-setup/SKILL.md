---
name: worktree-setup
description: >-
  Create, provision, sync and later tear down an isolated workspace for agent work (git worktree, local clone or copy), including env and config files, dependencies, ports, databases, caches, queues and containers, without touching the user's main checkout or live secrets. Use whenever a workflow needs an isolated workspace, when syncing one with its target branch, or when cleaning one up.
---

# Workspace setup and teardown

The user's main checkout, running servers and real data should never notice that agents are working. A separate directory is not enough: every resource the app touches needs its own instance or its own namespace.

## 1. Choose the isolation method

Pick the lightest method that works for this repository and record the choice:
- **git worktree.** The default for plain git repositories.
- **Local clone.** For example `git clone --local`. Use it when the repo has submodules, Git LFS set up with repo-local hooks, or tools that break when `.git` is a file instead of a directory. Git's own docs call submodule support in worktrees incomplete.
- **Directory copy.** For repositories without git, or when the user doesn't want agent branches in their repo. Track changes by initializing a throwaway git repo inside the copy.
- **The project's own mechanism.** If the repo ships a devcontainer, a dev-environment script or a workspace tool, prefer it.

## 2. Place and name it

- Prefer a location outside the repository, such as a sibling directory `../<repo>-worktrees/<run-id>`. If it must live inside, make sure git ignores it: check with `git check-ignore`, and add it to `.git/info/exclude` rather than editing `.gitignore` unless the user wants that.
- Use a unique run ID such as `<feature>-<YYYYMMDD-HHMM>-<4 random hex>`, and a branch such as `agent/<run-id>`.
- Base it on the current head of the target branch, and record that commit.
- Never stash, check out, reset or clean anything in the main checkout to make setup work.

## 3. Env and config files

The workspace should get working, non-production configuration without any secret value passing through your context.

1. Take the inventory of env and config files from the profile: committed templates, local-only files, per-environment variants. Don't open local-only files to read their values.
2. Build the workspace's config, preferring the first option that works:
   - copy a committed template, then fill in workspace-specific, non-secret values such as ports, database names and service URLs;
   - run the project's documented setup script if it creates local config;
   - only with the user's approval, copy specific named keys from their local config, limited to test or development credentials.
3. Never copy production credentials, never print values, and never commit config files. Confirm that the files you created are ignored inside the workspace.
4. Record in the taskboard which keys you set and where each came from, by name only.
5. If something can't be configured without a secret you don't have, stop and ask.

## 4. Isolate shared resources

List everything the app talks to: databases, caches, queues and workers, search, object storage, email or webhook sinks, emulators, ports, container projects, and paths outside the repo such as upload or temp directories. Give the workspace its own instance or namespace for each one and record it.

| Resource | Usual isolation |
| --- | --- |
| Ports | A free port per service, recorded and passed through config |
| SQL databases | A separate database named `<project>_wt_<id>`, created and migrated from the workspace |
| Caches | A separate logical database or a key prefix |
| Queues and workers | A queue-name prefix; no workers consuming shared queues |
| Containers | A per-workspace compose project name |
| File paths | Directories inside the workspace |

`references/resource-isolation.md` has engine-specific notes. If a resource can't be isolated, explain the risk and get the user's approval before sharing it.

**Name guard.** Before you create, migrate, reset or drop anything, check its name against the allocation you recorded and the workspace prefix. Never take a drop target from an environment variable alone, because a missing or inherited variable can point at the user's real database.

## 5. Dependencies

- Install with the profile's frozen install command, so the lockfile is used and not rewritten.
- If the frozen install fails, stop and report. Don't regenerate the lockfile during setup.
- Shared download caches are fine. Don't symlink dependency directories such as `node_modules` or virtual environments from the main checkout, because writes would leak across.

## 6. Hooks and git config

Hooks and repository config are shared between worktrees. Don't edit `.git/hooks`, `core.hooksPath` or repo-level git config. Note which hooks run on commit, since they may reformat files at handoff.

## 7. Baseline

Run the profile's fast checks in the new workspace before changing anything. Record which tests pass, which already fail, and the test count. Pre-existing failures belong to the base branch, and later checks need this list to prove that no test went missing.

## 8. Record the allocation

Write to the taskboard: method, path, branch, base commit, ports, resource names, config keys set, and the exact teardown steps.

## Syncing with the target branch

At the start of each task, merge the target branch into the workspace so the task's diff contains only its own changes. If only lockfiles conflict, take both sides' manifest changes, regenerate the lockfile with the package manager's documented conflict-resolution method, read the lockfile diff for unexpected packages, then run the frozen install. If manifests conflict, or you're unsure, stop and ask.

## Teardown

Tear down only after the user has committed, or has told you to discard the work.
1. Stop processes you started for the workspace.
2. Remove each recorded resource, checking every name against the allocation first. A database with open connections may refuse to drop; close them, or use the engine's force option for that one database.
3. Save the branch head under an archive ref, for example `git update-ref refs/archive/<run-id> <branch>`, so the history survives.
4. Remove the workspace with `git worktree remove`, or delete the clone or copy, then run `git worktree prune`.
5. Delete the branch. After a squash merge git doesn't see it as merged, so `git branch -d` fails; use `-D`, and only after the archive ref exists.
6. Move the taskboard to its archive location.
