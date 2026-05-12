---
name: migration-observability
description: "Expert in real-time database migration monitoring, CDC (Change Data Capture) pipelines, and anomaly detection during data transitions."
---

# Migration Observability

Ensure zero-downtime, high-fidelity data migrations with real-time visibility and alerting.

## 🏗️ Observability Architecture
- **CDC (Change Data Capture)**: Use **Debezium** and **Kafka** to stream real-time changes from source to target.
- **Metrics Instrumentation**: Use Prometheus to track:
  - **Documents/Rows Processed**: Total throughput.
  - **Replication Lag**: Time delay between source and target.
  - **Error Rate**: Percentage of failed transformations.
- **Anomaly Detection**: Monitor for sudden drops in throughput or spikes in error rates.

## ⚡ Real-Time Monitoring Patterns
- **Grafana Dashboards**: Programmatic creation of dashboards for live migration tracking.
- **Alerting**: Multi-channel alerts (Slack, PagerDuty) for critical lag or pipeline failures.
- **Verification**: Continuous checksum or row-count validation between source and target.

## 🛡️ Best Practices
- **Idempotency**: All migration steps must be safely retryable.
- **Progress Tracking**: Store migration state in a persistent "metadata" table.
- **Logging**: Structured logging for every batch and transformation error.

## 📋 Verification Checklist
- [ ] Is the CDC pipeline (Debezium/Kafka) healthy and lag-free?
- [ ] Are real-time metrics being exported to Prometheus?
- [ ] Is there an automated dashboard for the migration progress?
- [ ] Are alerts configured for throughput anomalies?
- [ ] Is the replication lag within acceptable thresholds (< 5s)?
