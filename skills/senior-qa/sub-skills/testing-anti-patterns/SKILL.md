---
name: testing-anti-patterns
description: "Identification and prevention of common testing mistakes. Use during BUILD and REVIEW phases to ensure test quality."
---

# Testing Anti-Patterns

Avoid these common pitfalls to maintain a high-quality, reliable test suite.

## 1. Testing Mock Behavior
**Violation**: Asserting that a mock was called rather than asserting on the final state or output of the system.
**Result**: Brittle tests that pass even if the real logic is broken.
**Fix**: Use mocks only for isolation; always assert on true behavior or state changes.

## 2. Test-Only Methods in Production
**Violation**: Adding public methods to production classes used only for setting up or verifying tests.
**Result**: Polluted API and leaked internals.
**Fix**: Use test utilities, factories, or reflection if necessary. Avoid polluting the core domain.

## 3. Incomplete Mocks
**Violation**: Mocking only the fields used for the current test case.
**Result**: Silent failures when code is changed to access new fields.
**Fix**: Mock the complete data structure or use a shared factory for mock objects.

## 4. Fragile Assertions
**Violation**: Asserting on specific string messages, internal indices, or incidental details (e.g., exact timestamps).
**Result**: Frequent test failures on trivial UI or text changes.
**Fix**: Assert on intent and domain results (e.g., `user.is_authenticated()`) instead of implementation details.

## 5. Mocking Without Understanding
**Violation**: Mocking a dependency without knowing its side effects (e.g., database persistence).
**Result**: Tests that pass but integration that fails.
**Fix**: Run tests with real implementations first to understand the contract before deciding to mock.

## Red Flags Checklist
- [ ] Is my test setup longer than the actual test logic?
- [ ] Am I asserting on a mock's internal state?
- [ ] Did I add a "test-only" field to a production class?
- [ ] Does my test break if I change a non-logical string?
