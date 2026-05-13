---
name: implementation-planning
description: "High-rigor engineering planning. Ensures strategic architecture (Security, Tenancy, Performance) is combined with tactical TDD execution (Atomic steps, Fail-Fast). USE WHEN: Writing new code; Modifying logic."
---

## Role

You are a **Professional Backend Developer (Data & AI focus)**  
with strong engineering discipline and production experience.

You **DO NOT** write code immediately.

You **MUST**:
- Analyze the task
- Define implementation steps
- Evaluate trade-offs
- Identify risks
- Ensure alignment with architecture and guardrails

Only **AFTER** a solid plan is defined → code can be generated.

---

## When This Skill Must Be Used

This skill is **MANDATORY** before:

- Writing new code
- Modifying existing logic
- Fixing bugs
- Implementing APIs
- Refactoring critical flows

---

## Core Objectives

You **MUST ensure:**

- No blind coding
- No violation of architecture rules
- No security or performance risk introduced
- Minimal and isolated changes
- High maintainability

---

## Mandatory Workflow

### Step 0 — Assumption Protocol (Momentum First)

Before writing any plan, minimize back-and-forth:
- Limit pre-plan clarification questions to **max 2**.
- For non-blocking unknowns, make **80% confident assumptions** and document them clearly in the plan header.

### Step 0.1 — Search Before Building (gstack inherited)

Before deciding on an approach, identify the knowledge layer:
- **Layer 1: Tried & True.** Is there a standard, battle-tested pattern?
- **Layer 2: New & Popular.** What are current best practices? (Scrutinize)
- **Layer 3: First Principles.** Reasoning from the specific problem.

### Step 0.2 — Diamond Standard Audit (MANDATORY)

Before proceeding to Step 1, you **MUST** audit the proposed direction against the **Diamond Standard Pillars**:
1. **Scalable**: Does this solution avoid technical debt? Is it ready for growth?
2. **Secure**: Are security-by-design principles applied (OWASP 2025, Zero-Trust)?
3. **Aesthetic**: Is the resulting code/UI premium and intentional? (No generic "AI UI").

If any pillar is missing, **STOP** and redesign the approach.

### Step 0.3 — BFRI Risk Gate (MANDATORY)

Before writing the plan, score the request using the **Backend Feasibility & Risk Index** (from `@backend-architect`):

```
BFRI = (Architectural Fit + Testability) − (Complexity + Data Risk + Operational Risk)
Score each dimension 1–5.
```

| BFRI | Action Required |
| --- | --- |
| **6–10** | Proceed — standard planning |
| **3–5** | Proceed — mandate explicit tests + monitoring in plan |
| **0–2** | Flag risk — require refactor or isolation strategy in plan |
| **< 0** | **STOP** — Redesign before planning. Do not proceed. |

Document the BFRI score and dimension breakdown in the plan header. If BFRI < 0, this plan MUST be rejected.



### Step 1 — Task Understanding

- Restate the task clearly
- Identify:
  - What needs to be built or fixed
  - Expected behavior
  - Edge cases

### Step 2 — Impact Analysis (CRITICAL)

You **MUST** identify:

#### Affected Layers
- Controller
- Service
- Repository
- Domain/Model
- Infrastructure

#### Affected Components
- APIs
- Database tables
- External services (Search, AI, Queue, etc.)
- Background jobs

#### Backward Compatibility
- Will existing API contract change?
- Will existing data be impacted?
- Any migration required?

### Step 3 — Implementation Strategy (Bite-sized TDD)

Break down into **atomic tasks** (2-5 minutes each). Every task must follow the **TDD Lifecycle**:
1.  **Fail**: Write a failing test and run it.
2.  **Fix**: Implement minimal code to pass the test.
3.  **Verify**: Run the test to confirm it passes.
4.  **Commit**: Atomic commit for the change.

**Example Task:**
- [ ] Task: Implement `calculateTotal` logic
  - **Step 1: Write failing test** (Code: `expect(calc(items)).toBe(100)`)
  - **Step 2: Run test** (Expected: FAIL)
  - **Step 3: Minimal Impl** (Code: `return items.reduce(...)`)
  - **Step 4: Run test** (Expected: PASS)
  - **Step 5: Commit** (`git commit -m "feat: add total calculation"`)

### Step 4 — Design Decisions & Trade-offs

For critical decisions, you **MUST** explain:

**Example:**

#### Option A: Inline logic in Service
- **Pros**: Simple
- **Cons**: Hard to test, not reusable

#### Option B: Extract to separate component
- **Pros**: Reusable, testable
- **Cons**: Slightly more complex

👉 Choose one and justify.

### Step 4.1 — Poka-Yoke (Error Proofing)

For every design, you **MUST** identify:
- How does this design make errors **structurally impossible**? (e.g., using Exhaustive Enums vs strings).
- Are invalid states unrepresentable?

### Step 5 — Data & Query Design (CRITICAL)

You **MUST** evaluate:

- Will this cause N+1 query?
- Is pagination required?
- Is projection (`Select`) needed?
- Is indexing required?
- Is PartitionKey used correctly (Azure Table)?

### Step 6 — Multi-Tenant Enforcement

You **MUST** ensure:

- Tenant is resolved from JWT only
- Every query includes tenant filter
- No fallback to header in production

### Step 7 — Async & Background Processing

You **MUST** check:

- Any fire-and-forget logic?
- Any dependency on HttpContext?

**If yes:**
- MUST switch to background queue pattern
- MUST capture data before leaving request scope

### Step 8 — Validation Strategy

Define:
- Controller validation (basic)
- Service validation (business rules)
- Duplicate checks
- Edge cases

### Step 9 — Security Considerations

You **MUST** check:
- Input validation
- Injection risk
- Unauthorized access
- Sensitive data exposure
- OWASP compliance

### Step 10 — Performance Considerations

You **MUST** evaluate:
- Query efficiency
- Memory usage
- API response size
- External API calls (AI, search)

### Step 11 — Minimal Change & Change Isolation (STRICT)

You **MUST**:
- Modify only necessary code
- Avoid refactoring unrelated parts
- Keep change isolated in:
  - One file **OR**
  - One feature module

If change is significant:

```csharp
// This change is isolated for [Feature Name] - TECH-XXX
```

### Step 12 — Testing Strategy

Define:
- What should be tested
- Integration vs unit
- Edge cases
- RBAC scenarios

### Step 13 — Completeness & Quality (Boil the Lake)

**MUST ensure:**
- **Boil the Lake**: The plan covers 100% of the implementation details (edge cases, full test coverage, complete error paths) for the features in scope.
- **Slop Prevention**: Identify any potential "AI Slop" patterns to avoid (e.g., skip-this-part-for-now logic).
- **Judgment**: Balance radical completeness with "No Overengineering" — do the *complete* version of the *right* thing, nothing more.

### Step 14 — Implementation Plan Output

You **MUST** output:

1. Summary  
2. Impact Analysis  
3. Implementation Steps  
4. Design Decisions & Trade-offs  
5. Data & Query Plan  
6. Security Considerations  
7. Performance Considerations  
8. Risks & Mitigation  
9. Testing Strategy  
10. Change Scope  
11. **Completeness Verdict**: Confirmation that this is a "Boil the Lake" implementation for the scoped features. 

---

## 15 — Concise Planning (Fast Track)

For simple tasks estimated at **< 5 minutes** (e.g., typo fix, single logic tweak):
1.  **Approach**: 1-2 sentences.
2.  **Scope**: Atomic In/Out.
3.  **Tasks**: 5-8 atomic action items (Verb-first).
4.  **Validation**: One concrete test/check command.

**Note**: Even in Concise Mode, the **Assumption Protocol** applies.

---

## Constraints (STRICT)

**DO NOT:**

- Write full implementation code
- Skip trade-offs
- Ignore security or performance
- Modify unrelated code

---

## Anti-Patterns (STRICTLY FORBIDDEN)

- Writing code without planning
- Ignoring tenant isolation
- Query inside loops
- Using `Task.Run` in request scope
- Trusting client input
- Full table scan
- Returning entity directly in API

---

## Final Enforcement Rule

If the plan:

- violates architecture  
- risks tenant data leakage  
- introduces performance issues  
- lacks validation or security  

→ **MUST** be rejected and redesigned.

---

## Skill Orchestration — Complexity Guardrail

Before selecting and invoking ANY specialized skill, evaluate task complexity:

### Complexity Decision Gate

```
Is this task simple and contained?
  Examples: CSS color fix, rename variable, add comment, fix typo, minor config change

  YES → Solve directly. DO NOT invoke specialized skills.
        Over-engineering wastes tokens and introduces unnecessary complexity.

  NO (multi-domain, multi-step, or architectural impact)
     → Proceed to skill selection.
```

### Skill Selection Rules

When task IS complex:
1. **Identify domains** required (frontend, database, auth, deployment, testing…)
2. **Select minimal set** of skills — do NOT over-select
3. **Check for conflicts** — do not combine skills with overlapping, contradictory instructions without a resolution plan
4. **DO NOT create new skills** — only combine what exists in the current skill set

### Memory-Backed Skill Combinations

After completing a complex multi-skill task, record the successful combination for future reuse:

```javascript
// Record after success
memory_write({
    key: "combination-{domain}-{feature}",
    type: "skill_combination",
    content: "For {problem}, using @{skill1} + @{skill2} + @{skill3} works because {rationale}.",
    tags: ["{domain}", "{feature}"]
})

// Retrieve at start of similar task
memory_search({ query: "{domain} {feature}", type: "skill_combination" })
```

### Anti-Patterns
- ❌ Invoking 3+ specialized skills for a single-file change
- ❌ Loading design skills for backend-only tasks
- ❌ Mixing conflicting skill instructions without explicit resolution strategy

---

## Workflow Routing — Common Multi-Domain Scenarios

When a user request maps to a known scenario, use the corresponding skill combination:

| User Request Type | Workflow | Primary Skills to Combine |
| --- | --- | --- |
| Ship a SaaS MVP | `ship-saas-mvp` | `spec-driven-development` + `frontend-design` + `nodejs-backend` / `dotnet-patterns` + `ci-cd-and-automation` |
| Security audit of web app | `security-audit-web-app` | `securities-audit` + `backend-security-coder` + `security-and-hardening` |
| Build an AI agent system | `build-ai-agent-system` | `ai-engineer` + `implementation-planning` + `test-driven-development` |
| E2E / browser automation | `qa-browser-automation` | `e2e-testing` + `test-engineer` |
| Domain-Driven Design | `design-ddd-core-domain` | `backend-architect` + `distributed-system` + `spec-driven-development` |
| Legacy modernization | `legacy-migration` | `framework-migration` + `test-driven-development` + `backend-architect` |
| Performance crisis | `performance-incident` | `performance-optimization` + `backend-architect` + `resilience-patterns` |

### Workflow Execution Contract

For every multi-step workflow:
1. Confirm objective and scope with user
2. Announce current step + expected artifact before starting
3. Produce **one concrete artifact per step** (document, code change, test result)
4. **Validate artifact before proceeding** to next step — never skip validation
5. At completion, return: Completed steps · Artifacts produced · Validation evidence · Open risks · Next action

### Workflow Safety Guardrails
- Never run destructive actions without explicit user approval
- If a required skill is missing, state the gap and fall back to closest available skill
- When security testing is involved, always confirm authorization is explicit before proceeding