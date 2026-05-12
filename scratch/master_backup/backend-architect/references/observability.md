# Observability: Logging, Metrics & Tracing

## 🆔 Distributed Tracing
- **X-Correlation-ID / TraceID**: MANDATORY attachment to every request header. TraceID must propagate from Frontend -> API Gateway -> Backend Services -> Database/Cache.
- **Log Correlation**: Every log line must contain a TraceID to enable end-to-end request tracing.

## 📝 Structured Logging
- **Format**: Always use JSON format (Serilog/NLog) for machine-readability (ELK Stack, Grafana Loki).
- **Context**: Enrich logs with contextual metadata like `UserId`, `TenantId`, `MachineName`, and `Environment`.
- **Level Usage**:
    - `Critical`: Severe system failures (DB down, disk failure).
    - `Error`: Business logic errors or Exceptions requiring immediate attention.
    - `Warning`: Unusual behavior not yet causing a crash.
    - `Information`: Major milestones (App start, Job finished).
    - `Debug`: Detailed troubleshooting info (automatically disabled in Production).

## 📊 Metrics (Prometheus/Grafana)
- **RED Pattern**:
    - **R**ate: Requests per second.
    - **E**rrors: Failed requests per second.
    - **D**uration: Response latency.
- **Business Metrics**: Order counts, active user counts, etc.

## 🏥 Health Checks
- **Liveness**: Is the app alive? (Memory/CPU checks only).
- **Readiness**: Is the app ready for traffic? (Check DB, Redis, and Third-party API connectivity).

## 📋 Observability Checklist
- [ ] Do logs contain a TraceID?
- [ ] Is PII (Email, Password) scrubbed from logs?
- [ ] Are Alerts configured for Error Rates > 5% within 1 minute?
- [ ] Is log exportation to a centralized system (ELK/Loki) configured?
