---
name: brainstorm
description: Explore an idea before building it. Asks focused questions, lays out two or three distinct approaches with tradeoffs, and lets the user pick. Use when the user wants to brainstorm, is unsure what to build or how, or asks to be grilled on a design. Skip for clear, specific requests.
---

# Brainstorm

Turn a fuzzy idea into a chosen direction. Do not write code, tests, or a plan here. The output is a decision the user made, ready for the `planning` skill.

## 1. Ground yourself first

Read the relevant code, README, and existing `.agent-docs/` notes before asking anything. Never ask the user a question you can answer by looking. If a lookup is slow, ask the questions that don't depend on it while it runs.

## 2. Understand the problem

Ask one question at a time. Prefer multiple choice with your recommended answer marked. Cover only what changes the design:

- Who uses this and what are they trying to do?
- What does "done" look like?
- Hard constraints: deadlines, stack, compatibility, things that must not change.

Stop asking once you could explain the problem back in two sentences. Do that, and let the user correct it.

## 3. Offer approaches

Present two or three approaches that are actually different, not one idea in three sizes. For each one:

- **What it is.** One or two sentences.
- **Cost.** Rough size, files or systems touched, new dependencies.
- **Tradeoff.** What you gain and what you give up.

Then recommend one and say why. If there is only one sensible approach, say so and skip the menu. Apply YAGNI: cut features the user didn't ask for.

Let the user pick. They can also mix parts of different options.

## 4. Stress-test (optional)

Run this when the choice is costly to reverse (data model, public API, security, architecture) or when the user says "grill me". Walk the decision tree:

1. List the open decisions whose prerequisites are already settled.
2. Ask them as a numbered round. Give each one a recommended answer.
3. Use the answers to settle those decisions and unblock the next ones, then ask the next round.
4. Stop when no open decisions remain and nothing is silently assumed.

Look up facts yourself. Only put real decisions to the user.

## 5. Close

Summarize the decision in a short block:

```markdown
**Problem.** ...
**Chosen approach.** ...
**Out of scope.** ...
**Open questions.** none | ...
```

Then offer to run `planning`. Keep the summary in chat unless the user asks to save it. If they do, write it to `.agent-docs/briefs/<topic>.md`.
