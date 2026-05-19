# Condition-Based Waiting

## Overview

Replace arbitrary timeouts (`time.sleep(5)`, `setTimeout(5000)`) with condition-based polling. Arbitrary timeouts are either too short (flaky) or too long (slow). Condition-based waiting adapts to actual system speed.

## The Anti-Pattern

```python
# ❌ BAD: Arbitrary timeout — too slow on fast machines, too fast on slow CI
time.sleep(5)
response = api.get("/status")
assert response.json()["ready"] == True
```

## The Pattern

```python
# ✅ GOOD: Condition-based polling — adapts to actual speed
import time

def wait_for_condition(check_fn, timeout=30, interval=0.5, description="condition"):
    """Poll until check_fn() returns True or timeout expires."""
    start = time.time()
    last_error = None
    while time.time() - start < timeout:
        try:
            if check_fn():
                return True
        except Exception as e:
            last_error = e
        time.sleep(interval)
    raise TimeoutError(
        f"Condition '{description}' not met within {timeout}s. "
        f"Last error: {last_error}"
    )

# Usage
wait_for_condition(
    lambda: api.get("/status").json().get("ready") == True,
    timeout=30,
    description="API becomes ready"
)
```

## Rules

1. **Never use `time.sleep()` for synchronization** — only for rate limiting
2. **Always set a timeout** — infinite polling is worse than arbitrary timeouts
3. **Include a description** — timeout errors must explain what was being waited for
4. **Log the last error** — helps debugging when the condition never becomes true
5. **Use reasonable intervals** — 0.5s for fast checks, 2-5s for expensive checks

## When to Use

- Waiting for a service to become ready after startup
- Waiting for async operations to complete (index refresh, cache invalidation)
- Waiting for CI/CD pipeline stages to finish
- Any test that uses `time.sleep()` for timing-dependent behavior

## Application to E2E Tests

| Scenario | Instead of | Use |
|----------|-----------|-----|
| OpenSearch index refresh | `time.sleep(3)` | Poll `/_refresh` endpoint |
| Keycloak token generation | `time.sleep(1)` | Already synchronous (no wait needed) |
| Playwright page load | `time.sleep(2)` | `page.wait_for_load_state("networkidle")` |
| API availability after deploy | `time.sleep(10)` | Poll health endpoint with condition |
