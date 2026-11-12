# Coordinate a plan

You are the coordinator. Every plan runs through you, whether it has one slice or many. You don't build or review code yourself. You run the plan's phases in order. For each phase you start one orchestrator per slice, merge their branches, and start a review gate. Gemini Flash can do this job. The judgment calls belong to the children: Sol orchestrators build and review each task, and an Opus or Astra reviewer checks each phase.

Keep your context small. Read the index, the children's final report lines, and the review verdicts. Don't read slice files or diffs. The children do that.

## Phases

The index's `## Phases` section lists the phases in order. The planner decides how many phases there are and what each holds, so there's no fixed set. Each phase has one or more slices that run in parallel. A phase starts only after the previous phase has merged and passed review. Every phase ends with a review gate, and the gate after the last phase is the whole-feature final review.

**No `## Phases` section** (an older single-file plan with its own tasks): treat it as one phase whose only slice is that file. Write that phase into the file before you start, so the checkboxes have somewhere to go.

## Before starting

1. Read the index. Being asked to run it is the go-ahead.
2. Run `git status` in the main checkout and note any uncommitted user changes. Never touch them.
3. **Resuming?** If phase boxes are already ticked, or the index Notes have a `Coordinator` entry, reuse the integration worktree and baseline recorded there, and continue from the first unticked box. Skip steps 4 and 5.
4. Add `.worktrees/` to `.git/info/exclude` if it isn't already there. Create the integration worktree from the plan's base: `git worktree add .worktrees/<feature> -b <feature> <base>`. Every merge, test run, review, and fix happens there. Your main checkout stays as it was.
5. In the integration worktree, run the plan's test, lint, and build commands once, each sent to a log file. Under `Coordinator` in the index Notes, record the integration worktree's absolute path, the branch, and the baseline counts.
6. Call `orchestrator_capabilities` once. If `~/.agents/routing.md` exists, read it and use the instance it names whenever you dispatch a model it lists, following its fallback rule. If the user named a provider instance, that overrides the file. Add `Provider routing: <the user's words>` to every child prompt so it reaches the implementers. Set the index status to `in progress`.

Plan files live in `.agent-docs/` in the main checkout, which worktrees don't see. Always give children the absolute paths to the index and slice files.

## Per-phase loop

1. **Record the start.** Note the integration branch's head SHA as the phase's `Start`.
2. **Start the slices.** For each slice in the phase, call `delegate_task` with Sol at the index's orchestrator effort and `isolation: "worktree"`. Start every slice in the phase at once, using the slice prompt below.
3. **Wait.** Follow each delegate's `next`. Don't poll. As each slice finishes, read its last line:
   - `ready for final review`: done. Tick `Slices done` once every slice in the phase is.
   - `handoff`: start a fresh Sol child without isolation in that slice's worktree, using the slice prompt with `Resume in [worktree path].` added.
   - `stuck` or `blocked`: let the other slices finish, then stop and pass the child's question to the user. Don't merge a partial phase.
4. **Merge.** In the integration worktree, merge each slice branch in the phase's merge order with `git merge --no-ff <slice-branch>`. A one-slice phase still merges, to keep every phase the same. On a conflict, run `git merge --abort`, stop, and report it: two slices touched the same file, so the plan's file ownership was wrong. Then run test, lint, and build to logs and compare them against the baseline. Tick `Merged`. Failures don't stop you. Pass them to the reviewer.
5. **Review gate.** Call `delegate_task` with Opus (or Astra), without isolation, using the review prompt below. Wait for its verdict.
6. **Act on the verdict.**
   - **PASS** or **PASS after fixes**: the reviewer ticks `Reviewed`. Go to the next phase.
   - **FIX** (rare, since the reviewer fixes everything short of very large work itself): call `delegate_task` with Sol, without isolation, using the fix prompt below. When it's done, run the review gate once more. If the second verdict is still FIX, stop and report to the user. Two rounds of fixes that don't land mean the plan or the phase needs a human decision.

## Prompts

Fill in the brackets. Paths are absolute.

**Slice:**

```text
Run the orchestrate skill on [abs path to slice file] as a slice.
Index: [abs path to index]. Your worktree must start at integration commit [phase start SHA]. Check `git rev-parse HEAD` first. If it differs and the worktree is fresh, run `git checkout -B [feature]-[slice] [phase start SHA]`.
Commit on that branch. When you're done or have to stop, end with exactly one line:
Slice [n]: <ready for final review | handoff | stuck | blocked>, branch <branch>, head <sha>
```

**Review gate:**

```text
Run the final-review skill on [abs path to index], phase [k] of [K] ([phase name]).
Work in [abs path to integration worktree]. Review range: [phase start SHA]..HEAD.
Merge and test results after merging: [one line each, plus any failing test names].
```

**Fix:**

```text
Run the orchestrate skill on [abs path to index], fixing the phase [k] review findings in its Notes.
Work in [abs path to integration worktree] and commit there. Don't create a worktree.
```

## Handing off

Every step is a box in the index, so a fresh coordinator can resume from the boxes alone. If the session grows large or the user says "hand off", write any in-flight state under `Coordinator`, such as which delegates are still running and their thread links, and give this prompt:

```text
Run the orchestrate skill on .agent-docs/plans/<feature>.md
```

## Finish

After the last phase passes review, the final reviewer sets the status to `done`. In chat, give:

- Each phase with its verdict, and any fix rounds.
- The integration branch and its worktree path. The feature is on that branch, ready for the user to merge and push. Don't merge it into their branch yourself.
- The slice worktrees you left in place. Removing them is for the user to decide.
- Anything a child marked unverified.

End with a clickable markdown link to the index on its own line, using the absolute path.

## Other harnesses

Without `delegate_task`, use the native subagent tool if it supports worktree isolation and nested subagents, and tell the user which models you substituted. If it doesn't, stop. Give the user one copy-paste slice prompt for each slice in the current phase, and ask them to rerun you when those slices finish. You then merge the phase and run its gate as usual.

## Stop and ask when

- A slice is stuck or blocked, a merge conflicts, or a phase fails review twice.
- A child asks for a dependency, a migration, or a destructive operation.
