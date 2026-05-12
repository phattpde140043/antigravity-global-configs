---
name: vibe-code-auditor
description: "Expert in auditing AI-generated/prototype code, detecting technical debt, and scoring Production Readiness."
category: quality
metadata:
  triggers: [code-audit, ai-slop, technical-debt, production-readiness, hallucination-check]
---

# Vibe Code Auditor

## 🎯 Objectives
1. Detect "Vibe code" (unstructured), and AI hallucinations.
2. Check for Robustness: bare exceptions, missing timeouts.
3. Score Production Readiness (0-100).

## 🛠️ Execution Workflow
1. **Pattern Recognition**: 
    - Search for `eval()`, `exec()`, and bare `except:`.
    - Detect N+1 queries and unbounded loops.
2. **Hallucination Check**: Validate libraries and APIs (ensure no calls to non-existent methods).
3. **Readiness Scoring**:
    - Starting Score: 100 points.
    - Critical Issue: -15 points.
    - High Severity: -8 points.
    - Medium Severity: -3 points.
    - Pervasive patterns: -5 points.

## 📋 Acceptance Criteria (AC)
- [ ] Report includes a Production Readiness Score.
- [ ] No "AI Slop" (redundant comments, placeholders) remains.
- [ ] All API/Library calls are verified to exist in reality.
