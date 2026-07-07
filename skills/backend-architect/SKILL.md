---
name: backend-architect
description: "Master Architecture Orchestrator. Coordinates System Design, Microservices, and Structural Excellence through specialized sub-disciplines."
category: engineering
metadata:
  category: master-orchestrator
  triggers: [api-design, microservices, dotnet, fastapi, system-transformation, architecture-design]
---

# 🏗️ Backend Architect Orchestrator

The strategic lead for scalable and resilient systems. This master skill coordinates structural analysis and architectural design to ensure systemic integrity.

---

## 🧭 Architectural Strategy
- **Type-Safe First**: Prioritize **tRPC**, **GraphQL**, or **Prisma** (Type-safe ORM).
- **Microservices Patterns**: Design clear **Service Boundaries** (Bounded Contexts). Implement **Saga** for data consistency, **CQRS** for performance, and **API Gateways** for secure entry.
- **Polyglot Mastery**: Expertise in Java, Javascript/TypeScript, and Kotlin.
- **Workflow Orchestration**: Implement durable execution using **Inngest** or **Temporal**.
- **Edge Computing**: Optimize for **Cloudflare Workers** and global Edge functions.
- **Privacy by Design**: Implement security and tenant isolation at the architectural level.
- **Fail-Safe**: Build for redundancy and self-healing.
- **Simplicity**: Avoid over-engineering; maintain the Diamond Standard.

---

## 🔗 Sub-Discipline Chain (MANDATORY DELEGATION)

When performing architectural tasks, you **MUST** chain to the following sub-skills. Navigate the sub-skills in the sequential order defined below to ensure structured design:

### 🔄 Sequential Sub-Skill Pipeline
```
[Software Architecture] ──→ [Architecture Design] ──→ [System Architecture] ──→ [API Design] ──→ [Performance Optimization]
```


### 1. High-Level Design & Strategy
- **[Software Architecture Excellence](sub-skills/software-architecture/SKILL.md)** — Clean Architecture, DDD, and whole-system structural integrity. **Use when:** establishing architectural style, layering, and systemic integrity for a new or evolving system. **Not for:** framework-specific implementation or code-level review.
- **[Architecture Design](sub-skills/architecture-design/SKILL.md)** — Scalable, secure, multi-tenant backend architecture with data and AI considerations. **Use when:** designing a new system or feature, or making high-level technical decisions. **Not for:** tasks better served by a more specific skill.
- **[Domain Driven Design](sub-skills/domain-driven-design/SKILL.md)** — Strategic and tactical DDD: bounded contexts, ubiquitous language, and complex domain modeling. **Use when:** modeling a complex business domain, mapping bounded contexts, or aligning software with business language.
- **[Distributed System](sub-skills/distributed-system/SKILL.md)** — Scalable distributed systems via CQRS, event-driven architecture, sagas, and eventual consistency. **Use when:** designing systems that span services with scalability and eventual-consistency needs.
- **[System Architecture](sub-skills/system-architecture/SKILL.md)** — End-to-end system, REST/GraphQL API, and tech-stack (.NET/FastAPI) design decisions. **Use when:** designing new systems, refactoring architecture, or making backend API/architecture decisions. **Not for:** pre-implementation brainstorming, writing plans, or code review.
- **[Blockchain Developer](sub-skills/blockchain-developer/SKILL.md)** — Web3 apps, smart contracts, and decentralized systems (DeFi, NFTs, DAOs). **Use when:** building EVM/Solidity or Solana Rust contracts, DeFi protocols, NFT platforms, or enterprise blockchain integrations.
- **[SaaS Multi-Tenant Architecture](sub-skills/saas-multi-tenant/SKILL.md)** — Multi-tenant isolation with row-level security and tenant-scoped queries. **Use when:** isolating tenants or choosing database-per-tenant, schema-per-tenant, or row-level tenancy in PostgreSQL/TypeScript.
- **[Saga Orchestration](sub-skills/saga-orchestration/SKILL.md)** — Distributed transactions and long-running processes via orchestration/choreography with compensating actions. **Use when:** coordinating multi-service transactions that need rollback or compensation.
- **[C4 Modeling](sub-skills/c4-modeling/SKILL.md)** — C4 model architecture diagramming (Context, Container, Component, Code) in Mermaid. **Use when:** visualizing system architecture, container/component boundaries, or deployment topology as diagrams. **Not for:** making the architectural decisions themselves (use System Architecture).
- **[CQRS Pattern](sub-skills/cqrs-pattern/SKILL.md)** — Command Query Responsibility Segregation: separating read and write models for performance, scalability, and security. **Use when:** read and write workloads diverge and need independent scaling, optimized read models, or event-sourcing alignment. **Not for:** simple CRUD where a single model suffices.

### 2. Specialized Frameworks & Platforms
- **[Dotnet Patterns](sub-skills/dotnet-patterns/SKILL.md)** — Idiomatic C#/.NET, dependency injection, and async patterns. **Use when:** building or reviewing C#/.NET services. **Not for:** non-.NET stacks.
- **[Avalonia Layout Zafiro](sub-skills/avalonia-layout-zafiro/SKILL.md)** — Avalonia UI layout with Zafiro (shared styles, generic components, EdgePanel). **Use when:** building Avalonia XAML layouts with Zafiro while avoiding XAML redundancy.
- **[Avalonia ViewModels Zafiro](sub-skills/avalonia-viewmodels-zafiro/SKILL.md)** — ViewModel and Wizard patterns with Zafiro and ReactiveUI. **Use when:** creating Avalonia ViewModels, SlimWizard flows, or ReactiveUI commands.
- **[Avalonia Zafiro Development](sub-skills/avalonia-zafiro-development/SKILL.md)** — Conventions and behavioral rules for Avalonia + Zafiro. **Use when:** enforcing Zafiro naming standards or DynamicData pipelines across an Avalonia app.
- **[Nodejs Backend](sub-skills/nodejs-backend/SKILL.md)** — Production Node/Express + TypeScript layered architecture (Zod, Prisma, Sentry). **Use when:** building or reviewing Node.js/Express microservices, APIs, jobs, or middleware. **Not for:** C#/.NET services or frontend React/Next.js.
- **[Python Backend](sub-skills/python-backend/SKILL.md)** — Async-first APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. **Use when:** building async FastAPI microservices or modern Python APIs.
- **[WordPress Architect](sub-skills/wordpress-architect/SKILL.md)** — High-fidelity React/HTML/Next.js to WordPress conversion with ACF mapping and technical SEO. **Use when:** porting a codebase or design to WordPress with pixel-perfect UI and dynamic ACF fields.
- **[Python Best Practices](sub-skills/python-best-practices/SKILL.md)** — Modern Python development patterns and conventions. **Use when:** establishing idiomatic Python style or project conventions. **Not for:** FastAPI-specific backend work (use Python Backend).
- **[BullMQ Queue Specialist](sub-skills/bullmq-specialist/SKILL.md)** — Redis-backed BullMQ job queues and reliable async execution in Node/TS. **Use when:** adding background jobs, scheduled/repeatable jobs, or worker processing on Redis.
- **[Bun Development](sub-skills/bun-development/SKILL.md)** — Fast JS/TS development on the Bun runtime. **Use when:** setting up a Bun server, bundling dependencies, or adopting Bun's toolchain.
- **[Salesforce Development](sub-skills/salesforce-development/SKILL.md)** — Salesforce platform development with Apex, LWC, and SOQL. **Use when:** building Salesforce Apex classes, LWC components, or SOQL queries.
- **[Sankhya BI Dashboards](sub-skills/sankhya-dashboard/SKILL.md)** — Sankhya ERP dashboards in HTML/JSP/Java/SQL. **Use when:** creating or fixing Sankhya BI dashboard widgets with JSP/JSTL and SQL parameter protection.
- **[Scala Pro](sub-skills/scala-pro/SKILL.md)** — Enterprise Scala: functional programming, Scala 3, Akka/Pekko, Spark, ZIO/Cats. **Use when:** writing functional Scala, reactive systems, or big-data Scala pipelines.
- **[Pakistan Payments](sub-skills/pakistan-payments/SKILL.md)** — Pakistani payment rails (JazzCash, Easypaisa, PSPs, optional Raast) for PKR billing. **Use when:** integrating local Pakistani gateways with webhook reliability and reconciliation.
- **[Payment Integration](sub-skills/payment-integration/SKILL.md)** — Stripe/PayPal/processor integration: checkout, subscriptions, webhooks, PCI compliance. **Use when:** implementing payments, billing, or subscription features generally.
- **[PayPal Integration](sub-skills/paypal-integration/SKILL.md)** — PayPal Express Checkout, IPN handling, recurring billing, and refunds. **Use when:** integrating PayPal specifically, including SDK checkout and webhook idempotency. **Not for:** non-PayPal processors (use Payment Integration).
- **[Plaid Fintech](sub-skills/plaid-fintech/SKILL.md)** — Plaid API integration: Link token, transactions, and balance synchronization. **Use when:** connecting bank accounts and syncing transactions/balances via Plaid.
- **[PHP Pro](sub-skills/php-pro/SKILL.md)** — Idiomatic PHP with generators/SPL, Laravel architecture, modern OOP, and security. **Use when:** writing or refactoring PHP/Laravel with modern patterns.
- **[Postgres Best Practices](sub-skills/postgres-best-practices/SKILL.md)** — Postgres performance and best practices (from Supabase). **Use when:** writing, reviewing, or optimizing Postgres queries, schemas, or configurations.
- **[PostgreSQL Development](sub-skills/postgresql/SKILL.md)** — Postgres-specific schema design: data types, indexing, constraints, and advanced features. **Use when:** designing a PostgreSQL schema with DDL, JSONB, triggers, or views.
- **[Database Engineering](sub-skills/database-engineering/SKILL.md)** — Advanced database design, query optimization, indexing strategies, and migration management. **Use when:** designing schemas, tuning queries/indexes, or managing migrations for high-performance applications across DB engines. **Not for:** Postgres-only tuning (use Postgres Best Practices / PostgreSQL Development).
- **[Spark Optimization](sub-skills/spark-optimization/SKILL.md)** — Apache Spark tuning: partitioning, caching, shuffle reduction, memory management. **Use when:** improving Spark job performance, debugging slow jobs, or scaling data pipelines.
- **[SQL Optimization](sub-skills/sql-optimization/SKILL.md)** — Systematic SQL query optimization via indexing and query-plan analysis. **Use when:** turning slow database queries into fast operations.
- **[SQL Pro](sub-skills/sql-pro/SKILL.md)** — Advanced SQL: OLTP/OLAP tuning, window functions, data modeling, cloud-native databases. **Use when:** writing complex SQL or tuning hybrid analytical systems.
- **[Claimable Postgres](sub-skills/claimable-postgres/SKILL.md)** — Provision instant, temporary Postgres databases via Claimable Postgres by Neon (pg.new), no login required. **Use when:** you need a quick throwaway DATABASE_URL or disposable Postgres environment for prototyping.
- **[Ruby Pro](sub-skills/ruby-pro/SKILL.md)** — Idiomatic Ruby with metaprogramming, Rails patterns, gem development, and testing. **Use when:** writing Ruby/Rails with ActiveRecord optimization or building gems.
- **[Recsys Pipeline](sub-skills/recsys-pipeline/SKILL.md)** — Composable recommendation/ranking/feed pipelines via Source→Hydrator→Filter→Scorer→Selector→SideEffect. **Use when:** designing recommendation, ranking, or feed pipelines with candidate retrieval and scoring.

### 🦀 Rust Systems Engineering & Robius
- **[Rust Pro](sub-skills/rust/pro/SKILL.md)** — Modern Rust 1.75+ with async patterns, advanced type-system features, and production systems programming. **Use when:** writing idiomatic Rust with lifetimes, trait bounds, async, and cargo tooling.
- **[Rust Project Scaffolding](sub-skills/rust/systems-programming/SKILL.md)** — Scaffolds production-ready Rust projects: complete structures, cargo tooling, module organization, testing. **Use when:** bootstrapping a new Rust application's architecture and module layout.
- **[Rust Async Patterns](sub-skills/rust/async-patterns/SKILL.md)** — Rust async with Tokio, async traits, error handling, and concurrent patterns. **Use when:** building async Rust applications, implementing concurrent systems, or debugging async code.
- **[Robius App Architecture](sub-skills/rust/robius/app-architecture/SKILL.md)** — Makepad/Robius app structure with async/Tokio backend integration (SignalToUI, Cx::post_action, worker tasks). **Use when:** structuring a Makepad application with an async backend.
- **[Robius Event Action](sub-skills/rust/robius/event-action/SKILL.md)** — Custom actions and event handling in Makepad (MatchEvent, cx.widget_action, handle_actions). **Use when:** implementing custom actions, widget events, or widget-to-widget communication in Makepad.
- **[Robius Matrix Integration](sub-skills/rust/robius/matrix-integration/SKILL.md)** — Matrix SDK integration with Makepad (sliding sync, timeline subscriptions). **Use when:** building a Matrix chat client or wiring matrix-sdk async operations into a Makepad UI.
- **[Robius State Management](sub-skills/rust/robius/state-management/SKILL.md)** — Makepad app state and persistence (AppState, Scope::with_data, serde). **Use when:** designing app state structure, persisting state across sessions, or theme switching.
- **[Robius Widget Patterns](sub-skills/rust/robius/widget-patterns/SKILL.md)** — Reusable Makepad widgets via live_design (apply_over, modal, collapsible, view caching). **Use when:** designing reusable Makepad widgets, component APIs, or dynamic styling.

### 📈 Quantitative Finance & Risk Analysis
- **[Risk Metrics Calculation](sub-skills/finance/risk-metrics-calculation/SKILL.md)** — Portfolio risk metrics: VaR, CVaR, Sharpe, Sortino, and drawdown analysis. **Use when:** measuring portfolio risk, implementing risk limits, or building risk monitoring systems.

### 💾 Vector Databases & Advanced Storage
- **[Vector Database Engineer](sub-skills/vector-database-engineer/SKILL.md)** — Vector databases and semantic search (Pinecone, Weaviate, Qdrant, Milvus, pgvector) for RAG. **Use when:** implementing embeddings, semantic search, or vector storage for RAG/recommendation systems.
- **[Vector Index Tuning](sub-skills/vector-index-tuning/SKILL.md)** — Tune vector indexes for latency, recall, and memory (HNSW, quantization). **Use when:** tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure.
- **[VideoDB Core](sub-skills/videodb/SKILL.md)** — Video/audio perception, indexing, and editing: ingest, build visual/spoken indexes, search with timestamps, edit timelines. **Use when:** ingesting media, building temporal indexes, or editing timelines/overlays/subtitles.
- **[VideoDB Client Skills](sub-skills/videodb-skills/SKILL.md)** — Upload, stream, search, edit, transcribe, and generate media via the VideoDB SDK. **Use when:** using the VideoDB SDK to query temporal indices or run visual search pipelines.
- **[Vexor Semantic Search Core](sub-skills/vexor/SKILL.md)** — Vector-powered CLI for semantic file search, with a Claude/Codex skill. **Use when:** setting up or using Vexor to semantically search files in a repository.
- **[Vexor CLI](sub-skills/vexor-cli/SKILL.md)** — Semantic file discovery via the `vexor` command. **Use when:** locating where something is implemented/loaded/defined in a medium or large repo, or when a file's location is unclear. **Not for:** manual browsing of small, known directories.
- **[Neon Postgres](sub-skills/neon-postgres/SKILL.md)** — Serverless Postgres with autoscaling, branching, instant restore, and scale-to-zero. **Use when:** using Neon serverless Postgres, branch-per-PR databases, or pooled connections.
- **[Upstash QStash](sub-skills/qstash/SKILL.md)** — Serverless HTTP message queue with schedules and retries. **Use when:** adding HTTP-based serverless queuing, scheduled triggers, or retry backoff without managing infra.
- **[Python uv Package Manager](sub-skills/python/uv-package-manager/SKILL.md)** — Extremely fast Python package installer/resolver (uv) for project and dependency management. **Use when:** managing Python dependencies, lockfiles, or virtual environments with uv.

### 🔄 Distributed Workflow Orchestration (Temporal)
- **[Temporal Go](sub-skills/temporal/golang/SKILL.md)** — Durable distributed systems with the Temporal Go SDK (deterministic workflows, mTLS workers). **Use when:** building Temporal workflows/activities in Go with signals and queries.
- **[Temporal Python Core](sub-skills/temporal/python/core/SKILL.md)** — Temporal orchestration with the Python SDK: durable workflows, saga patterns, distributed transactions. **Use when:** implementing async Temporal workflows/activities in Python.
- **[Temporal Python Testing](sub-skills/temporal/python/testing/SKILL.md)** — Testing Temporal Python workflows with pytest and time-skipping environments. **Use when:** writing tests or mocks for Temporal Python workflows.

### 3. API & Communication
- **[API Design](sub-skills/api-design/SKILL.md)** — Stable REST/GraphQL endpoint and interface/type-contract design. **Use when:** designing endpoints, resource naming, pagination, versioning, or module/frontend-backend contracts.
- **[X API](sub-skills/x-api/SKILL.md)** — X/Twitter API integration: posting tweets/threads, reading timelines, OAuth, rate limits. **Use when:** posting or reading X/Twitter content programmatically. **Not for:** content strategy or cross-platform distribution.
- **[Crosspost](sub-skills/crosspost/SKILL.md)** — Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. **Use when:** publishing one idea as platform-specific versions across multiple networks. **Not for:** deriving a voice profile or fixing weak source material.

### 4. Resilience & Evolution
- **[Resilience Patterns](sub-skills/resilience-patterns/SKILL.md)** — Retry, circuit breaker, timeout, idempotency, and outbox patterns. **Use when:** hardening distributed calls for fault tolerance and reliability.
- **[Error Resilience](sub-skills/error-resilience/SKILL.md)** — Observability, error tracking, and system recovery patterns. **Use when:** adding error tracking, observability, or recovery around failures.
- **[Performance Optimization](sub-skills/performance-optimization/SKILL.md)** — Fix bottlenecks in code, databases, and APIs (caching, indexing, Core Web Vitals). **Use when:** diagnosing and fixing concrete performance bottlenecks.
- **[Performance Engineering](sub-skills/performance-engineering/SKILL.md)** — Performance engineering with observability, load testing, and capacity planning. **Use when:** isolating bottlenecks from metrics/traces, designing load tests, or planning scalability. **Not for:** feature work with no performance goals or no access to metrics.
- **[Performance Optimizer](sub-skills/performance-optimizer/SKILL.md)** — Find and fix bottlenecks with before/after measurement to prove improvement. **Use when:** you need measured evidence of an optimization in code, databases, or APIs.
- **[Performance Profiling](sub-skills/performance-profiling/SKILL.md)** — Profiling principles: measurement, analysis, and optimization (flame graphs, traces). **Use when:** profiling to locate CPU or memory hotspots.
- **[Speed Reader (RSVP)](sub-skills/performance-optimization/speed/SKILL.md)** — Launches an RSVP/Spritz word-by-word speed reader for text. **Use when:** the user wants to speed-read provided text or a prior response word-by-word. **Not for:** system latency/throughput optimization — despite its path, this is a reading aid, not a performance tool.
- **[Durable Execution](sub-skills/durable-execution/SKILL.md)** — Fault-tolerant durable workflows with DBOS that complete despite failures/reboots. **Use when:** ensuring long-running logic survives crashes, restarts, or network issues.
- **[Framework Migration](sub-skills/framework-migration/SKILL.md)** — Legacy modernization (Strangler Fig), framework/language migrations, and dependency upgrades. **Use when:** migrating to a new framework/language/platform, upgrading major dependencies, or modernizing legacy systems. **Not for:** greenfield development or minor bug fixes.
- **[MCP Server Patterns](sub-skills/mcp-server-patterns/SKILL.md)** — Build MCP servers with the Node/TypeScript SDK: tools, resources, prompts, and transports. **Use when:** creating an MCP server or adding/updating its tools, resources, or prompts. **Not for:** product business logic or non-MCP API design.
- **[Bazel Build Optimization](sub-skills/bazel-build-optimization/SKILL.md)** — Optimize Bazel builds for large monorepos (remote execution, action caching, hermeticity). **Use when:** configuring Bazel or optimizing enterprise build performance.

### 5. Deep Analysis & Code Craftsmanship
- **[Code Architect](sub-skills/code-architect/SKILL.md)** — Feature architecture blueprints from existing codebase patterns (files, interfaces, data flow, build order). **Use when:** translating approved feature direction into concrete multi-file code structure. **Not for:** deep system-architecture alternatives or final-diff code review.
- **[Architect](sub-skills/architect/SKILL.md)** — System design, scalability, and technical decision-making. **Use when:** planning new cross-cutting features or refactoring large/tightly-coupled systems. **Not for:** line-by-line implementation plans or build/type-error fixing.
- **[Improve Codebase Architecture](sub-skills/improve-codebase-architecture/SKILL.md)** — Find shallow→deep refactor opportunities in existing codebases for testability and AI-navigability. **Use when:** improving architecture, consolidating tightly-coupled modules, or making a codebase more testable. **Not for:** designing new systems from scratch (use System Architecture) or initial brainstorming.

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of the system and API architecture design:
- 👉 Recommend calling **[Security Master](../security-master/SKILL.md)** next to perform a comprehensive STRIDE analysis and map security boundaries before coding.
- 👉 Alternatively, call **[Senior QA](../senior-qa/SKILL.md)** to establish the test strategy and write TDD test cases matching the designed APIs.

---

## 🏗️ Operating Pipeline
This Orchestrator enforces the **[Agent Review Framework](file:///Users/macos/.antigravity-global/agent_review_framework.md)**.
1. **Discovery**: Map tech stack and context.
2. **Risk Assessment**: Use **BFRI Model** for decision making.
3. **Design**: Document using **C4 Model** and **ADRs**.
4. **Hardening**: Apply specific patterns from Sub-Disciplines.

---

## 🏷️ Standards (The Iron Laws)
- **Prohibited**: No `utils`, `helpers`, `common` naming.
- **Limits**: File < 200, Function < 50, Nesting < 3.
- **Library-First**: Always check standard libraries before custom logic.
