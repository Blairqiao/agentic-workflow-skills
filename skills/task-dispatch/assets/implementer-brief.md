# Implementer brief: <task-id>

You are implementing one task. Work only inside the workspace at `<path>`.

## Task

- Goal: <one sentence>
- Criteria: <AC IDs with their full text>
- Scope: <files or globs>
- Mode: <verification mode> · Stubs allowed: <yes | no>
- Red expectation: <tests to add and how they should fail>

## Read-only context

Spec: <path> · Plan: <path> · Taskboard: <path> · Profile: <path>

## Commands

- Single test: <command>
- Fast suite: <command>
- Lint: <command>
- Typecheck: <command>

## Rules

- Follow `tdd-integrity`: a red commit, then a green commit. Never edit tests during green.
- Change only files in scope. Never push, never touch the main checkout, never print secrets.
- If the criteria are unclear, ask instead of guessing.

## Return

- Commits made, with hashes.
- Commands you ran and their results.
- Decisions you made and why, in a few lines.
- Anything you couldn't do, and anything that looked wrong.
