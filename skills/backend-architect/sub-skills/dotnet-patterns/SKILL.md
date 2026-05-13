---
name: dotnet-patterns
description: "Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for building robust, maintainable .NET applications. USE WHEN: writing new C# code; refactoring .NET services and libraries. NOT FOR: deep security audits or threat modeling; PR severity triage process."
---

# .NET Development Patterns

Idiomatic C# and .NET patterns for robust, performant, and maintainable applications.

## Purpose

Use this skill as the practical implementation guide for day-to-day .NET code decisions.

## When to Activate

- writing new C# code
- refactoring .NET services and libraries
- reviewing idiomatic .NET usage
- designing ASP.NET Core service architecture boundaries

## Scope Boundaries

Use this skill for:
- C# language and .NET framework patterns
- async/await, DI, options, and middleware best practices
- EF Core query and repository patterns

Do NOT use this skill as primary source for:
- deep security audits or threat modeling
- PR severity triage process
- build-only error triage workflows

Delegation:
- use [security-review](../security-review/SKILL.md) for implementation-time security checklist
- use [csharp-reviewer](../csharp-reviewer/SKILL.md) for review findings on changed C# code
- use [build-error-resolver](../build-error-resolver/SKILL.md) for minimal-diff compile/type fixes

## Core Principles

1. prefer immutability by default
2. explicit over implicit (nullability, access, intent)
3. depend on abstractions at service boundaries
4. async all the way, never block async paths
5. prioritize performance with ValueTypes and Spans where I/O or high-throughput logic exists
6. keep code simple, testable, and observable

## Immutability and Modeling

- Prefer `record`, `readonly struct`, or value-like models where mutation is not required.
- Use **Primary Constructors** (C# 12+) to simplify dependency injection and initialization.
- Use `init`-only properties for request/DTO models when possible.
- Use `required` properties and `raw string literals` for safer and more readable DTOs.
- Use **Target-typed new** (`List<string> list = new();`) for brevity when the type is obvious.

## 🚀 Modern C# (12/13) & .NET 8/9
- **Pattern Matching**: Leverage switch expressions and property patterns for clean conditional logic.
- **Result Pattern**: Avoid exception-driven flow control by returning `Result<T>` records containing success/failure state.
- **Async Efficiency**: Use `ValueTask` for hot paths and `IAsyncEnumerable` for streaming large datasets.
- **Span & Memory**: Use `ReadOnlySpan<T>` and `Memory<T>` for zero-allocation memory manipulation.

## 🏗️ Architectural Patterns
- **Clean Architecture**: Isolate the Domain from Infrastructure and Application concerns.
- **Vertical Slice Architecture**: Group code by features rather than technical layers.
- **CQRS**: Separate read and write concerns using MediatR or custom dispatchers.
- **Repository & Unit of Work**: Abstract data access while maintaining transactional integrity.

## Dependency Injection and Boundaries

- register dependencies through container, avoid manual new-ing for app services
- use constructor injection for required dependencies
- keep service interfaces cohesive and focused

## Async/Await Patterns

- pass CancellationToken through async call chains
- use Task.WhenAll for independent concurrent operations
- avoid Result/Wait/GetAwaiter().GetResult() in request paths
- avoid async void except event handlers
- simplify small async methods with `ValueTask` or `ValueTask<T>` to reduce heap allocations on high-frequency hot paths.

## Configuration via Options Pattern

- bind configuration sections to typed options
- validate critical configuration on startup when possible
- avoid ad hoc dictionary/config parsing in application logic

## Result and Error Patterns

- use explicit result objects for expected domain failures where useful
- throw exceptions for exceptional flows, not routine validation outcomes
- preserve context in logs while returning safe client-facing errors

### Result Pattern Implementation

```csharp
public record Result<T>(bool IsSuccess, T? Value, string? Error = null, string? ErrorCode = null)
{
    public static Result<T> Success(T value) => new(true, value);
    public static Result<T> Failure(string error, string? code = null) => new(false, default, error, code);
}
```

## Clean Architecture Structure

Organize projects by responsibility:
- **Domain**: Entities, Interfaces, Exceptions, ValueObjects (No dependencies).
- **Application**: Use cases, DTOs, Validators, Interfaces.
- **Infrastructure**: Data access (EF/Dapper), Caching, External APIs.
- **Api**: Controllers, MinimalAPI, Middleware, Program.cs.

## EF Core and Data Access Patterns

- use AsNoTracking for read-only queries
- avoid N+1 loading patterns
- project only needed columns for list/read paths
- keep repository/service responsibilities clean

## Middleware and Pipeline

- encapsulate cross-cutting concerns in middleware
- ensure structured logging and correlation identifiers where required
- keep middleware lightweight and deterministic

## Minimal API and Endpoint Patterns

- group related routes
- keep handlers thin, push business logic to services
- return explicit typed results where supported

## Guard Clauses and Flow Clarity

- validate inputs early
- use guard clauses to reduce nesting
- keep happy path straightforward

## Anti-Patterns to Avoid

- async blocking calls
- empty catch blocks and swallowed exceptions
- mutable global static state
- hardcoded config/secrets
- large god classes with mixed responsibilities
- string-concatenated queries or dynamic unsafe command building

## Performance Mastery

- Use `ReadOnlySpan<char>` or `Span<T>` for high-performance string/array manipulation (e.g., parsing, slicing).
- Avoid unnecessary object allocations in loops; use `ArrayPool<T>` for large temporary buffers.
- For high-throughput services, use **BenchmarkDotNet** to measure and validate performance improvements before committing to complex optimizations.
- Prefer **Composition over Inheritance** to maintain flexibility and simplify testing.

## Practical Checklist

Before shipping .NET changes:

- [ ] nullability and async usage are correct
- [ ] DI boundaries are respected
- [ ] config uses typed options
- [ ] data access is efficient and safe
- [ ] logging/error handling are consistent
- [ ] no obvious anti-patterns remain

## Output Contract

When activated, return:

1. recommended .NET patterns for current task
2. concrete implementation guidance
3. anti-pattern risks detected
4. prioritized cleanup/refactor actions
