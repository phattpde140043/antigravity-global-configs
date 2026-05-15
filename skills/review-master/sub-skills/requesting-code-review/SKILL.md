---
name: requesting-code-review
description: "Protocol for requesting code review. Part of the review-master discipline."
---

# Requesting Code Review

**Systematic delegation for quality assurance.**

## 🔄 The Protocol
1. **Scope Identification**: Determine if the change is a major feature, security-critical, or architectural.
2. **Review Dispatch**: Use a dedicated subagent or parallel session for the review.
3. **Template Usage**: Provide the reviewer with a clear context and the required checklists (Security, .NET, JS, etc.).
4. **Mandatory Gating**: Major features MUST be approved by a `review-master` before merging.

## 📝 Review Request Template
- **Context**: [Summary of changes and goal]
- **Risks**: [Identified risks during implementation]
- **Tests**: [Verification evidence/results]
- **Specific Focus**: [Areas needing extra attention]

## 🎯 Target Reviewers
- **Security Audit**: `security-auditor`
- **Architecture Check**: `backend-architect`
- **Standard PR**: `code-reviewer`
