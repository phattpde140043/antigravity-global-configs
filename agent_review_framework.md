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

#### Phase 0: Context Discovery & Threat Triage (`@backend-architect`, `@security-master`)
- **Context Discovery (CRITICAL)**: Before starting any task, the Agent **MUST** check the `knowledge/` directory (e.g., `~/.gemini/antigravity/knowledge/`) to read project context (Briefings, ADRs, Filesystem context).
- **Context Availability Rule**: If no project context is found in the Knowledge Base, the Agent **MUST** ask the User: *"I don't see any context for this project in the knowledge base. Would you like me to perform a scan to ingest the project context?"*
- **Scope**: Map architecture & **Mini-Threat Modeling (STRIDE)** to identify high-risk areas.

## 🛡️ The Zero-Context Isolation Protocol (Anti-Bias)
To ensure the highest architectural integrity and avoid "Confirmation Bias," the Review Council (Phases 6-11) must operate under strict isolation:

1. **Independent Refutation**: Each reviewer (Gates, Jobs, Altman, etc.) performs their critique **autonomously**. They MUST NOT see the critiques of other phases until the final consolidation.
2. **Output-Only Visibility**: Reviewers only see the **Target Artifacts** (Code/Design). They are strictly prohibited from viewing the `PLAN`, reasoning, or conversation history that led to the implementation.
3. **Red-Teaming Mindset**: Each reviewer starts with the assumption that the implementation is **critically flawed**. Their job is not to "approve," but to "refute."
4. **No Consensus Bias**: Do not attempt to harmonize critiques during the process. Conflicting feedback is a signal of healthy architectural tension.

#### Phase 1: Architectural Excellence (`@backend-architect`)
- **Diamond Standard**: Domain Naming, Library-First policy, DDD Compliance.

#### Phase 2: Deep Security & Mitigation Mapping (`@security-master`)
- **Scope**: **STRIDE** analysis, **Blast Radius** analysis, **Control Mapping** (Preventive/Detective/Corrective).
- **AC**: Security-by-Design reaching **Defense-in-Depth** standards.

#### Phase 3: Performance Tuning (`@backend-architect`)
- **AC**: Zero N+1 queries, 100% Caching strategy, Query optimization.

#### Phase 4: Clean Code & AI Slop Scan (`@agent-master`)
- **Hard Limits**: 50/200/3 rule. AI Slop Scan. Readiness Score > 85.

#### Phase 5: Verification & Fix Audit (`@senior-qa`, `@review-master`)
- **Scope**: Root Cause verification & Regression checking.
- **External Audit (Post-Merge)**: For serious launches, run `npx commitshow audit .` to identify deployment-specific gaps (RLS, Webhooks, Idempotency).
- **AC**: Build: PASS, Tests: 100% PASS, commit.show Score > 80.

#### Phase 6: Strategic Critique (`@strategic-critique-gates`)
- **Scope**: Out-of-the-flow systemic refutation. Challenge scalability, chokepoints, and 10-year viability.
- **Goal**: Identify hidden technical debt and "blind spots."

#### Phase 7: Product & Design Critique (`@product-critique-jobs`)
- **Scope**: Visceral, uncompromising review of simplicity, UX flows, and "soul."
- **Goal**: Ensure the experience is "magical." Reject mediocrity.

#### Phase 8: Hyper-Growth & Iteration Critique (`@hyper-growth-critique-altman`)
- **Scope**: High-velocity review of user value and learning speed.
- **Goal**: Maximize "Aha!" moments.

#### Phase 9: Value & Durability Critique (`@value-durability-critique-buffett`)
- **Scope**: Disciplined, defense-first review of moats, simplicity, and safety.
- **Goal**: Ensure long-term durability and a clear "Margin of Safety."

#### Phase 10: Scientific Rigor & Objective-Driven Critique (`@scientific-rigor-critique-lecun`)
- **Scope**: Grounded, scientific refutation of hype and probabilistic guessing.
- **Goal**: Ensure the implementation follows World Models and Objective-Driven logic.

#### Phase 11: Clean Craftsmanship & SOLID Critique (`@clean-craftsmanship-critique-bob`, `@code-simplifier`)
- **Scope**: Professional review of code health, structure, and SOLID integrity.
- **Goal**: Ensure the code is maintainable, clean, and follows Clean Architecture.

## 🔄 PHASE 12: AGENT SELF-CRITIQUE (MANDATORY BEFORE SHIP)
Sau khi thực thi bất kỳ kỹ năng nào, Agent bắt buộc phải tự trả lời 3 câu hỏi sau vào nhật ký ẩn (thought process):
1. Tôi có vi phạm bất kỳ điều khoản nào trong [EXECUTION CONTRACT] của kỹ năng vừa dùng không?
2. Có bước nào trong checklist bị bỏ qua do hạn chế token không?
3. Đầu ra đã khớp 100% với [OUTPUT EXPECTATION] chưa?

---

## 🛠️ Feedback & Reporting Rules (FULL AUTOMATION)

1.  **Automatic Documentation**: Agent **MUST** automatically generate `docs/assessment/` reports.
2.  **Security Reporting**: Must include **STRIDE Analysis** and proposed **Control Mapping**.
3.  **Mandatory "How to Test"**: Every change must include testing instructions.
4.  **Auto-Changelog**: Automatically update `CHANGELOG.md`.
