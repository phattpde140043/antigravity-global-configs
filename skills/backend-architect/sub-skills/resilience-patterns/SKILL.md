---
name: resilience-patterns
description: "Apply resilience patterns (retry, circuit breaker, timeout, idempotency, outbox) to ensure system reliability and fault tolerance in distributed environments."
---



# Resilience Patterns (Tier 2)
Ensure system stability, fault tolerance, and graceful degradation in distributed environments.

## ⚡ Quick References (MANDATORY)
- **[Fault Tolerance](references/fault-tolerance.md)**: Retry, Exponential Backoff, and Circuit Breaker.
- **[Caching & Idempotency](references/caching-idempotency.md)**: Cache-Aside strategies, Idempotency Keys, and Outbox Pattern.

---

# When to Use
- Calling external APIs (OpenAI, Search API, Payment Gateway).
- Handling Background Jobs or Async Workflows.
- Designing Distributed Systems.

---

# 🛠️ Operating Pipeline


### Step 1 — Failure Mode Analysis
Identify: What can fail? What is the impact? (Data loss? Duplication? System collapse?)

### Step 2 — Pattern Selection
Based on the analysis, choose the appropriate design pattern from the reference files above.

### Step 3 — Async & Background Safety
- **NEVER** use `Task.Run(() => DoWork());` for fire-and-forget tasks in Web APIs.
- **USE**: `IHostedService` or `BackgroundService`.
- Refer to safety code samples in `references/fault-tolerance.md`.

### Step 4 — Multi-Tenant Safety & Testing
- Ensure Retries do not leak tenant context.
- Use **Chaos Testing** (error injection) to verify recovery capability.

### Step 5 — Observability
Log Circuit Breaker states, Retry attempts, and propagate TraceID throughout the flow.

---

# 🛡️ Idempotency Strategy (MANDATORY)
Every mutation operation (Create/Update/Delete) must be safe to retry.

1. **Idempotency Keys**: Use a unique client-generated key (e.g., `X-Idempotency-Key`) for critical operations.
2. **Get-or-Create Pattern**: Before creating a resource, check if it already exists with the same parameters.
3. **Handling Conflict (409)**: 
   - If a `Conflict` occurs during a retry, the system should verify if the existing resource matches the requested state.
   - **Action**: Catch `EntityConflictException` (or similar), log the event, and return the existing resource as a success instead of failing the workflow.
4. **State Transitions**: Ensure state machine transitions are unidirectional and safe to repeat (e.g., `UpdateStatusToActive` should do nothing if already `Active`).

**Impact**: This prevents broken onboarding flows and "zombie" resources caused by network retries.
