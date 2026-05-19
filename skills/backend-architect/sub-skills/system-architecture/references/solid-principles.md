# SOLID Principles

## S — Single Responsibility Principle
A class should have only one reason to change.

```csharp
// ❌ WRONG — multiple responsibilities
public class UserService
{
    public void CreateUser(User user) { /* DB logic */ }
    public void SendWelcomeEmail(User user) { /* Email logic */ }
    public string GenerateReport(User user) { /* Report logic */ }
}

// ✅ CORRECT — single responsibility each
public class UserService { public void CreateUser(User user) { } }
public class UserNotificationService { public void SendWelcomeEmail(User user) { } }
public class UserReportService { public string GenerateReport(User user) { } }
```

## O — Open/Closed Principle
Open for extension, closed for modification. Use abstractions and polymorphism.

## L — Liskov Substitution Principle
Subtypes must be substitutable for their base types without altering correctness.

## I — Interface Segregation Principle
No client should be forced to depend on methods it does not use. Prefer small, focused interfaces.

```csharp
// ❌ WRONG — fat interface
public interface IRepository<T>
{
    Task<T> GetById(int id);
    Task<List<T>> GetAll();
    Task Add(T entity);
    Task Update(T entity);
    Task Delete(int id);
    Task BulkImport(List<T> entities);   // Not all repos need this
    Task GenerateReport();                // Not a repository concern
}

// ✅ CORRECT — segregated
public interface IReadRepository<T> { Task<T> GetById(int id); Task<List<T>> GetAll(); }
public interface IWriteRepository<T> { Task Add(T entity); Task Update(T entity); Task Delete(int id); }
public interface IBulkImportable<T> { Task BulkImport(List<T> entities); }
```

## D — Dependency Inversion Principle
Depend on abstractions, not concretions. High-level modules should not depend on low-level modules.

```csharp
// ❌ WRONG — depends on concrete implementation
public class SearchService
{
    private readonly ElasticSearchClient _client = new();
}

// ✅ CORRECT — depends on abstraction
public class SearchService
{
    private readonly ISearchProvider _provider;
    public SearchService(ISearchProvider provider) => _provider = provider;
}
```
