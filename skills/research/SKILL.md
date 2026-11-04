---
name: research
description: Audit a project's documentation against its actual code, then write or fix the docs. Use when the user asks to audit, cross-check, update, or create project documentation. For explaining a project, use `walkthrough`. Not for web research or code fixes.
---

# Research

Make the project's documentation match the code. This skill edits docs only. It never changes application behavior.

## 1. Scope

Confirm what to cover: the whole repository, one subsystem, or one doc. Note the current commit (`git rev-parse --short HEAD`) and any uncommitted changes, since the docs should match the working tree.

## 2. Inventory

List the maintained source with `git ls-files`, grouped into subsystems. Skip vendored, generated, and binary files. Next to each subsystem, note which doc covers it, or that none does.

For a large repository, give each subsystem to a read-only subagent. Ask each one for its responsibilities, entry points, public interfaces, config and env vars, commands, and file paths as evidence. Reconcile the results yourself.

## 3. Cross-check

Read each doc against the code it describes and sort what you find:

| Finding | Action |
| --- | --- |
| Missing doc | Write it from the code you read |
| Outdated doc | Fix it, citing the source file |
| Code contradicts documented intent | Don't pick a side. Report it as a possible bug |
| Unknown, such as rationale you can't see in the code | Leave a visible TODO. Don't guess |

Run documented commands (setup, test, build) when that's safe, and note any that fail. Read a script before running it.

## 4. Write

Keep docs where they already live. New guides go in `docs/`, with an index in `docs/README.md` or the main README. Write only the guides the project needs, typically overview, architecture, setup, and one guide per complex subsystem. Link source as repository-relative paths. Check that every link resolves. Apply `unslop`.

## 5. Report

Leave changes uncommitted. In chat, list the docs created or updated, the code-versus-docs contradictions, the commands that failed, and the areas not covered. Don't fix code bugs you found. List them for the user.
