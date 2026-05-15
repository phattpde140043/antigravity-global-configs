---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code.
---

# Writing Plans

Write comprehensive implementation plans assuming the engineer has zero context and requires strict guidance.

**Core principle:** Decomposition into 2-5 minute tasks + Plan Review Loop.

## Bite-Sized Task Granularity

Each step is one action (2-5 minutes):
- "Write the failing test"
- "Run it to make sure it fails"
- "Implement minimal code"
- "Verify passing"
- "Commit"

## Plan Review Loop

After drafting the plan:
1. **Review**: Dispatch a plan-document-reviewer.
2. **Refine**: If issues are found, fix them and re-review.
3. **Approve**: Only execute once the plan is ✅ Approved.

## Task Structure

```markdown
### Task N: [Component Name]
**Files:** Create/Modify/Test paths.
- [ ] **Step 1: Write the failing test**
- [ ] **Step 2: Run test to verify it fails**
- [ ] **Step 3: Write minimal implementation**
- [ ] **Step 4: Run test to verify it passes**
- [ ] **Step 5: Commit**
```

## Remember

- **Exact paths always**.
- **Complete code in plan**.
- **Exact commands with expected output**.
- **DRY, YAGNI, TDD, frequent commits**.
