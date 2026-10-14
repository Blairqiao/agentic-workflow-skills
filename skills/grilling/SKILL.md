---
name: grilling
description: >-
  Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, resolve architectural tradeoffs, or uses any 'grill' trigger phrases.
---

# Grilling

Interview the user relentlessly until you reach a shared understanding. Map the discussion as a **design tree** where every decision branches into the downstream decisions that depend on it.

When invoked for a scoped decision, build the tree only for that decision and its relevant downstream branches. Reuse settled conversation and brainstorm decisions as prerequisites, without reopening unrelated product choices. If evidence contradicts a prerequisite or resolution requires expanding scope, surface the conflict and establish the revised boundary with the user before pursuing the affected branch. An explicit request to grill the whole design retains that broader scope.

An unresolved domain meaning is an unsettled prerequisite. Use [domain-modeling](../domain-modeling/SKILL.md) to resolve it before asking dependent design questions; independent frontier questions can proceed. Research inspectable facts first. During an explicitly autonomous one-shot run, apply [shared decision rules](../_workflow/design.md#shared-decision-rules) without starting this interview.

Work the tree in **rounds**. The **frontier** contains every decision whose prerequisites are already settled, meaning the questions you can ask right now without guessing at answers you have not heard yet. Ask the whole frontier in one round, numbering each question and giving your recommended answer. Wait for the user's answers before starting the next round.

Format each round like this:

```markdown
**Q1. <Question title>.** <Question body, which may span multiple paragraphs and include concrete options.>

**Recommendation.** <Your recommended answer and rationale.>

---

**Q2. <Question title>.** <Question body, which may span multiple paragraphs and include concrete options.>

**Recommendation.** <Your recommended answer and rationale.>
```

Each round the user answers reshapes the tree. Settled decisions push the frontier outward and unblock downstream questions. Recompute the frontier and ask the next round. Any question whose answer depends on another open question in the current round belongs to a later round.

Finding facts is your job, never the user's. When a frontier question depends on a fact from the environment, such as the filesystem or tools, inspect the repository or dispatch a subagent to find it rather than asking the user for something you can look up yourself. Do not block the whole round on exploration. Only the questions downstream of a running lookup wait for the result; ask the rest of the frontier immediately. Put only real decisions to the user and wait.

The session ends when the frontier is empty, every branch within the agreed scope has been visited, and nothing remains silently assumed. Confirm shared understanding, then return settled decisions and their rationale to the calling conversation or active design record. This confirmation is not implementation approval; the active track retains its approval gate. Do not start implementation merely because the grilling session is complete.
