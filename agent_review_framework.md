# 🛡️ Agent Review & Testing Framework (V8 - Threat-Centric Edition)

This document defines the execution flow for Audit, Review, Transformation, and Debugging activities.

---

## 🛑 Classification & Orchestration Rules

1.  **PRODUCTION-READY Mode (Level 3)**: Use `@backend-architect`.
2.  **DEBUGGING Mode (Level 4)**: Use `@systematic-debugging`.
3.  **"Library-First" Rule**: Prioritize standard libraries over manual coding.

---

## 🛡️ Anti-Rationalization (Conflict Map)
Agents MUST NOT bypass the process for any reason.

| Rationalization Pattern | Reality & Strict Rule |
| :--- | :--- |
| "This change is too small/simple" | Simple code can still harbor critical security flaws. Audit is MANDATORY. |
| "I will run the audit later" | Post-hoc audits do not prevent immediate failures. Audit MANDATORY before commit. |
| "System is running fine, no fix needed" | Technical debt accumulation leads to systemic collapse. Refactor MANDATORY. |
| "No suitable library found" | Must search at least 3 libraries thoroughly before manual implementation. |

**No Exceptions:**
- Do not "adapt" to legacy code if it violates the Diamond Standard.
- Multi-tenant isolation steps MUST NOT be skipped for performance reasons.
- Obsolete code must be completely removed, not kept for "reference".

---

## 🟢 Level 1: Passive Hygiene Check (PHC)
**Workflow Fast-track**:
1.  **Step 1: Architecture Limits**: Check File < 200 lines, Function < 50 lines, Nesting < 3 levels.
2.  **Step 2: Coding Style**: Early Returns & Domain-Driven Naming.
3.  **Step 3: Security & Resilience**: Secrets Management & Retry policies.
4.  **Step 4: Conventional Commits**: Validate commit message format.

---

## 🔴 Level 2: Deep System Audit (DSA)

#### Phase 0: Context Discovery & Threat Triage (`@backend-architect`, `@securities-audit`)
- **Context Discovery (CRITICAL)**: Before starting any task, the Agent **MUST** check the `knowledge/` directory (e.g., `~/.gemini/antigravity/knowledge/`) to read project context (Briefings, ADRs, Filesystem context).
- **Context Availability Rule**: If no project context is found in the Knowledge Base, the Agent **MUST** ask the User: *"I don't see any context for this project in the knowledge base. Would you like me to perform a scan to ingest the project context?"*
- **Scope**: Map architecture & **Mini-Threat Modeling (STRIDE)** to identify high-risk areas.

#### Phase 1: Architectural Excellence (`@backend-architect`)
- **Diamond Standard**: Domain Naming, Library-First policy, DDD Compliance.

#### Phase 2: Deep Security & Mitigation Mapping (`@securities-audit`)
- **Scope**: **STRIDE** analysis, **Blast Radius** analysis, **Control Mapping** (Preventive/Detective/Corrective).
- **AC**: Security-by-Design reaching **Defense-in-Depth** standards.

#### Phase 3: Performance Tuning (`@performance-optimization`)
- **AC**: Zero N+1 queries, 100% Caching strategy, Query optimization.

#### Phase 4: Clean Code & AI Slop Scan (`@code-review-excellence`, `@backend-architect`)
- **Hard Limits**: 50/200/3 rule. AI Slop Scan. Readiness Score > 85.

#### Phase 5: Verification & Fix Audit (`@verification-loop`, `@securities-audit`)
- **Scope**: Root Cause verification & Regression checking.
- **AC**: Build: PASS, Tests: 100% PASS.

---

## 🛠️ Feedback & Reporting Rules (FULL AUTOMATION)

1.  **Automatic Documentation**: Agent **MUST** automatically generate `docs/assessment/` reports.
2.  **Security Reporting**: Must include **STRIDE Analysis** and proposed **Control Mapping**.
3.  **Mandatory "How to Test"**: Every change must include testing instructions.
4.  **Auto-Changelog**: Automatically update `CHANGELOG.md`.
