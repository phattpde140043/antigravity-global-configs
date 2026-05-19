# Observability — Logging, Metrics, and Tracing

## Three Pillars

| Pillar | Purpose | Tool |
|--------|---------|------|
| **Logging** | What happened (events) | Serilog, ILogger |
| **Metrics** | How much / how fast (aggregates) | Prometheus, App Insights |
| **Tracing** | Request flow across services | OpenTelemetry, Jaeger |

## Structured Logging

### Rules
- Use structured logging with `{Placeholder}` syntax, NOT string interpolation
- Include `CorrelationId` in every log entry
- Log at boundaries: API entry, service calls, external calls, errors
- NEVER log sensitive data (passwords, tokens, PII)

```csharp
// ✅ CORRECT — structured logging
_logger.LogInformation("Search executed for tenant {TenantId} with {ResultCount} results",
    tenantId, results.Count);

// ❌ WRONG — string interpolation (evaluates even when log level is disabled)
_logger.LogInformation($"Search executed for tenant {tenantId} with {results.Count} results");
```

### Log Levels

| Level | Use For |
|-------|---------|
| `Trace` | Detailed debugging (disabled in production) |
| `Debug` | Development diagnostics |
| `Information` | Normal operations (request start/end, business events) |
| `Warning` | Unexpected but handled (retry, fallback) |
| `Error` | Unhandled exceptions, operation failures |
| `Critical` | System failures (database down, out of memory) |

## Metrics

### Key Metrics to Track
- **Request Rate** — requests per second by endpoint
- **Error Rate** — 4xx and 5xx responses
- **Latency** — p50, p95, p99 response times
- **Saturation** — CPU, memory, connection pool usage

## Distributed Tracing

### OpenTelemetry Setup
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(tracing => tracing
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddEntityFrameworkCoreInstrumentation()
        .AddSource("MyApp")
        .AddOtlpExporter());
```

### Trace Context Propagation
- Pass `traceparent` header across service boundaries
- Use `Activity.Current` to add custom spans
- Tag spans with tenant ID for multi-tenant debugging
