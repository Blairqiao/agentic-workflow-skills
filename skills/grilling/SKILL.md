---
name: grilling
description: >-
  Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, resolve architectural tradeoffs, or uses any 'grill' trigger phrases.
---

# Grilling

Interview the user relentlessly until you reach a shared understanding. Map the discussion as a **design tree** where every decision branches into the downstream decisions that depend on it.

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

The session ends when the frontier is empty, every branch of the design tree has been visited, and nothing remains silently assumed. Do not act on the design until the user confirms you have reached a shared understanding.
