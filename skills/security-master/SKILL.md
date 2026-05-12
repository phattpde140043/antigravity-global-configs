---
name: security-master
description: "Master Security Orchestrator. Coordinates Threat Modeling, Secure Coding, Pentesting, and Cloud Hardening through specialized sub-disciplines."
metadata:
  category: master-orchestrator
  triggers: security-audit, vulnerability-scan, threat-modeling, secure-coding
---

# 🛡️ Security Master Orchestrator

The central authority and dispatcher for all security-related activities. This master skill orchestrates deep-dive specialized sub-disciplines to ensure full-stack security.

---

## 🧭 High-Level Strategy
- **Defense-in-Depth**: Layered security across Design, Code, and Infrastructure.
- **Fail-Closed**: Default system state is always secure/denied.
- **Audit-Ready**: Every change must produce a security assessment report.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing specific security tasks, you **MUST** chain to the following sub-skills for deep expertise:

### 1. Strategy & Threat Modeling (DESIGN Phase)
- For **STRIDE** and Risk Assessment: 
  👉 **[Securities Audit (Tier 2)](sub-skills/securities-audit/SKILL.md)**
- For **User Stories** and Boundary Analysis: 
  👉 **[Security Architecture & Design](sub-skills/security-design/SKILL.md)**

### 2. Secure Coding & Implementation (BUILD Phase)
- For **Backend Security** and Data Handling: 
  👉 **[Backend Security Coder](sub-skills/backend-security-coder/SKILL.md)**
- For **Review Checklists** and Injection prevention: 
  👉 **[Security Review (Checklist)](sub-skills/security-review/SKILL.md)**

### 3. Offensive Security & Pentesting
- For **Scanning, Exploitation, and PoC**: 
  👉 **[Penetration Testing Methodology](sub-skills/penetration-testing/SKILL.md)**

### 4. Cloud & Infrastructure
- For **AWS Hardening** and **SCA (Supply Chain)**: 
  👉 **[Infrastructure Security Reference](sub-skills/infrastructure-security/SKILL.md)**

---

## 🛡️ Coordination Protocol (V8 Framework)
This Orchestrator follows the **[Agent Review Framework](file:///Users/macos/.antigravity-global/agent_review_framework.md)**.
- **Step 1**: Context Discovery (Phase 0).
- **Step 2**: Trigger the relevant Sub-Discipline Chain.
- **Step 3**: Consolidate findings into a Master Security Assessment.

---

## 📋 Master Security Checklist
- [ ] Has the relevant Sub-Discipline been chained?
- [ ] Is there a STRIDE analysis for the Trust Boundaries?
- [ ] Are all "Hard Bans" (Hardcoded secrets, etc.) verified?
- [ ] Is the infrastructure/dependency audit passed?
