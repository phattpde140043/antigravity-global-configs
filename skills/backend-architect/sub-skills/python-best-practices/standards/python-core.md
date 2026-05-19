# Python Core Standards

> Complete patterns reference for modern Python 3.10+ development.

---

## Type Hints

### Built-in Generics (Python 3.10+)
```python
# Use built-in types directly — no typing.List, typing.Dict
def process(items: list[str], config: dict[str, int]) -> bool: ...
def fetch(url: str) -> dict | None: ...
```

### Abstract Types for Parameters
```python
from collections.abc import Mapping, Sequence, Iterable, Callable

# Accept abstract types in params, return concrete types
def transform(data: Mapping[str, int]) -> list[str]: ...
def apply_all(fns: Iterable[Callable[[int], int]], value: int) -> list[int]: ...
```

### TypeVar and Protocols
```python
from typing import TypeVar, Protocol

T = TypeVar("T")

class Comparable(Protocol):
    def __lt__(self, other: "Comparable") -> bool: ...

def sort_items(items: list[T]) -> list[T]: ...
```

---

## Data Structures

### dataclass (Default Choice)
```python
from dataclasses import dataclass, field

@dataclass(slots=True, frozen=True)
class Config:
    host: str
    port: int = 8080
    tags: list[str] = field(default_factory=list)
```

### Pydantic (API Boundaries)
```python
from pydantic import BaseModel, Field, field_validator

class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("Invalid email")
        return v.lower()
```

### attrs (Performance-Critical)
```python
import attrs

@attrs.define
class Point:
    x: float
    y: float

    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
```

---

## Error Handling

### Specific Exceptions
```python
# Minimal try scope, specific exceptions
try:
    result = parse_config(path)
except FileNotFoundError:
    result = default_config()
except ValueError as e:
    raise ConfigError(f"Invalid config: {e}") from e
```

### Custom Exception Hierarchy
```python
class AppError(Exception):
    """Base exception for application errors."""

class NotFoundError(AppError):
    """Resource not found."""

class ValidationError(AppError):
    """Input validation failed."""
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"{field}: {message}")
```

### Never Do
```python
# ❌ Bare except
except:
    pass

# ❌ Broad catch without re-raise
except Exception:
    log.error("something failed")

# ✅ Broad catch WITH re-raise (acceptable in top-level handlers)
except Exception:
    log.exception("Unhandled error")
    raise
```

---

## Resource Management

### Context Managers
```python
from pathlib import Path
from contextlib import contextmanager

# Simple file ops — use Path methods
content = Path("data.txt").read_text(encoding="utf-8")
Path("output.txt").write_text(result, encoding="utf-8")

# Streaming — use context manager
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        process(line)

# Custom context manager
@contextmanager
def managed_connection(url: str):
    conn = create_connection(url)
    try:
        yield conn
    finally:
        conn.close()
```

---

## Async Patterns

### Structured Concurrency
```python
import asyncio

async def main():
    results = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
    )
    return results

asyncio.run(main())
```

### Controlled Concurrency
```python
async def fetch_all(urls: list[str], limit: int = 10):
    semaphore = asyncio.Semaphore(limit)

    async def fetch_one(url: str):
        async with semaphore:
            return await fetch_data(url)

    return await asyncio.gather(*[fetch_one(u) for u in urls])
```

### Async Context Managers
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def managed_session():
    session = await create_session()
    try:
        yield session
    finally:
        await session.close()
```

---

## Testing Patterns

### pytest Conventions
```python
import pytest

class TestUserService:
    def test_create_user_with_valid_data(self, user_service):
        user = user_service.create(name="Alice", email="alice@example.com")
        assert user.name == "Alice"
        assert user.email == "alice@example.com"

    def test_create_user_rejects_empty_name(self, user_service):
        with pytest.raises(ValidationError, match="name"):
            user_service.create(name="", email="alice@example.com")
```

### Fixtures
```python
@pytest.fixture
def user_service(db_session):
    return UserService(session=db_session)

@pytest.fixture
def sample_user(user_service):
    return user_service.create(name="Test", email="test@example.com")
```

---

## Project Structure

```
src/
├── myapp/
│   ├── __init__.py
│   ├── models/          # Data models (dataclass, Pydantic)
│   ├── services/        # Business logic
│   ├── api/             # API endpoints
│   └── utils/           # Shared helpers
tests/
├── unit/
├── integration/
└── conftest.py
```

---

## Import Ordering (isort)

```python
# 1. Standard library
import os
from pathlib import Path

# 2. Third-party
import httpx
from pydantic import BaseModel

# 3. Local
from myapp.models import User
from myapp.services import UserService
```
