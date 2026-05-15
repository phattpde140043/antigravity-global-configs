---
name: subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session.
---

# Subagent-Driven Development

Execute a plan by dispatching a fresh subagent per task, with a two-stage review after each: spec compliance review first, then code quality review.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration.

## When to Use

Use when you have an implementation plan and the tasks are mostly independent. This approach keeps the current session clean and avoids context pollution.

## The Process

1. **Read Plan**: Extract all tasks and context.
2. **Per Task**:
   - **Dispatch Implementer**: Give the subagent the task text and relevant context.
   - **Verification**: The subagent implements, tests, and self-reviews.
   - **Spec Review**: Dispatch a reviewer to confirm the code matches the spec.
   - **Quality Review**: Dispatch a second reviewer for code quality and patterns.
3. **Completion**: Mark task as complete and move to the next.

## Model Selection

- **Mechanical tasks**: Use a fast, cheap model.
- **Integration/Judgment tasks**: Use a standard model.
- **Architecture/Design/Review**: Use the most capable model.

## Advantages

- **No Context Pollution**: Each subagent starts fresh.
- **Strict Quality Gates**: Two-stage review ensures both "What" and "How" are correct.
- **Parallel Safety**: Independent tasks don't conflict.

## Red Flags

- Skipping any review stage.
- Proceeding with open issues.
- Starting implementation on the main branch without isolation (use `using-git-worktrees`).
