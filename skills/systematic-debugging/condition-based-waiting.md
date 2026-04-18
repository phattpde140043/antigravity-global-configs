# Condition-Based Waiting

## Overview

Flaky tests are often caused by race conditions: the test checks for a result before the background process (agent, worker, database) has finished.

**Anti-pattern**: `await delay(5000);` (Slows down tests and doesn't guarantee the result).
**Elite Pattern**: Poll for the specific condition you need.

---

## Utility Functions

Use a robust polling utility to wait for specific thread events or state changes.

### TypeScript Implementation

```typescript
/**
 * Poll for a condition to be met
 * @param predicate - Function that returns true when condition is met
 * @param timeoutMs - Maximum time to wait
 * @param intervalMs - Time between checks
 */
export async function waitFor(
  predicate: () => boolean | Promise<boolean>,
  timeoutMs = 5000,
  intervalMs = 100
): Promise<void> {
  const startTime = Date.now();
  while (Date.now() - startTime < timeoutMs) {
    if (await predicate()) return;
    await new Promise(r => setTimeout(r, intervalMs));
  }
  throw new Error(`Timeout waiting for condition after ${timeoutMs}ms`);
}
```

---

## Usage Examples

### 1. Wait for a specific event count
```typescript
// Wait until at least 3 messages are in the thread
await waitFor(() => threadManager.getMessages(threadId).length >= 3);
```

### 2. Wait for a specific event type
```typescript
// Wait until a TOOL_RESULT event appears
await waitFor(() => 
  threadManager.getEvents(threadId).some(e => e.type === 'LACE_EVENT_TOOL_RESULT')
);
```

### 3. Combining with Assertions
```typescript
await waitFor(() => threadIsDone(threadId));
const messages = threadManager.getMessages(threadId);
expect(messages).toContain('Success');
```

---

## Why this is better than delay()
1. **Speed**: Resolves the instant the condition is met (often < 100ms).
2. **Reliability**: Handles variable latency in background processes.
3. **Clarity**: Explicitly states what the test is waiting for.

## Enforcement Rule
**RED FLAG**: Any use of `setTimeout`, `delay`, or `sleep` in a test without a predicate.
**REMEDY**: Replace with `waitFor()` and a specific condition.

---
**Debugging Workflow Complete.**
[Back to Systematic Debugging Master Skill](./SKILL.md)

