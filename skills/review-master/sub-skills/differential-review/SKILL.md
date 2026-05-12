---
name: differential-review
description: "Security-focused code review specializing in Blast Radius analysis and Git history audit."
category: security
metadata:
  triggers: [blast-radius, git-history, security-review, impact-analysis, triage]
---

# Differential Security Review

## 🎯 Objectives
1. Perform risk analysis based on commit history (Git Blame/History).
2. Calculate the Blast Radius for HIGH-RISK changes.
3. Apply Adaptive Review strategies:
    - SMALL (<20 files): DEEP (Review all dependencies).
    - MEDIUM (20-200 files): FOCUSED (1-hop dependencies).
    - LARGE (200+ files): SURGICAL (Critical paths only).

## 🛠️ Execution Workflow
1. **Triage**: Categorize risk levels (HIGH: Auth/Crypto, MEDIUM: Logic, LOW: UI/Docs).
2. **Git Analysis**: Verify if deleted code was a previous security fix.
3. **Blast Radius**: Identify transitive callers. If Blast Radius > 50 ➔ Escalate risk level.
4. **Adversarial Modeling**: Build realistic attack/exploit scenarios.

## 📋 Acceptance Criteria (AC)
- [ ] Report includes Blast Radius analysis for sensitive changes.
- [ ] All identified vulnerabilities include illustrative attack scenarios.
