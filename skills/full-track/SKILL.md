---
name: full-track
description: Use when the user explicitly requests full-track or a documented development workflow with design and plan approval.
---

# Full track

Read [workflow core](../_workflow/core.md) and follow its phase sequence with track `full`.

Produce a detailed spec, implementation plan, taskboard, proof, and walkthrough. Present the spec and plan together inline in chat for approval before implementation. For follow-up rounds or defect fixes, present the revised plan inline and obtain approval before editing code. Resolve consequential questions beforehand; reuse approval already given in the conversation only within its original scope.

Prefer a worktree, reusing suitable isolation. Implement directly or delegate independent tasks when useful. Require independent review of the completed change, with earlier reviews for risky portions. Use autopilot TDD unless the user requests human-guided testing.

Load each linked procedure when its phase begins. Deliver verified candidate changes and the complete documentation, leaving publishing and the final target-branch commit to the user.
