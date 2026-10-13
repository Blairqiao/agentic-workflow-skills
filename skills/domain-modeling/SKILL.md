---
name: domain-modeling
description: Build and sharpen a project's domain model and shared dictionary in .agent-docs/CONTEXT.md. Use when discussing codebase terminology, resolving overloaded or conflicting domain terms, or writing and updating .agent-docs/CONTEXT.md.
---

# Domain modeling

Actively build and sharpen the project's domain model and shared dictionary as you design and write code. This skill is an active discipline of challenging vague or conflicting terms, testing boundaries with concrete edge-case scenarios, and recording canonical definitions in `<main-repo>/.agent-docs/CONTEXT.md` as soon as they are settled.

## File structure

Most repositories have a single bounded context stored in `<main-repo>/.agent-docs/CONTEXT.md`:

```text
<main-repo>/
└── .agent-docs/
    └── CONTEXT.md
```

If a repository has multiple bounded contexts, `<main-repo>/.agent-docs/CONTEXT-MAP.md` maps each context to its context file under `<main-repo>/.agent-docs/contexts/<context>.md` or the module directory.

Create `.agent-docs/CONTEXT.md` lazily when the first domain term is settled. Ensure `.agent-docs` is ignored in `<main-repo>/.gitignore` and `<main-repo>/.git/info/exclude` following [workspace preparation](../_workflow/workspace.md).

## During the session

### Challenge against the shared dictionary

When the user or existing code uses a term that conflicts with `<main-repo>/.agent-docs/CONTEXT.md`, surface the conflict immediately. State what `.agent-docs/CONTEXT.md` currently defines and ask which meaning should govern.

### Sharpen fuzzy language

When terms are vague or overloaded, propose a precise canonical term and separate distinct concepts. For example, distinguish a billing Customer from an authenticated User instead of calling both an account.

### Stress-test with concrete scenarios

Probe domain relationships with specific edge-case scenarios that force clear boundaries between concepts.

### Cross-reference with code

When someone states how a domain concept behaves, check whether the codebase agrees. Surface any mismatch between code names, behavior, and spoken terminology.

### Update `.agent-docs/CONTEXT.md` inline

When a term is settled, update `<main-repo>/.agent-docs/CONTEXT.md` immediately rather than batching updates for the end of the session. Follow the structure in [context format](references/context-format.md).

Keep `.agent-docs/CONTEXT.md` free of implementation mechanics. It is a shared domain dictionary, not a specification, scratchpad, or task log.
