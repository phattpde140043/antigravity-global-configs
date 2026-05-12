---
name: database-engineering
description: "Advanced database design, query optimization, indexing strategies, and migration management for high-performance applications."
---

# Database Engineering

Master the art of high-performance data storage and retrieval.

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
