---
name: dotnet-patterns
description: "Idiomatic C# and .NET best practices, DI, and async patterns. Part of the backend-architect discipline."
---

# .NET Development Patterns

## 🏛️ Modern C# Standards
- **Immutability**: Prefer `record` types and `init-only` properties.
- **Syntactic Sugar**: Use `required` properties, Target-typed `new()`, and switch expressions.
- **Raw Strings**: Use raw string literals for SQL, JSON, or Regex.

## 🏗️ Architecture & DI
- **Explicit Dependencies**: Use constructor injection; avoid manual `new` for services.
- **Options Pattern**: Bind config to typed classes; validate on startup.
- **Middleware**: Encapsulate cross-cutting concerns (logging, auth, correlation).

## ⚡ Performance Mastery
- **Non-Blocking**: Async all the way; pass `CancellationToken` through the chain.
- **Memory**: Use `ReadOnlySpan<T>` or `Span<T>` for high-throughput slicing/parsing.
- **Allocation**: Use `ValueTask` for small async methods to reduce heap pressure.

## 💾 Data Access (EF Core)
- **Efficiency**: Use `AsNoTracking()` for reads; project only required columns.
- **Safety**: No string-concatenated queries.
