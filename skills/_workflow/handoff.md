# Integration and handoff

Inputs: verified candidate, review verdict, combined proof and walkthrough, and delivery preference if known.

1. **Inspect diff and ignore rules.** Check the final diff for unrelated edits, secrets, generated clutter, and temporary scaffolding. Confirm `<main-repo>/.git/info/exclude` ignores both `.agent-docs` and `.worktrees`, verify all workflow documentation resides in `<main-repo>/.agent-docs/` without any symlink inside a worktree, and ensure no files under `.agent-docs/` or `.worktrees/` are tracked or staged in Git. Run applicable formatting hooks before final verification if they modify candidate files.
2. **In-place handoff.** For runs in the current workspace, enforce a strict no-commits and no-push rule. Stage the candidate paths or hunks with `git add` so the changes are ready for the user to inspect and commit, while leaving unrelated unstaged user edits untouched. Never run `git commit` or `git push` on the user's branch.
3. **Isolated worktree handoff.** For runs in `<main-repo>/.worktrees/<feature>` or `<main-repo>/.worktrees/<run-id>`, commit or stage candidate changes cleanly inside the worktree branch so the isolated state is preserved. Never stage or merge changes into `<main-repo>` automatically unless the user explicitly requested it. In the handoff message, provide:
   - The worktree path and branch name.
   - Explicit step-by-step merge commands to run from `<main-repo>`:
     1. `cd <main-repo>`
     2. `git merge --squash <worktree-branch>`
     3. Integration check: compile and test on target branch (`npx tsc --noEmit && npm test`) to catch cross-branch drift.
     4. `git commit -m "<suggested-message>"`
     5. Optional worktree cleanup (`git worktree remove .worktrees/<feature> && git branch -D <worktree-branch>`).
4. **Optional requested squash into `<main-repo>`.** If the user explicitly asks to stage a squashed diff in `<main-repo>`, first verify `<main-repo>` is on the expected target revision without conflicting edits, apply the candidate, and confirm the staged diff matches the verified candidate. Never stash or reset user work to force delivery.
5. **Summarize delivery.** Present what changed, verification results, links to the `.agent-docs/` records and updated project guides, and any remaining risks or incomplete requirements. Suggest a commit message when useful. Leave publishing and the final target-branch commit to the user.

Keep the worktree available until the user commits or authorizes disposal, then follow [workspace cleanup](workspace.md).

Completion: the user has a staged in-place candidate or a clean worktree branch with merge instructions, backed by complete proof and walkthrough documentation and zero unauthorized target-branch commits.
