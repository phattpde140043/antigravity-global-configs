# Example: Golden Response for Database Engineering

Below is a demonstration of how a Senior Database Engineer agent must respond when asked to create a new index or optimize a slow database query.

---

## 🪐 Task Intake & Threat Model

**Request**: "Optimize a query that fetches user transactions filtered by status and created date, and write the migration for it in PostgreSQL."

### 1. Analysis Phase (Query Execution Plan)
*   **Access Pattern**: The primary access query is `SELECT * FROM transactions WHERE status = 'COMPLETED' AND created_at > NOW() - INTERVAL '30 days' ORDER BY created_at DESC;`
*   **Table Size**: 15 Million rows. A Sequential Scan will crash database memory limits and cause query timeouts.
*   **Locking Triage**: Standard `CREATE INDEX` will acquire an `AccessExclusiveLock`, locking out all read and write queries on `transactions` during execution. We MUST use `CREATE INDEX CONCURRENTLY`.

---

## 🏗️ Technical Specification

### 1. Safe Concurrent Migration (SQL)
```sql
-- migration: 20260520_add_idx_transactions_status_created --
-- PostgreSQL concurrent index creation cannot run inside a transaction block.
-- Ensure your migration runner (e.g. Prisma, Flyway) executes this with transaction disabled.

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_transactions_status_created 
ON transactions (status, created_at DESC);
```

### 2. Execution Plan Verification
Before and after running the concurrent migration, we run `EXPLAIN (ANALYZE, BUFFERS)`:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM transactions 
WHERE status = 'COMPLETED' AND created_at > NOW() - INTERVAL '30 days' 
ORDER BY created_at DESC;
```

**Expected Execution Plan Outcome**:
```text
-> Index Scan using idx_transactions_status_created on transactions  (cost=0.43..124.50 rows=450 width=128) (actual time=0.045..1.234 rows=452 loops=1)
     Index Cond: ((status = 'COMPLETED'::text) AND (created_at > (now() - '30 days'::interval)))
     Buffers: shared hit=453
Planning Time: 0.125 ms
Execution Time: 1.350 ms
```
*(Analysis: Sequential Scan eliminated. Query execution time reduced from 4.5 seconds to 1.35 milliseconds, with high cache buffer hits).*

---

## ✅ Post-Generation Self-Review

*   **Convention Check**: Verified. Index named using standard `idx_{table}_{columns}` prefix.
*   **Architecture Check**: Verified. SQL is fully optimized and isolated from business layers.
*   **Idempotency Check**: Verified. Used `IF NOT EXISTS` to ensure repeatable migration safety.
*   **Performance & Security**: Execution locking analyzed. Zero-downtime guaranteed via `CONCURRENTLY`.
*   **Final Judgment**: Production-grade, zero-lock query optimization complete.
