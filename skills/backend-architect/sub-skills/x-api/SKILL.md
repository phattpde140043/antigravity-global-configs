---
name: x-api
description: "X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. Covers OAuth auth patterns, rate limits, and platform-native content posting. USE WHEN: posting tweets or threads programmatically; reading timeline/mentions/user info. NOT FOR: content strategy and editorial planning; cross-platform distribution orchestration."
origin: ECC
---

# X API

Programmatic interaction with X for posting, reading, searching, and engagement tracking.

---

## Purpose

Use this skill to implement and operate X integrations safely with clear auth, rate-limit handling, and posting workflows.

---

## When to Activate

- posting tweets or threads programmatically
- reading timeline/mentions/user info
- searching X conversations/trends
- building bots or automation workflows
- tracking basic engagement metrics

---

## Scope Boundaries

Use this skill for:
- X API auth and request patterns
- posting/search/read workflows
- rate-limit and error handling
- operational safety for API integrations

Do NOT use this skill as primary source for:
- content strategy and editorial planning
- cross-platform distribution orchestration
- stale endpoint assumptions without docs verification

Delegation:
- use `content-engine` to draft X-native content
- use `crosspost` for multi-platform adaptation
- use `brand-voice` when strict voice matching is required

---

## Authentication Modes

## App-Only (OAuth 2 bearer)

Best for read-heavy operations and public data queries.

## User Context (OAuth 1.0a or current write auth path)

Required for write actions such as posting tweets/threads and account-scoped operations.

Rule:
- verify current auth requirements in official docs before implementation.

---

## Core Operation Patterns

- post single tweet
- post threaded tweets (reply chain)
- read user timeline
- search recent tweets
- lookup user by username
- optional media upload + post association

Design rules:
- idempotency strategy for retries (avoid duplicate posting)
- structured request/response logging without leaking secrets
- explicit dry-run mode when available for testing message payloads

---

## Rate Limits and Reliability

- do not hardcode static limits as permanent truth
- inspect rate-limit headers at runtime
- backoff on 429 responses
- queue/retry with jitter for burst traffic

For posting flows:
- handle transient failures with bounded retries
- fail safely with clear operator-visible error messages

---

## Security Rules

1. never hardcode credentials
2. keep tokens in environment/secret manager only
3. never log secrets or raw auth headers
4. use least-privilege tokens when possible
5. rotate credentials if exposure is suspected

---

## Error Handling Model

Handle explicitly:
- auth errors (401/403)
- rate limits (429)
- validation/content errors
- transport/network failures

Return actionable error categories for operators.

---

## Integration Workflow

1. validate auth mode for intended operation
2. build and validate payload
3. execute request with retry/rate policy
4. parse and persist key IDs/metrics
5. return concise operation summary

---

## Quality Gate

Before shipping integration:

- [ ] auth flow tested for read and/or write path
- [ ] rate-limit handling verified
- [ ] retries bounded and idempotent for posting
- [ ] secret handling verified end-to-end
- [ ] error taxonomy mapped to actionable remediation

---

## Output Contract

When activated, return:

1. selected auth mode and prerequisites
2. endpoint operation plan
3. rate-limit and retry strategy
4. security controls checklist
5. execution/reporting format
