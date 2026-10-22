# Integration and handoff

Inputs: verified candidate, observable review verdict, proof and walkthrough, and target branch state.

1. Inspect the final diff for unrelated edits, secrets, generated clutter, and temporary scaffolding. Confirm ignore rules and main-root documentation placement from [workspace preparation](workspace.md). No workflow record or nested-worktree symlink may be staged. Run formatting hooks before final verification if they alter candidate files.
2. Enforce no agent commits and no push during execution and handoff. In-place runs stage only candidate paths or hunks with `git add`, leaving unrelated user edits untouched. Never commit on the target branch or publish automatically.
3. For isolated work, stage the candidate cleanly in its named persistent worktree branch. Do not stage or merge into the main checkout unless explicitly requested. A squash merge transfers committed branch history, not unstaged or staged working-tree edits. Preserve the checkout and explain that the user commits the candidate branch before merging. Provide commands tailored to actual paths and branch names:
   ```sh
   cd <candidate-worktree>
   git diff --cached
   git commit -m "<suggested-candidate-message>"
   cd <main-repo>
   git merge --squash <candidate-branch>
   <actual-repository-verification-command>
   git commit -m "<suggested-final-message>"
   ```
   Inspect target status and resolve conflicting user edits before these user-run integration steps. Choose actual repository verification commands from the plan and project scripts, rather than assuming a language or package manager. Verify target branch integration again because target changes may invalidate candidate evidence. These commands are instructions for the user, not agent authorization to commit.
4. If the user explicitly requests a staged squash in the main checkout while the candidate is uncommitted, transfer the complete verified candidate diff deliberately. Include new files, preserve user changes, and verify that the staged result matches the candidate. Do not claim `git merge --squash` included uncommitted changes. Never stash or reset user work to force delivery.
5. Summarize what changed, actual checks, acceptance coverage, review independence, documentation links, candidate path and branch, and remaining limitations. Identify the exact plan and revision and the selected executor. Include native boost evidence gaps and unrun live smoke tests. Leave publishing and final commits to the user.

Keep the worktree available until the user commits or authorizes disposal. Optional cleanup instructions must identify the recorded checkout and branch and require confirmation that all candidate work is preserved. Use `git worktree remove <candidate-worktree>` and `git branch -d <candidate-branch>` only when safe; squash integration may require a deliberate user decision before deleting the unmerged branch. Follow [workspace cleanup](workspace.md).

Completion: the user has a staged candidate, complete proof and walkthrough, and integration instructions that preserve the actual working-tree changes.
