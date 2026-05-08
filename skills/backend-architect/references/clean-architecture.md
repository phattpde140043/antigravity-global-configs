# Clean Architecture (The Dependency Rule)

The primary goal of Clean Architecture is the separation of concerns, ensuring that the business logic is independent of frameworks, databases, and external interfaces.

## 🏗️ The Dependency Rule
Source code dependencies must point only **inward** toward higher-level policies (Entities and Use Cases).

1. **Entities (Enterprise Business Rules)**: The heart of the application. No outward dependencies. Pure business logic.
2. **Use Cases (Application Business Rules)**: Orchestrate the flow of data. Depend only on Entities.
3. **Interface Adapters (Presenters, Gateways, Controllers)**: Convert data between Use Cases/Entities and external formats.
4. **Frameworks & Drivers (DB, UI, External APIs)**: The outermost layer. Should be kept as "plug-ins" to the system.

## 🛡️ Implementation Rules
- **Framework Independence**: The system should not depend on a specific library or framework (e.g., your Core logic should not import `Entity Framework` or `FastAPI` specifics).
- **Testability**: Business rules can be tested without the UI, Database, or any other external element.
- **Database Independence**: You should be able to swap your database (e.g., SQL Server to MongoDB) without changing your business rules.
