# Implementer Subagent Prompt Template

Use this template when dispatching an implementer subagent for a task.

---

## Prompt

```markdown
# Task: {TASK_NAME}

## Context

You are implementing Task {TASK_NUMBER} of an implementation plan.

**Goal:** {ONE_SENTENCE_GOAL}

**Architecture context:** {2-3 SENTENCES about how this task fits into the larger system}

## Task Definition

{FULL_TASK_TEXT_FROM_PLAN — paste the entire task, not a summary}

## Files You'll Work With

- **Create:** {list of new files}
- **Modify:** {list of existing files with line ranges}
- **Test:** {list of test files}

## Project Conventions

{Any project-specific conventions the implementer needs to know.
For OSP Search E2E tests, include:}

- Use `get_settings()` for all config — never `os.getenv()`
- Use Playwright `APIRequestContext` — never `requests` library
- Use `data=` for POST payloads — never `json=`
- Apply both scope + priority markers to every test
- Follow `test_<scope>_<number>_<description>` naming

## Constraints

- Do NOT modify files outside the listed scope
- Do NOT refactor unrelated code
- Follow TDD: write failing test first, then implement
- Commit after each meaningful change

## Expected Output

Report your status as one of:

- **DONE** — Task complete, tests pass, committed
- **DONE_WITH_CONCERNS** — Complete but flagging doubts (explain)
- **NEEDS_CONTEXT** — Cannot proceed without specific information (list what you need)
- **BLOCKED** — Cannot complete the task (explain why)

Include:
1. Summary of what you implemented
2. Files created/modified
3. Test results (pass/fail count)
4. Any concerns or observations
```

---

## Usage Notes

- **Paste the full task text** — don't summarize. The implementer has no prior context.
- **Include project conventions** — the implementer doesn't know your codebase.
- **Specify constraints** — prevent scope creep.
- **Use DONE_WITH_CONCERNS** for the implementer to flag architectural doubts without blocking.
