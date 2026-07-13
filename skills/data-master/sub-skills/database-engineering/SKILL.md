---
name: database-engineering
description: "Advanced database design, query optimization, indexing strategies, and migration management for high-performance applications."
---

# 🗄️ Database Engineering

> [!IMPORTANT]
> ### 📜 EXECUTION CONTRACT (MANDATORY BEHAVIORS)
> 1. **Index Optimization**: ALWAYS run `EXPLAIN (ANALYZE, BUFFERS)` on complex queries. Ensure every join and search column uses appropriate index types (B-Tree, GIN) and eliminate Sequential Scans on tables larger than 10k rows.
> 2. **Zero-Downtime Migrations**: NEVER execute blocking/exclusive table-locking queries on high-traffic databases. ALWAYS run `CREATE INDEX CONCURRENTLY` in PostgreSQL and use multi-step backfills for defaults.
> 3. **Connection Efficiency**: ALWAYS use robust connection pooling (e.g., PgBouncer, HikariCP) and enforce strict statement timeouts to prevent connection starvation.

---
## ⚡ ACTIVATION TRIGGERS
### 1. Input Signals (Kích hoạt khi phát hiện)
- **Files changed/created:** `**/migrations/**`, `*.sql`, `**/repositories/**`, `PrismaService.ts`, `DbContext.cs`
- **Keywords in prompt:** `database index`, `query tuning`, `migration locking`, `explain analyze`, `connection pool`, `ACID`
### 2. Output Expectation (Đầu ra bắt buộc)
- An optimized database schema or index tuning strategy.
- Complete execution plan analysis report.

---

## 🏗️ Design & Architecture
- **Schema Design**: Normalization vs. Denormalization (intentional trade-offs).
- **Indexing**: B-Tree, GIN, GiST, and Brin indexes. Use covering indexes to avoid heap fetches.
- **Partitioning**: Range, List, and Hash partitioning for large datasets.
- **Constraints**: Enforce data integrity with Foreign Keys, Unique constraints, and Check constraints.

## ⚡ Query Optimization
- **Execution Plans**: Use `EXPLAIN ANALYZE` to identify bottlenecks (Seq Scan vs. Index Scan).
- **N+1 Prevention**: Use eager loading, JOINs, or window functions.
- **Connection Pooling**: Use `PgBouncer` or `HikariCP` to manage connection overhead.

## 🔄 Migration Management
- **Safe Migrations**: Avoid blocking operations (e.g., adding columns with default values in older Postgres versions).
- **Versioning**: Use Flyway, Liquibase, or Alembic for version-controlled schema changes.
- **Migration Observability**: Track success, duration, and row counts for all schema transitions.

## 📋 Verification Checklist
- [ ] Are all queries using appropriate indexes?
- [ ] Is the schema optimized for the primary access patterns?
- [ ] Are foreign keys and constraints protecting data integrity?
- [ ] Have migrations been tested for performance impact on large tables?
- [ ] Is connection pooling correctly configured?
