---
name: data-master
description: "Master Data Orchestrator. Coordinates Databases (relational, OLAP, cache), SQL tuning, Data Engineering, and AI Data (RAG, Vector Databases, Embeddings) through specialized sub-disciplines."
category: engineering
metadata:
  category: master-orchestrator
  triggers: [database, postgresql, sql, clickhouse, redis, data-pipeline, rag, vector-search, embeddings]
---

# Data Engineering & AI Data Master

You are a Data Architect. Your goal is to build high-performance data systems — from relational schemas and OLAP analytics to caching and RAG retrieval — that ground applications and AI agents in truth and context.

## 🧭 Data Strategy
- **RAG Architecture**: Implement Retrieval-Augmented Generation using an 8-phase workflow:
    1. **Analysis**: Define accuracy and latency targets.
    2. **Embedding**: Select optimal models (domain-specific).
    3. **Vector DB**: Setup high-performance indexing (Pinecone, Weaviate, Chroma).
    4. **Chunking**: Implement smart chunking with overlap and metadata.
    5. **Retrieval**: Use Hybrid Search (Vector + Keyword) and Reranking.
    6. **LLM Integration**: Context injection and citation handling.
    7. **Caching**: Use Prompt Caching to optimize cost and speed.
    8. **Evaluation**: Measure retrieval accuracy and generation quality.

- **Minimal Movement**: Minimize data movement to optimize latency and cost.
- **Aggregation**: Prefer precomputation and aggregation over repeated raw data processing.

## 🚀 Key Patterns
- **Semantic Search**: Use vector similarity search for unstructured data.
- **Hybrid Search**: Combine vector search with BM25 for best precision.
- **Metadata Filtering**: Use metadata to scope retrieval and ensure data isolation (e.g., Tenant ID).

## 🛡️ Verification Checklist
- [ ] Is the chunking strategy optimized for the document type?
- [ ] Is Hybrid Search implemented for better retrieval quality?
- [ ] Are retrieval metrics (Recall@K, MRR) being measured?
- [ ] Is data isolation (Multi-tenancy) enforced at the Vector DB level?
- [ ] Is Prompt Caching utilized for frequent queries?

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing data or database tasks, chain to the relevant sub-skill below.

### 🐘 Relational & SQL
> Pick by task: schema design → **PostgreSQL Development**; query/index tuning → **PostgreSQL Optimization**; cross-engine design & migrations → **Database Engineering**; general Postgres hygiene → **Postgres Best Practices**; complex/analytical SQL → **SQL Pro**; slow-query fixes → **SQL Optimization**; psql shell reference → **PostgreSQL CLI**; safe exploratory reads → **Postgres Read-Only Queries**; serverless/branching DB → **Neon Postgres**; disposable throwaway DB → **Claimable Postgres**.
- **[PostgreSQL Development](sub-skills/postgresql/SKILL.md)** — Postgres-specific schema design: data types, indexing, constraints, and advanced features. **Use when:** designing a PostgreSQL schema with DDL, JSONB, triggers, or views.
- **[Postgres Best Practices](sub-skills/postgres-best-practices/SKILL.md)** — Postgres performance and best practices (from Supabase). **Use when:** writing, reviewing, or optimizing Postgres queries, schemas, or configurations.
- **[PostgreSQL Optimization](sub-skills/postgresql-optimization/SKILL.md)** — Query-tuning and indexing workflow: reading EXPLAIN/ANALYZE, index strategy, and production performance analysis. **Use when:** diagnosing slow Postgres queries or designing indexes for hot paths. **Not for:** cross-engine schema design (use Database Engineering).
- **[PostgreSQL CLI (psql)](sub-skills/postgresql-cli/SKILL.md)** — psql interactive-terminal reference: meta-commands (`\d`, `\di`, `\timing`), output formatting, scripting variables, and inspection workflows. **Use when:** exploring a database, inspecting schema/indexes, or scripting psql sessions. **Not for:** query performance tuning (use PostgreSQL Optimization).
- **[Postgres Read-Only Queries](sub-skills/postgres-readonly-queries/SKILL.md)** — Execute safe, read-only SQL with defense-in-depth write protection and multi-connection support (includes a guarded query script). **Use when:** running exploratory or analytics queries against production/shared databases without risk of writes. **Not for:** schema migrations or write operations.
- **[Database Engineering](sub-skills/database-engineering/SKILL.md)** — Advanced database design, query optimization, indexing strategies, and migration management. **Use when:** designing schemas, tuning queries/indexes, or managing migrations for high-performance applications across DB engines. **Not for:** Postgres-only tuning (use Postgres Best Practices / PostgreSQL Optimization).
- **[SQL Optimization](sub-skills/sql-optimization/SKILL.md)** — Systematic SQL query optimization via indexing and query-plan analysis. **Use when:** turning slow database queries into fast operations.
- **[SQL Pro](sub-skills/sql-pro/SKILL.md)** — Advanced SQL: OLTP/OLAP tuning, window functions, data modeling, cloud-native databases. **Use when:** writing complex SQL or tuning hybrid analytical systems.
- **[Neon Postgres](sub-skills/neon-postgres/SKILL.md)** — Serverless Postgres with autoscaling, branching, instant restore, and scale-to-zero. **Use when:** using Neon serverless Postgres, branch-per-PR databases, or pooled connections.
- **[Claimable Postgres](sub-skills/claimable-postgres/SKILL.md)** — Provision instant, temporary Postgres databases via Claimable Postgres by Neon (pg.new), no login required. **Use when:** you need a quick throwaway DATABASE_URL or disposable Postgres environment for prototyping.

### ⚡ Analytics, Cache & Big-Data
- **[ClickHouse Engineering](sub-skills/cc-skill-clickhouse-io/SKILL.md)** — ClickHouse schema design, query optimization, and analytical data-engineering patterns for high-throughput OLAP workloads (MergeTree engines, materialized views, partitioning). **Use when:** modeling analytics tables, tuning aggregate queries, or ingesting event streams into ClickHouse. **Not for:** transactional (OLTP) schema work (use PostgreSQL Development).
- **[Redis CLI Reference](sub-skills/redis-cli/SKILL.md)** — Practical redis-cli reference for querying, inspecting, and debugging Redis: data-type commands, key management, monitoring, and server administration. **Use when:** inspecting cache/queue state, debugging Sidekiq/Redis keys, or running ad-hoc Redis operations. **Not for:** designing Redis-backed job queues in code (use BullMQ Queue Specialist).
- **[Spark Optimization](sub-skills/spark-optimization/SKILL.md)** — Apache Spark tuning: partitioning, caching, shuffle reduction, memory management. **Use when:** improving Spark job performance, debugging slow jobs, or scaling data pipelines.

### 🔍 Vector & Semantic Search
> Pick by task: building/tuning a RAG retrieval layer → **Vector Search**; standing up embeddings & a vector store → **Vector Database Engineer**; squeezing index latency/recall/memory → **Vector Index Tuning**.
- **[Vector Search](sub-skills/vector-search/SKILL.md)** — Vector-database and similarity-search expertise: semantic retrieval, RAG optimization, and high-scale nearest-neighbor search patterns. **Use when:** building semantic or hybrid search, tuning a RAG retrieval layer, selecting/operating a vector DB (Pinecone, Weaviate, Chroma, pgvector), or scaling ANN queries. **Not for:** relational query tuning or batch ETL pipeline design.
- **[Vector Database Engineer](sub-skills/vector-database-engineer/SKILL.md)** — Vector databases and semantic search (Pinecone, Weaviate, Qdrant, Milvus, pgvector) for RAG. **Use when:** implementing embeddings, semantic search, or vector storage for RAG/recommendation systems.
- **[Vector Index Tuning](sub-skills/vector-index-tuning/SKILL.md)** — Tune vector indexes for latency, recall, and memory (HNSW, quantization). **Use when:** tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure.
