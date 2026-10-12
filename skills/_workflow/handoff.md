# Integration and handoff

Inputs: verified candidate, review verdict, proof, walkthrough, and delivery preference if known.

1. Inspect the final diff for unrelated edits, secrets, generated clutter, and unfinished scaffolding. Ensure `.gitignore` contains rules ignoring both `docs` (`docs/*`, `docs`) and `.worktrees` (`.worktrees/*`, `.worktrees`), confirm all workflow documentation resides in `<main-repo>/docs/` (or via a `<worktree>/docs -> <main-repo>/docs` symlink, never isolated inside a worktree), and verify no files inside `docs/` or `.worktrees/` are staged in Git. Run applicable formatting hooks before final checks if they change the candidate.
2. For in-place work, stage only candidate paths or hunks, preserving the user's existing index and working changes. If those changes cannot be separated safely, leave them unstaged and explain why. Do not create a target-branch commit.
3. For isolated work, follow an established delivery preference. Otherwise leave the reviewed candidate in its worktree, stage its changes, and provide the location. This default avoids another decision gate in one-shot.
4. If delivering a staged squash to the main checkout, first require a clean checkout on the expected target revision. Then compare staged content with the verified candidate. A mismatch requires reconciliation and relevant verification; never stash or reset user work to force delivery.
5. Present what changed, verification results, artifact links, and any risks or incomplete requirements. Suggest a commit message when useful. Leave publishing and the final target-branch commit to the user.

Keep the workspace available for review. After the user commits or authorizes disposal, follow [workspace cleanup](workspace.md), preserving recoverable work and respecting destructive-action authorization.

Completion: the user has an identifiable, reviewable candidate with proof and walkthrough, and no unsupported completion claims.
