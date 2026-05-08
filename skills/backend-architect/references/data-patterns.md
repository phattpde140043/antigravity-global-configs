# Data Architecture & Scaling Patterns

## 📊 Data Partitioning
- **Vertical Partitioning**: Split a large table into smaller tables based on columns (e.g., separate BLOB/Text data).
- **Horizontal Partitioning (Sharding)**: Split data into multiple database instances based on a Shard Key (e.g., `TenantId`, `Geography`).

## 🔄 Read/Write Splitting (CQRS Lite)
- Use a **Primary** node for Writes and multiple **Replica** nodes for Reads.
- Implement **Eventual Consistency** awareness in the UI/API.

## 🧱 Distributed Locking
- Use `Redis` (Redlock) or `Database` locks to ensure a resource is only processed by one worker at a time in a distributed environment.

## 📋 Data Scaling Checklist
- [ ] Is the Shard Key evenly distributed to avoid "Hot Shards"?
- [ ] Is the replication lag monitored?
- [ ] Are indices optimized for the most frequent query patterns?
- [ ] Is sensitive data encrypted at rest and in transit?
