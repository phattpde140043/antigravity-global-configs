---
name: mcp-server-patterns
description: "Build MCP servers with Node/TypeScript SDK patterns: tools, resources, prompts, validation, and transport choices (stdio vs Streamable HTTP). Use official MCP docs or Context7 for current API signatures. USE WHEN: creating a new MCP server; adding or updating tools/resources/prompts. NOT FOR: product-specific business logic; generic API design unrelated to MCP."
origin: ECC
---

# MCP Server Patterns

Build MCP servers that are robust, version-aware, and easy for clients to integrate.

---

## Purpose

Use this skill for implementing and maintaining MCP servers: tool/resource/prompt registration, schema validation, transport selection, and runtime troubleshooting.

---

## When to Activate

- creating a new MCP server
- adding or updating tools/resources/prompts
- choosing stdio vs Streamable HTTP transport
- upgrading MCP SDK versions
- debugging registration, schema, or transport issues

---

## Scope Boundaries

Use this skill for:
- MCP server architecture and implementation patterns
- schema-first tool contracts
- transport and deployment decisions
- compatibility and upgrade strategy

Do NOT use this skill as primary source for:
- product-specific business logic
- generic API design unrelated to MCP
- relying on stale SDK signatures from memory

Delegation:
- use `documentation-lookup` to fetch up-to-date MCP API signatures
- use `deep-research` for broader protocol/vendor landscape analysis

---

## Core Concepts

- Tools: callable actions exposed to the model
- Resources: read-only retrievable data
- Prompts: reusable parameterized prompt templates
- Transport: stdio for local integration, Streamable HTTP for remote clients

Version rule:
- SDK method names/signatures can evolve; verify against current docs before coding.

---

## Implementation Workflow

## 1) Define Server Contract First

Specify:
- server name/version
- tool/resource/prompt inventory
- input/output schemas
- error model and observability fields

## 2) Implement Schema-First Registration

- validate every tool input with schema (for example Zod)
- define clear output shape and failure shape
- reject ambiguous or weakly typed contracts

## 3) Keep Transport Isolated

- keep core business handlers transport-agnostic
- plug stdio or HTTP transport in thin entrypoints
- avoid mixing transport concerns into tool logic

## 4) Add Operational Guardrails

- structured logging
- request correlation IDs where possible
- timeout and retry strategy for external dependencies
- rate/cost controls for expensive downstream APIs

## 5) Validate End-to-End

- registration appears in client
- schema validation fails safely on bad input
- tools/resources/prompts return expected structure
- transport handshake and lifecycle events are healthy

---

## Transport Selection Guide

Use stdio when:
- local desktop workflows
- low-latency local process integration
- simple single-user setups

Use Streamable HTTP when:
- remote or shared environments
- cloud deployment and multi-client access
- managed infrastructure and observability requirements

Fallback:
- support legacy transport only when compatibility is explicitly required.

---

## Tool/Resource Design Rules

1. Schema first: no unvalidated free-form input for critical paths.
2. Idempotent by default where retries are possible.
3. Error responses must be structured and actionable.
4. Include cost/rate notes in tool descriptions for expensive calls.
5. Keep tool surface small and composable.

---

## Versioning and Upgrades

- pin SDK version in dependency manifest
- review changelogs before upgrading
- run compatibility tests for registration/transport behavior
- avoid copy-paste snippets without version check

---

## Troubleshooting Playbook

- tool not visible: verify registration path and schema shape
- handler not called: verify client capability negotiation and transport wiring
- intermittent failures: inspect timeout/retry settings and downstream dependency health
- schema mismatch: compare runtime payload with declared contract

---

## Quality Gate

Before shipping:

- [ ] tool/resource/prompt contracts are validated and documented
- [ ] transport choice is explicit and justified
- [ ] error handling is structured and non-leaky
- [ ] observability fields are present
- [ ] SDK version and docs alignment is confirmed

---

## Hard Bans

Do not ship:
- unvalidated tool inputs on critical operations
- stale SDK signatures copied without verification
- transport-coupled core logic
- raw stack traces exposed as user-facing tool output

---

## Output Contract

When activated, return:

1. MCP server contract summary
2. registration and schema plan
3. transport decision with rationale
4. validation/troubleshooting checklist
5. upgrade and compatibility notes
