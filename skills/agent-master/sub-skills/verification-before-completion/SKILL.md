---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs.
---

# Verification Before Completion

Claiming work is complete without verification is a failure of the engineering process.

**Core principle:** Evidence before claims, always.

## The Iron Law

> **NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**

## The Gate Function

BEFORE claiming any status:
1. **IDENTIFY**: What command proves this claim?
2. **RUN**: Execute the FULL command (fresh, complete).
3. **READ**: Analyze output, check exit code.
4. **VERIFY**: Does output confirm the claim?
5. **ONLY THEN**: Make the claim with evidence.

## Red Flags

- Using words like "should", "probably", "seems to".
- Expressing satisfaction before verification ("Done!", "Fixed!").
- Relying on partial verification or previous runs.

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification. |
| "I'm confident" | Confidence is not evidence. |
| "Linter passed" | Linter is not a compiler. |
| "Agent said success" | Verify independently. |
