---
name: integration-handoff
description: >-
  Hand finished workflow changes to the user safely: sync with the target branch, deliver as staged squashed changes, a branch or a patch, prove the delivered content matches what was tested, suggest a commit message, and clean up only after the user commits. Use at the end of any workflow track.
---

# Integration and handoff

The user commits. Your job is to make the change easy to review, and to prove that what you hand over is exactly what was tested.

## Preconditions

- Every required task is done, and `verification-evidence` ran after the latest sync with the target branch.
- The repository's own pre-commit formatters have run in the workspace and their changes are committed, so the user's commit won't rewrite files.

## Choose delivery

Use the profile's preference, or ask:
- **Staged squash.** Changes staged but uncommitted in the user's main checkout.
- **Branch.** Leave `agent/<run-id>` for the user to review, push and open a pull request.
- **Patch.** A patch file the user applies themselves.

## Staged squash

1. Check the main checkout. It must be on the target branch, with no uncommitted changes, at the same commit you last synced from. If not, stop and offer the branch option. Never stash or reset the user's work.
2. Run `git merge --squash <branch>` in the main checkout.
3. Confirm the staged content equals the tested branch: `git diff --cached --exit-code <branch>` should report no differences. If evidence or taskboard files are meant to stay out of the commit, exclude them with a pathspec and tell the user.
4. Show the user a summary and a suggested commit message based on `assets/commit-message-template.md`, listing the criteria covered and linking the evidence. Then stop.

## After the user commits

- Compare the commit with the branch, for example `git diff <branch> HEAD --stat`. If the user changed something, note it in the taskboard. That's their call, not an error.
- Then run the teardown in `worktree-setup`, which archives the branch head before deleting the branch.

If the user wants to keep the branch or workspace, skip teardown and record that.

## Never

Push, open pull requests on the user's behalf, commit to the target branch, or delete anything the allocation record doesn't list.
