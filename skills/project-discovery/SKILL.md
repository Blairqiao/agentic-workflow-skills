---
name: project-discovery
description: >-
  Discover how a codebase installs, builds, tests, configures and runs, then record verified commands and conventions in docs/agent-profile.md. Use before the first workflow run in a repository, when the profile is missing or stale, or whenever an agent would otherwise guess a project's test, lint, env or service setup.
---

# Project discovery

Every other skill reads the project profile instead of assuming things about the codebase. Fill it with facts you have checked, and mark anything you could not check.

## Sources, most trusted first

1. **CI configuration.** For example `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`. CI is what the team actually enforces.
2. **Scripts and task runners.** Manifest script sections, `Makefile`, `justfile`, `Taskfile` and similar.
3. **Docs.** `AGENTS.md`, `CONTRIBUTING.md`, `README.md`. Docs drift, so confirm by running.
4. **Manifests and lockfiles.** These tell you the ecosystem and package manager.
5. **Inference.** Conventions you deduce. Mark them unverified.

`references/ecosystem-hints.md` lists common starting points per ecosystem. Treat it as a list of places to look, never as the answer.

## What to record

Use `assets/profile-template.md`. Cover:
- **Packages.** Each manifest root in a monorepo, its ecosystem and package manager.
- **Install.** The frozen or locked install command, which uses the lockfile without rewriting it.
- **Checks.** Format, lint, typecheck and build commands.
- **Tests.** How to run one test, one file and the fast suite, plus slower tiers such as integration or e2e and the services they need. Note how to get machine-readable results, or that only exit codes are available.
- **Test layout.** Where test code lives: separate directories, files beside the code, test modules inside source files, doctests, fixtures, snapshots, shared helpers, runner config.
- **Environment.** Env and config files by name, and which are committed templates versus local-only. Record names only, never values.
- **Services.** Databases, caches, queues, search, object storage, emulators, ports, and how the project starts them.
- **Hooks.** Pre-commit and pre-push hooks, and whether they rewrite files.
- **Boundaries.** Paths that need extra care, such as auth, payments, migrations, infrastructure and public APIs.
- **VCS facts.** Submodules, Git LFS, generated or vendored code, monorepo layout.
- **Workflow settings.** Fast-track limits, artifact locations, evidence storage and delivery preference, if the user has opinions.

## Calibrate before trusting

Do this in a scratch workspace, never in the user's main checkout:
1. Run the fast test command twice on a clean checkout. Record runtime, test count, and any test whose result changes between runs.
2. Add a throwaway test that must fail on an assertion. Confirm the command reports it as failing, and that you can tell an assertion failure apart from an import or setup error. Remove the test.
3. Confirm the frozen install succeeds from scratch.

Write each outcome into the profile. If a step fails, say what that means for later phases, for example: "Only exit codes are available, so integrity checks rely on reading diffs."

## Keep it current

Mark the profile stale when manifests, lockfile tooling, CI config or test runner config change, then rerun discovery for the affected parts. When you first create the profile, show the user a short summary and ask them to confirm or correct it.
