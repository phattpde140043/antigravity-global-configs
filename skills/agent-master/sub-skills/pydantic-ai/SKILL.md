---
name: pydantic-ai
description: "Expert in PydanticAI framework for building type-safe, production-ready AI agents. Focuses on structured outputs, dependency injection, and deterministic testing."
---

# Pydantic AI Agent Framework

Master the creation of robust, typed AI agents using PydanticAI.

## 🏗️ Core Architecture
- **Type-Safe Agents**: Define agents with `result_type` using Pydantic models for guaranteed structured output.
- **Dependency Injection**: Use `deps_type` and `RunContext` to inject services (databases, APIs) into tools, making agents testable.
- **Tool Use**: Register tools using the `@agent.tool` decorator. Docstrings are used as tool descriptions for the LLM.

## 🚀 Key Patterns
- **Structured Output**: Return fully validated Pydantic instances instead of raw strings.
- **Streaming**: Use `run_stream` for progressive responses in user interfaces.
- **Model Overrides**: Use `.override(model=...)` to switch LLM providers (OpenAI, Anthropic, Gemini, Ollama) without changing logic.
- **Model Retry**: Raise `ModelRetry` inside validators to force the LLM to correct its own output based on validation errors.

## 🛡️ Testing & Observability
- **TestModel**: Use for unit tests to verify agent logic without making real LLM calls (saves cost and increases speed).
- **FunctionModel**: Provide deterministic responses for specific test scenarios.
- **Usage Tracking**: Monitor token consumption using `result.usage()`.

## 📋 Verification Checklist
- [ ] Is `result_type` defined with a Pydantic model for structured output?
- [ ] Is dependency injection used for external services (no global state)?
- [ ] Are tools documented with clear, specific docstrings for the LLM?
- [ ] Are unit tests implemented using `TestModel`?
- [ ] Is `ModelRetry` used for recoverable validation failures?
