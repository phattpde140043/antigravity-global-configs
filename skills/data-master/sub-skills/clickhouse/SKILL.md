---
name: clickhouse-patterns
description: "Advanced ClickHouse database patterns, MergeTree engines, and query optimization for high-performance analytical workloads."
---

# ClickHouse Analytics Patterns

Master high-performance OLAP with ClickHouse-specific storage engines and query patterns.

## 🏗️ Storage Engine Selection
- **MergeTree**: Standard engine for high-volume analytics.
- **ReplacingMergeTree**: Automatic deduplication based on primary key.
- **AggregatingMergeTree**: Incremental pre-aggregation for real-time dashboards.

## ⚡ Query Optimization
- **Primary Key Selection**: Put most frequently filtered, low-to-medium cardinality columns first.
- **Aggregation Heuristics**: Use `sumMerge`, `uniqMerge`, and `quantile` (percentiles) for extreme efficiency.
- **Avoid `SELECT *`**: Always specify columns to leverage columnar storage.
- **Materialized Views**: Use for real-time background aggregations instead of expensive runtime grouping.

## 📥 Ingestion Best Practices
- **Batching**: Always insert in large batches (min 1,000+ rows). Individual inserts are an anti-pattern.
- **Buffer Engine**: Use for small, high-frequency inserts if batching at the application layer is not possible.

## 📋 Verification Checklist
- [ ] Is the correct MergeTree engine selected for the use case?
- [ ] Are the primary and ordering keys optimized for common filters?
- [ ] Are materialized views used for repeated heavy aggregations?
- [ ] Is the ingestion strategy using batching?
- [ ] Are ClickHouse-specific functions used (e.g., `uniq`, `quantile`)?
