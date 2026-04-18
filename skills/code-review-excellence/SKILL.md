---
name: code-review-excellence
description: "Professional code review culture and process. Focuses on constructive feedback, severity labels, mentoring, and collaborative improvement."
---

# Code Review Excellence

Transform code reviews from gatekeeping to knowledge sharing through constructive feedback and systematic analysis.

## Review Mindset
- **Educational**: Focus on teaching and knowledge transfer.
- **Constructive**: Focus on the code, not the person.
- **Specific**: Provide actionable feedback with specific rationale and examples.

## Resource Chaining (MANDATORY LOOKUP)
When you need deep examples, language-specific patterns (Python/TS), or complex feedback templates, you **MUST** refer to the **[Review Excellence Playbook](file:///Users/macos/.antigravity-global/skills/code-review-excellence/resources/playbook.md)**.

## Severity Labels (MANDATORY)
Use these labels to categorize your feedback clearly:

- 🔴 **[blocking]** - Must fix before merge (security, data loss, logic error).
- 🟡 **[important]** - Should fix, discuss if you disagree.
- 🟢 **[nit]** - Small improvement, not blocking.
- 💡 **[suggestion]** - Alternative approach to consider.
- 📚 **[learning]** - Educational comment, no action required.
- 🎉 **[praise]** - Highlight good work!

## The Question Approach
Instead of stating "this is wrong," ask a question to encourage thinking:
- ❌ "This will fail if the list is empty."
- ✅ "How should this handle an empty list scenario?"

## Refinement Process (4 Phases)

1. **Context Gathering**: Read the task/PR description and linked issues before reading code.
2. **High-Level Review**: Check architecture, design consistency, and scaling concerns.
3. **Line-by-Line Review**: Check logic, security, performance, and naming.
4. **Summary & Verdict**: Provide a clear summary with a final verdict (APPROVE / REQUEST CHANGES).

## Handling Disagreements
When an author disagrees with your feedback:
1. **Seek to Understand**: Ask "Help me understand your approach. What led you to choose this pattern?"
2. **Acknowledge Valid Points**: "That's a good point about [X], I hadn't considered that."
3. **Provide Data**: If still concerned, provide performance benchmarks or documentation links.
4. **Know When to Let Go**: If it's a matter of preference and functional, approve it. Perfection is the enemy of progress.

## Feedback Pattern: The Modified Sandwich
1. **Praise**: Start with what was done well.
2. **Specific Issue**: Describe the concern and its impact.
3. **Helpful Solution**: Suggest a specific fix or alternative.

## Review Checklist
- [ ] Is the feedback balanced (praise + critique)?
- [ ] Are all blocking issues clearly labeled with 🔴?
- [ ] Did I offer to pair if the logic is too complex?
- [ ] Is the tone mentoring and constructive?
