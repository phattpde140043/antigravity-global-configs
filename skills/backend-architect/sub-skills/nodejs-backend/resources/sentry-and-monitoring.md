# Sentry & Monitoring — Full Production Setup

## instrument.ts Template (MUST be first import)

```typescript
// src/instrument.ts — import this BEFORE anything else in server.ts
import * as Sentry from '@sentry/node';
import { config } from './config/unifiedConfig';

Sentry.init({
    dsn: config.sentry.dsn,
    environment: process.env.NODE_ENV || 'development',
    tracesSampleRate:    config.sentry.tracesSampleRate ?? 0.1,
    profilesSampleRate:  config.sentry.profilesSampleRate ?? 0.1,

    integrations: [
        ...Sentry.getDefaultIntegrations({}),
        Sentry.extraErrorDataIntegration({ depth: 5 }),
        Sentry.localVariablesIntegration(),
        Sentry.prismaIntegration(),          // Auto-instrument Prisma queries
        Sentry.contextLinesIntegration(),
    ],

    beforeSend(event) {
        // 1. Filter noise — health checks are not errors
        if (event.request?.url?.includes('/health')) return null;

        // 2. Scrub sensitive headers
        if (event.request?.headers) {
            delete event.request.headers['authorization'];
            delete event.request.headers['cookie'];
            delete event.request.headers['x-api-key'];
        }

        // 3. Mask PII — email addresses
        if (event.user?.email) {
            event.user.email = event.user.email.replace(/^(.{2}).*(@.*)$/, '$1***$2');
        }

        return event;
    },

    ignoreErrors: [
        /^Invalid JWT/,
        /^JWT expired/,
        'NetworkError',
    ],
});

// Tag every event with service identity
Sentry.setTags({ service: config.service.name, version: config.service.version });
Sentry.setContext('runtime', { node_version: process.version });
```

```typescript
// server.ts — instrument.ts MUST be the first import
import './instrument'; // ← FIRST LINE (no exceptions)
import express from 'express';
// ... rest of imports
```

## Performance Spans

```typescript
// Wrap key operations in a span for distributed tracing
router.post('/workflow/execute', async (req, res) => {
    return Sentry.startSpan(
        { name: 'workflow.execute', op: 'http.server', attributes: { 'http.method': 'POST' } },
        async () => {
            const result = await workflowService.execute(req.body);
            res.json({ success: true, data: result });
        }
    );
});
```

## Cron Job Monitoring

```typescript
// #!/usr/bin/env node
import '../instrument'; // ← FIRST (after shebang)
import * as Sentry from '@sentry/node';

async function main() {
    return Sentry.startSpan({ name: 'cron.cleanup-expired-sessions', op: 'cron' }, async () => {
        try {
            await sessionService.cleanupExpired();
        } catch (error) {
            Sentry.captureException(error, { tags: { 'cron.job': 'cleanup-expired-sessions' } });
            logger.error('[Cron] Failed:', error);
            process.exit(1);
        }
    });
}

main()
    .then(() => process.exit(0))
    .catch((err) => { logger.error('[Cron] Fatal:', err); process.exit(1); });
```

## Rich Error Context

```typescript
Sentry.withScope((scope) => {
    scope.setUser({ id: user.id });                       // Non-PII user identifier
    scope.setTag('service', 'notification');
    scope.setTag('operation', 'createNotification');
    scope.setContext('operation', { type, recipientId: user.id, channel });
    scope.addBreadcrumb({ category: 'notification', message: 'Starting routing', level: 'info' });
    Sentry.captureException(error);
});
```

## PII Rules Summary

| Data | Rule |
| --- | --- |
| User ID | ✅ Safe to log |
| Tenant ID | ✅ Safe to log |
| Email | ⚠️ Must mask: `us***@domain.com` |
| Name | ⚠️ Avoid in error context |
| Password / Token | ❌ NEVER log |
| Cookie / Auth header | ❌ Delete before sending to Sentry |
| IP Address | ⚠️ Check GDPR/compliance requirements |
