# FastAPI & Python Async Patterns

## ⚡ FastAPI Core (v0.100+)
- **Annotated Types**: Use `Annotated` for Dependency Injection and Validation (e.g., `db: Annotated[AsyncSession, Depends(get_db)]`).
- **Pydantic V2**: Utilize the high-performance Rust-based validation engine. Use `.model_dump()` and `.model_validate()`.
- **Async-First**: Always use `async def` for endpoints unless performing blocking I/O (in which case, use `def` and FastAPI will run it in a threadpool).

## 🗄️ SQLAlchemy 2.0 (Async)
- **AsyncSession**: Use `asyncpg` or `aiomysql` drivers.
- **Select Statement**: Use `select()` and `scalars()` for modern 2.0 style queries.
- **Session Lifecycle**: Use `lifespan` events for startup/shutdown database engine initialization.

## 🛡️ Security & Auth
- **OAuth2PasswordBearer**: Standard for JWT-based flows.
- **Dependency Overrides**: Use for clean, testable security logic.
- **Pydantic Settings**: Centralize configuration and secrets management.

## 🚀 Performance & Observability
- **BackgroundTasks**: For lightweight fire-and-forget tasks.
- **Loguru/Structlog**: For structured, async-safe logging.
- **OpenTelemetry**: For distributed tracing.

## 📋 FastAPI Checklist
- [ ] Are all long-running I/O operations `await`-ed?
- [ ] Is `Annotated` used for all dependencies?
- [ ] Are Pydantic models used for both Request and Response schemas?
- [ ] Is there a global exception handler for custom `HTTPException`s?
- [ ] Is `CORS` configured for specific origins only?
