# .NET & C# Best Practices (Modern Era)

## 💎 Modern C# Features (12/13)
- **Primary Constructors**: Reduce boilerplate code for Dependency Injection.
- **Collection Expressions**: Use `[]` instead of `new List<T>()` or `new[]`.
- **Required Members**: Mandate property initialization without complex constructors.
- **Raw String Literals**: Use `"""` for long JSON or SQL strings without escaping.

## ⚡ Async/Await Patterns
- **Async All The Way**: Never use `.Result` or `.Wait()`.
- **ValueTask**: Use for hot-paths that likely return immediately (from cache) to reduce memory allocation.
- **IAsyncEnumerable**: Use for streaming large datasets from Databases or APIs.
- **CancellationToken**: Always propagate `CancellationToken` to every async method.
- **ConfigureAwait(false)**: Use in library code to avoid deadlocks and optimize performance.

## 💉 Dependency Injection (DI)
- **Keyed Services (.NET 8+)**: Register multiple implementations for the same interface and distinguish them by Key.
- **Lifetimes**: 
    - `Singleton`: Single instance (Cache, Config).
    - `Scoped`: One instance per request (DbContext, UnitOfWork).
    - `Transient`: New instance every time (Validators, Lightweight services).
- **IOptions Pattern**: Use `IOptions`, `IOptionsSnapshot`, or `IOptionsMonitor` for type-safe configuration.

## 🎯 Result Pattern
Avoid using Exceptions for business logic. Use a `Result<T>` object to return success/failure status.

```csharp
public record Result<T>(bool IsSuccess, T? Value, string? Error = null);
```

## 📐 Architecture Patterns
- **Clean Architecture**: Domain at the core, dependencies pointing inward.
- **Vertical Slice Architecture**: Organize code by Feature rather than technical layers for complex projects.
- **CQRS**: Use `MediatR` to separate Command (Write) and Query (Read) flows.
