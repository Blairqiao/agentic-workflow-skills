# Integration and handoff

Inputs: verified candidate, review verdict, proof, walkthrough, and delivery preference if known.

1. Inspect the final diff for unrelated edits, secrets, generated clutter, and unfinished scaffolding. Ensure `<main-repo>/.gitignore` and `<main-repo>/.git/info/exclude` contain rules ignoring both `.agent-docs` (`.agent-docs/*`, `.agent-docs`) and `.worktrees` (`.worktrees/*`, `.worktrees`), confirm all workflow documentation resides in `<main-repo>/.agent-docs/` without any symlink inside a worktree, and verify no files inside `.agent-docs/` or `.worktrees/` are staged or committed in Git. Run applicable formatting hooks before final checks if they change the candidate.
2. For in-place work, stage only candidate paths or hunks, preserving the user's existing index and working changes. If those changes cannot be separated safely, leave them unstaged and explain why. Do not create a target-branch commit.
3. For isolated work in `<main-repo>/.worktrees/<run-id>`, keep the `test(red)` and `feat(green)` commits intact on the worktree branch and commit or stage any remaining worktree edits cleanly inside the worktree. Never stage changes in `<main-repo>` automatically from a worktree run unless the user explicitly requested it. Provide the worktree path, branch name, and exact `git merge --squash <worktree-branch>` command for the user to run in `<main-repo>`.
4. If the user explicitly asks to stage a squashed diff in `<main-repo>`, first require a clean checkout on the expected target revision. Then compare staged content with the verified candidate. A mismatch requires reconciliation and relevant verification; never stash or reset user work to force delivery.
5. Present what changed, verification results, artifact links, and any risks or incomplete requirements. Suggest a commit message when useful. Leave publishing and the final target-branch commit to the user.

Keep the workspace available for review. After the user commits or authorizes disposal, follow [workspace cleanup](workspace.md), preserving recoverable work and respecting destructive-action authorization.

Completion: the user has an identifiable, reviewable candidate with proof and walkthrough, and no unsupported completion claims.
