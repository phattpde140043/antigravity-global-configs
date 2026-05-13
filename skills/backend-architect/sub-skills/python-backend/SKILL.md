---
name: python-backend
description: "Expert in high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Focuses on async-first development, microservices, and modern Python patterns."
---

# Python Backend Development

Master high-performance, async-first API development with modern Python patterns.

## Core Stack
- **FastAPI**: Modern, high-performance web framework.
- **Pydantic V2**: Strict data validation and serialization.
- **SQLAlchemy 2.0**: Async-capable ORM (use `asyncpg` or `aiomysql`).
- **Alembic**: Database migrations for SQLAlchemy.

## 🚀 Async-First Patterns
- Use `async def` for I/O bound operations (DB, API, Files).
- Avoid blocking calls (`time.sleep`, synchronous DB drivers) in async paths.
- Use `BackgroundTasks` for lightweight post-request processing.
- Use `CancellationToken` patterns (via Request State) where supported.

## ⚡ Performance & Optimization
- **Profiling**: Use `cProfile` and `viztracer` to identify CPU bottlenecks. Use `memory_profiler` for memory leaks.
- **Async Efficiency**: Use `anyio.to_thread.run_sync` for CPU-bound tasks to avoid blocking the event loop.
- **Data Validation**: Leverage **Pydantic v2** for ultra-fast serialization and strict type validation.
- **Concurrency**: Use `asyncio.gather` for parallel I/O operations with proper error handling.

## 🏗️ Architecture Best Practices
- **Dependency Injection**: Use FastAPI's `Depends` for clean, testable code.
- **Annotated Types**: Use `Annotated` for clear dependency definitions.
- **Repository Pattern**: Abstract data access from business logic.
- **Middleware**: Implement cross-cutting concerns (Auth, Logging, CORS).

## 🛡️ Security & Validation
- **JWT Authentication**: Secure token-based auth with `python-jose`.
- **Input Validation**: Leverage Pydantic's powerful validation features.
- **Rate Limiting**: Protect endpoints with IP or User-based limits.
- **Security Headers**: Use `CORSMiddleware` and standard security headers.

## 🧪 Testing Strategy
- **pytest-asyncio**: Standard for async Python testing.
- **TestClient**: For integration/E2E testing of FastAPI endpoints.
- **Mocks**: Use `pytest-mock` for external service dependencies.

## Verification Checklist
- [ ] Is all I/O handled asynchronously?
- [ ] Are Pydantic models used for all inputs and outputs?
- [ ] Is dependency injection used to improve testability?
- [ ] Are tests covering both happy and error paths?
- [ ] Is OpenAPI documentation (Swagger) correctly configured?
