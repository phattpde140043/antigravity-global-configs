---
name: cqrs-pattern
description: "Expert in Command Query Responsibility Segregation (CQRS). Focuses on separating read and write models to optimize performance, scalability, and security."
---

# CQRS Implementation Pattern

> [!IMPORTANT]
> ### 📜 EXECUTION CONTRACT (MANDATORY BEHAVIORS)
> 1. ALWAYS prioritize production-ready best practices for cqrs-pattern.
> 2. NEVER introduce raw, unvalidated patterns under cqrs-pattern context.
> 3. ALWAYS write clean, self-documenting code with comprehensive error bounds.

---
## ⚡ ACTIVATION TRIGGERS
### 1. Input Signals (Kích hoạt khi phát hiện)
- **Files changed/created:** `**/sub-skills/cqrs-pattern/**`
- **Keywords in prompt:** `cqrs pattern`
### 2. Output Expectation (Đầu ra bắt buộc)
- Domain-optimized implementation following clean multi-layer standards.

---

Master the separation of concerns between state-changing operations (Commands) and data-retrieval operations (Queries).

## 🏗️ Core Architecture
- **Command Model**: Optimized for write operations, business logic, and consistency. Usually maps to the Domain Model.
- **Query Model**: Optimized for read operations, UI requirements, and high-performance reporting. Often uses flattened schemas or materialized views.
- **Synchronization**: Use **Projections** (Projectors) to update the read model when command events occur.

## 🚀 Implementation Strategies
- **Synchronous**: Read model is updated in the same transaction as the command (Strong consistency).
- **Asynchronous**: Command publishes an event; a background worker updates the read model (Eventual consistency).
- **Data Stores**: You can use different databases for Read (e.g., Elasticsearch/Redis) and Write (e.g., PostgreSQL).

## 🛡️ When to Use
- Complex domains where the read logic differs significantly from the write logic.
- Systems needing to scale reads independently from writes.
- When query performance is critical and standard JOINs are too slow.

## 📋 Verification Checklist
- [ ] Are the Command and Query models clearly separated?
- [ ] Is the Query model optimized for specific UI/Reporting needs (denormalized)?
- [ ] Is the consistency model (Strong vs Eventual) documented and appropriate?
- [ ] Are projections handling failure scenarios (retries, re-indexing)?
- [ ] Is the Command model focused on business rules and data integrity?
