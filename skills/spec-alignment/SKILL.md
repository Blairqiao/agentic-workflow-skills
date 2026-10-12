---
name: spec-alignment
description: >-
  Turn a feature request into an approved design spec through focused questioning, with numbered, testable acceptance criteria. Use in the align phase of the full-track or one-shot workflow, or whenever the user wants to pin down what to build before code is written.
---

# Spec alignment

The spec is what every later check measures against. Vague criteria here become unreviewable work later.

## Questioning

- Read the relevant code and the project profile first, so your questions are about choices rather than facts you could look up.
- Ask at most three questions per message, most important first. Offer concrete options where you can.
- Cover: user-visible behavior, edge cases and failure modes, data and migrations, permissions and security, performance limits, compatibility, and what is explicitly out of scope.
- After each round, restate your understanding in a few lines so the user can correct it.
- Stop when every acceptance criterion is testable and the non-goals are clear.

## Writing the spec

Use `assets/spec-template.md` and save to the profile's spec location, by default `docs/spec/<feature>.md`.

For acceptance criteria:
- Number them `AC-1`, `AC-2` and so on. Plans, tests, reviews and evidence cite these IDs.
- State one observable behavior per criterion, with a clear pass condition.
- Say how each one is verified: automated test, manual check, or both.
- Mark criteria that touch the profile's boundary paths.

Add mockups, diagrams or example payloads where they remove ambiguity. Leave code out except interface sketches of a few lines.

## Gate

Show the spec and ask the user to approve it. Record the approval in the spec header with the date and the user's words. After approval the spec is frozen. Any change goes in its Amendments section and needs a fresh approval.

In one-shot runs, skip the gate and mark the status "approved by request".
