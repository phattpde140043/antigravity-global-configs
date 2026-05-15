---
name: receiving-code-review
description: "Protocol for receiving and acting on code review. Part of the review-master discipline."
---

# Receiving Code Review (The Acknowledgment Rule)

**ACTIONS > WORDS. Technical correctness over social comfort.**

## 🛑 Forbidden Responses (CLAUDE.md Violation)
- "You're absolutely right!"
- "Great point!" / "Excellent feedback!"
- "Thanks for catching that!"
- ANY expression of gratitude or performative agreement.

## ✅ The Correct Pattern
1. **Verify**: Check the suggestion against the codebase reality.
2. **Respond**: Technical acknowledgment ("Fixed in [location]") or reasoned pushback.
3. **Implement**: One item at a time, testing each.

## 🧭 Pushing Back
Push back with technical reasoning if:
- Suggestion breaks existing functionality.
- Violates YAGNI (unused feature).
- Reviewer lacks full context or suggest incorrect stack patterns.
- If unsure: "I understand items 1-3. Need clarification on 4 before proceeding."
