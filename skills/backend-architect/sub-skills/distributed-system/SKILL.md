---
name: distributed-system
description: "Design scalable distributed systems using CQRS, event-driven architecture, saga patterns, and eventual consistency. USE WHEN: the request clearly matches the distributed-system domain."
---

# 🌐 Distributed System Design

> [!IMPORTANT]
> ### 📜 EXECUTION CONTRACT (MANDATORY BEHAVIORS)
> 1. **Idempotency Guarantee**: Any event/message consumer MUST implement idempotency tracking (e.g. storing message IDs in an Idempotency Table) before executing updates to prevent duplicate delivery issues.
> 2. **Transactional Integrity (No Dual-Writes)**: NEVER write to a database and publish to a message queue in a single transaction block. ALWAYS use the Transactional Outbox pattern to guarantee event delivery.
> 3. **Resilience Boundaries**: Enforce strict timeouts, retries with exponential backoff + jitter, and circuit breakers (e.g. Polly, Resilience4j) on all synchronous HTTP/gRPC RPC calls.

---
## ⚡ ACTIVATION TRIGGERS
### 1. Input Signals (Kích hoạt khi phát hiện)
- **Files changed/created:** `**/consumers/**`, `**/messages/**`, `**/events/**`, `*Consumer.cs`, `*Handler.ts`
- **Keywords in prompt:** `distributed transaction`, `saga pattern`, `outbox pattern`, `message queue`, `idempotence`, `CQRS`
### 2. Output Expectation (Đầu ra bắt buộc)
- A distributed systems architecture topology or event-driven contract design.
- Failure mode mitigation matrix.

---

## Step 1 — Identify System Type
- Monolith → keep simple
- Distributed → apply patterns

## Step 2 — Choose Architecture Pattern

### CQRS (Command Query Responsibility Segregation)
Separate:
- Write model (commands)
- Read model (queries)

Benefits:
- Scalability
- Performance
Trade-off:
- Complexity
- Eventual consistency

### Event-Driven Architecture
- Use events instead of direct calls

Example:
`UserCreated` → `SendEmail` → `UpdateSearchIndex`

### Saga Pattern (CRITICAL for distributed transactions)
Use when:
- Multiple services involved

Types:
- **Orchestration**: Central controller
- **Choreography**: Event-driven

### Event Sourcing (Optional)
- Store events instead of state
Use when:
- Audit is critical
- History tracking required

## Step 3 — Consistency Model
- Strong consistency → simple systems
- Eventual consistency → distributed systems

## Step 4 — Message Queue Design
Use:
- Azure Service Bus / Kafka / RabbitMQ

Rules:
- Messages MUST be idempotent
- Include tenant context
- Include correlation ID

## Step 5 — Failure Handling
- Retry with backoff
- Dead-letter queue
- Monitoring

## Step 6 — Multi-Tenant Isolation (CRITICAL)
- NEVER mix tenant data
- Include tenant in:
  - events
  - messages
  - queries

## Step 7 — Data Ownership
- Each service owns its DB
- No shared DB across services

## Step 8 — API vs Event Decision
| Use API | Use Event |
|--------|----------|
| Need immediate response | Async processing |
| Strong consistency | Eventual consistency |

## Step 9 — Observability
- Distributed tracing
- Correlation ID
- Logging across services

## Step 10 — Trade-offs
You MUST evaluate:
- Latency vs consistency
- Complexity vs scalability
- Cost vs reliability

## Output Requirement
You MUST:
1. Identify system boundaries
2. Choose architecture pattern
3. Define data flow
4. Handle failure scenarios
5. Explain trade-offs clearly
6. Ensure tenant isolation
7. Ensure observability
