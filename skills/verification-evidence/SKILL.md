---
name: verification-evidence
description: >-
  Verify finished work from a clean checkout and write a reproducible proof of commands and outputs plus a walkthrough with manual verification steps. Use after all workflow tasks are done and the workspace is synced with the target branch, or whenever the user asks for proof that agent-written changes actually run.
---

# Verification and evidence

Passing tests don't prove the software works, and an agent-written proof is only worth as much as the user's ability to rerun it. Write evidence the user can reproduce.

## When

After every required task is done and after the final sync with the target branch, so the evidence describes exactly what will be delivered. If anything changes afterwards, regenerate it.

## Verify from a clean checkout

1. Create a fresh temporary checkout of the workspace branch's head commit.
2. Run the frozen install, then every check and test tier in the profile, plus the build.
3. If the change is user-facing, start the app on the workspace's ports and exercise the changed behavior. Capture screenshots or browser checks if your tools allow it.
4. Any failure stops here and goes back to the task loop.

## Proof

Write it with `assets/proof-template.md` to the profile's proof location, by default `docs/proofs/<feature>-proof.md`.
- If Showboat is installed, use it to record commands and their outputs; `showboat verify` reruns them later. Otherwise write commands and outputs as plain Markdown.
- Paste outputs exactly. Trim long logs to the summary and any failures, and say that you trimmed them. Never hand-edit an output; if it's wrong, rerun and regenerate.
- End with a Rerun section listing every command in order, so the user can reproduce each result.

## Walkthrough

Write it with `assets/walkthrough-template.md`, by default to `docs/walkthroughs/<feature>-walkthrough.md`: what changed task by task, design notes, risks, and numbered manual verification steps with expected results. Skip it when the track says so.

## Storage

Follow the profile. If it doesn't say, ask the user whether evidence goes into the repository or stays outside it. Screenshots committed to git stay in history permanently.
