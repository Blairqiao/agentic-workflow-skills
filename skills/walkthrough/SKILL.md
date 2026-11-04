---
name: walkthrough
description: Write an easy-to-follow walkthrough of a project or a recent change, covering what it does, how the pieces fit, and where to start reading. Use when the user asks to explain, tour, onboard onto, or walk through a codebase, feature, or diff.
---

# Walkthrough

Explain the code so a new developer can find their way around in ten minutes. Aim for understanding, not completeness.

## Pick the scope

- **Project.** The whole repository or one subsystem.
- **Change.** A diff, branch, or finished plan. Use `git diff`, `git log`, and the plan in `.agent-docs/plans/` if one exists.

If the user didn't say, infer it. "Walk me through this repo" means project. Asking right after a build means change.

## Read before writing

Start with the README, the manifest (`package.json`, `pyproject.toml`, etc.), entry points, and the directory layout. Then follow one real request or command through the code. For a large repository, send read-only subagents to separate subsystems and ask each for a short summary with file paths. Write the final explanation yourself.

Only state what you've read. If you're inferring, say so.

## Structure

Use this order and skip sections that don't apply:

1. **What it is.** Two or three sentences in plain language, no jargon.
2. **How to run it.** The few commands that matter.
3. **Map.** The top-level folders and key files, one line each on what lives there.
4. **How it works.** Trace one important flow step by step, such as "user clicks Save, then X, then Y, then the data lands in Z." Link each step to its file. Add a small Mermaid diagram if the flow branches or crosses several services.
5. **Key concepts.** Domain terms or patterns a newcomer would trip on.
6. **Where to start.** Which files to read first, and where to make common changes.

For a change walkthrough, swap sections 3 to 6 for: what changed and why, each change grouped by behavior rather than by file, how to try it, and risks or follow-ups.

## Style

Use short sentences and concrete names. Link files as `path/to/file.ts:42`. Explain why something exists, not only what it is. Use a table or list where it's easier to scan than prose. Apply `unslop`.

## Output

Answer inline by default. If the walkthrough runs long or the user wants to keep it, save it to `.agent-docs/walkthroughs/<topic>.md`, with `.agent-docs/` listed in `.git/info/exclude`. Use `docs/` instead if it should ship with the repository. If you saved a file, end with a clickable markdown link to it using its absolute path.
