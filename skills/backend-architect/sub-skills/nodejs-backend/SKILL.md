---
name: nodejs-backend
description: "Production-grade Node.js backend engineering guide. Covers Express/TypeScript layered architecture, Zod validation, Prisma data access, Sentry observability, async error handling, and testing discipline. USE WHEN: building or reviewing Node.js/Express microservices, APIs, background jobs, or middleware. NOT FOR: C#/.NET services (use dotnet-patterns + csharp-reviewer instead); frontend React/Next.js code."
stack: ["Node.js", "Express", "TypeScript", "Prisma", "Zod", "Sentry", "Jest"]
origin: internal
date_created: "2026-04-24"
---

# Node.js Backend Engineering

Production-grade guide for building predictable, observable, and maintainable Node.js backend services.

## When to Use

Activate this skill when working on:
- Express routes, controllers, services, repositories
- Middleware (auth, audit, error boundary, validation)
- Prisma database access and query optimization
- Zod input validation schemas
- Sentry error tracking and performance monitoring
- Background jobs and cron tasks
- Configuration management
- Backend refactors or migrations

Do NOT use for:
- C#/.NET services → use `dotnet-patterns` + `csharp-reviewer`
- Frontend React/Next.js → use `frontend-patterns` + `nextjs-turbopack`
- Pure infrastructure/DevOps → use `ci-cd-and-automation`

---

## Core Architecture Doctrine

### The Four-Layer Rule (Non-Negotiable)

```
HTTP Request
    ↓
Routes        → Define paths, register middleware, delegate to controllers. ZERO business logic.
    ↓
Controllers   → Parse request, validate input (Zod), call service, format response, handle errors.
    ↓
Services      → Business logic, orchestration, business rules. Framework-agnostic.
    ↓
Repositories  → Data access abstraction, Prisma operations, query optimization.
    ↓
Database
```

**Layer violation rules:**
- ❌ Routes must NEVER contain business logic or direct DB calls
- ❌ Controllers must NEVER contain business rules or Prisma calls
- ❌ Services must NEVER import `Request`/`Response` types (no HTTP knowledge)
- ❌ Repositories must NEVER contain business decisions

### Directory Structure (Canonical)

```
src/
├── config/              # unifiedConfig — typed, validated at startup
├── controllers/         # BaseController + feature controllers
├── services/            # Business logic (framework-agnostic)
├── repositories/        # Prisma data access
├── routes/              # Express route registration only
├── middleware/          # Auth, audit, error boundary, validation
├── validators/          # Zod schemas + inferred DTO types
├── types/               # Shared TypeScript types
├── utils/               # Stateless helpers
├── tests/               # Unit + integration tests
├── instrument.ts        # Sentry init — MUST be first import
├── app.ts               # Express app setup
└── server.ts            # HTTP server entrypoint
```

---

## Routes — Routing Only

```typescript
// ✅ CORRECT — routes/userRoutes.ts
import { Router } from 'express';
import { UserController } from '../controllers/UserController';
import { SSOMiddlewareClient } from '../middleware/SSOMiddleware';
import { auditMiddleware } from '../middleware/auditMiddleware';

const router = Router();
const controller = new UserController();

router.get('/:id',   SSOMiddlewareClient.verifyLoginStatus, auditMiddleware, (req, res) => controller.getUser(req, res));
router.post('/',     SSOMiddlewareClient.verifyLoginStatus, auditMiddleware, (req, res) => controller.createUser(req, res));
router.put('/:id',   SSOMiddlewareClient.verifyLoginStatus, auditMiddleware, (req, res) => controller.updateUser(req, res));
router.delete('/:id',SSOMiddlewareClient.verifyLoginStatus, auditMiddleware, (req, res) => controller.deleteUser(req, res));

export default router;
```

---

## BaseController Pattern

All controllers MUST extend `BaseController`. No raw `res.json()` calls outside helpers.

```typescript
// controllers/BaseController.ts
import * as Sentry from '@sentry/node';
import { Response } from 'express';

export abstract class BaseController {
    protected handleError(error: unknown, res: Response, context: string, statusCode = 500): void {
        Sentry.withScope((scope) => {
            scope.setTag('controller', this.constructor.name);
            scope.setTag('operation', context);
            Sentry.captureException(error);
        });
        res.status(statusCode).json({
            success: false,
            error: { message: error instanceof Error ? error.message : 'An error occurred', code: statusCode },
        });
    }

    protected handleSuccess<T>(res: Response, data: T, message?: string, statusCode = 200): void {
        res.status(statusCode).json({ success: true, message, data });
    }

    protected async withTransaction<T>(name: string, op: string, callback: () => Promise<T>): Promise<T> {
        return Sentry.startSpan({ name, op }, callback);
    }
}
```

---

## Validation — Zod (Mandatory)

All external input MUST be validated before reaching services.

```typescript
// validators/userSchemas.ts
import { z } from 'zod';

export const createUserSchema = z.object({
    email: z.string().email(),
    name:  z.string().min(2).max(100),
    age:   z.number().int().min(18),
    roles: z.array(z.enum(['admin', 'user'])),
});

// Infer DTO types — never define manually
export type CreateUserDTO = z.infer<typeof createUserSchema>;
```

```typescript
// In controller
async createUser(req: Request, res: Response): Promise<void> {
    try {
        const validated = createUserSchema.parse(req.body); // throws ZodError if invalid
        const user = await this.userService.create(validated);
        this.handleSuccess(res, user, 'User created', 201);
    } catch (error) {
        const status = error instanceof z.ZodError ? 400 : 500;
        this.handleError(error, res, 'createUser', status);
    }
}
```

**Rules:**
- Use `schema.parse()` (throws) in synchronous paths
- Use `schema.safeParse()` when you need to inspect errors without throwing
- Always export `z.infer<typeof schema>` as the DTO type — never duplicate type definitions
- Validate: request body, query params, route params, webhook payloads

---

## Services — Business Logic

```typescript
// services/userService.ts
import { ConflictError, NotFoundError, ValidationError } from '../types/errors';
import { userRepository } from '../repositories/UserRepository';
import type { CreateUserDTO, UpdateUserDTO, User } from '../types/user.types';

export class UserService {
    async create(data: CreateUserDTO): Promise<User> {
        // Business rule: age
        if (data.age < 18) throw new ValidationError('User must be 18 or older');

        // Business rule: email uniqueness
        if (await userRepository.emailExists(data.email)) {
            throw new ConflictError('Email already in use');
        }

        return userRepository.create(data);
    }

    async getById(id: string): Promise<User> {
        const user = await userRepository.findById(id);
        if (!user) throw new NotFoundError(`User not found: ${id}`);
        return user;
    }
}
```

**Rules:**
- Services are framework-agnostic — no `Request`/`Response` imports
- Throw **typed, meaningful errors** (`ConflictError`, `NotFoundError`) — never `throw new Error('error')`
- One service = one domain. No God services. Extract `PermissionService`, `AuditService`, etc.
- Use constructor DI or singleton export — never call Prisma directly in a service

---

## Repositories — Data Access

```typescript
// repositories/UserRepository.ts
import { PrismaService } from '@org/database';
import type { User, Prisma } from '@prisma/client';

export class UserRepository {
    async findById(id: string): Promise<User | null> {
        return PrismaService.main.user.findUnique({
            where: { id },
            select: { id: true, email: true, name: true, isActive: true }, // Always project
        });
    }

    async emailExists(email: string): Promise<boolean> {
        const count = await PrismaService.main.user.count({ where: { email } });
        return count > 0;
    }

    async create(data: Prisma.UserCreateInput): Promise<User> {
        return PrismaService.main.user.create({ data });
    }
}

export const userRepository = new UserRepository();
```

**Rules:**
- Always `select` only needed fields on read paths — never `findMany()` with full objects on list endpoints
- Never use `include` with unbounded depth — load only what the caller needs
- N+1 prevention: load related data in a single query via `include` or batch `findMany({ where: { id: { in: ids } } })`
- Use `$transaction(async (tx) => {...})` for any multi-step write operation

---

## Async & Error Handling

```typescript
// ✅ All async route handlers MUST be wrapped
export function asyncErrorWrapper(
    handler: (req: Request, res: Response, next: NextFunction) => Promise<any>
) {
    return async (req: Request, res: Response, next: NextFunction) => {
        try { await handler(req, res, next); }
        catch (error) { next(error); }
    };
}

// ✅ Custom typed errors
export class AppError extends Error {
    constructor(message: string, public code: string, public statusCode: number) {
        super(message);
        this.name = this.constructor.name;
    }
}
export class NotFoundError  extends AppError { constructor(m: string) { super(m, 'NOT_FOUND', 404); } }
export class ConflictError  extends AppError { constructor(m: string) { super(m, 'CONFLICT', 409); } }
export class ForbiddenError extends AppError { constructor(m: string) { super(m, 'FORBIDDEN', 403); } }
export class ValidationError extends AppError { constructor(m: string) { super(m, 'VALIDATION', 400); } }

// ✅ Global error boundary middleware (register AFTER all routes)
export function errorBoundary(error: Error, req: Request, res: Response, next: NextFunction): void {
    const statusCode = error instanceof AppError ? error.statusCode : 500;
    Sentry.withScope((scope) => {
        scope.setLevel(statusCode >= 500 ? 'error' : 'warning');
        scope.setTag('error_type', error.name);
        Sentry.captureException(error);
    });
    res.status(statusCode).json({
        success: false,
        error: { message: error instanceof AppError ? error.message : 'Internal server error', code: error.name },
    });
}
```

**Anti-patterns:**
- ❌ `somePromise()` without await — fire-and-forget without `.catch()` is forbidden
- ❌ Empty catch blocks: `catch (e) {}` — always log + rethrow or handle explicitly
- ❌ `.then().catch()` chains — use `async/await` for readability
- ❌ `Promise.all` without a try-catch wrapper

---

## Middleware Ordering (Critical)

```typescript
// app.ts — ORDER IS MANDATORY
app.use(Sentry.Handlers.requestHandler()); // 1. Sentry — FIRST
app.use(express.json());                   // 2. Body parsing
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());                   // 3. Cookies
app.use(SSOMiddleware.initialize());       // 4. Auth init

// 5. Routes
app.use('/api/users', userRoutes);

app.use(errorBoundary);                    // 6. Error handler — AFTER routes
app.use(Sentry.Handlers.errorHandler());   // 7. Sentry errors — LAST
```

---

## Audit Context — AsyncLocalStorage Pattern

Pass user/request context through the entire call stack without parameter drilling:

```typescript
// middleware/auditMiddleware.ts
import { AsyncLocalStorage } from 'async_hooks';
import { v4 as uuidv4 } from 'uuid';

export interface AuditContext {
    userId: string;
    tenantId?: string;
    requestId: string;
    timestamp: Date;
}

export const auditStorage = new AsyncLocalStorage<AuditContext>();

export function auditMiddleware(req: Request, res: Response, next: NextFunction): void {
    auditStorage.run({
        userId:    res.locals.effectiveUserId || 'anonymous',
        tenantId:  res.locals.claims?.tenantId,
        requestId: req.id || uuidv4(),
        timestamp: new Date(),
    }, next);
}

// Accessible from anywhere in the call stack
export const getAuditContext = (): AuditContext | null => auditStorage.getStore() ?? null;
```

```typescript
// In any service, without needing the context passed as a parameter
import { getAuditContext } from '../middleware/auditMiddleware';

async function someOperation() {
    const ctx = getAuditContext();
    logger.info('Operation by user %s (tenant %s)', ctx?.userId, ctx?.tenantId);
}
```

---

## Configuration — Typed & Validated at Startup

```typescript
// ❌ NEVER
const secret = process.env.JWT_SECRET;

// ✅ ALWAYS
import { config } from './config/unifiedConfig';
const secret = config.tokens.jwt; // typed, validated at startup, throws if missing
```

```typescript
// config/unifiedConfig.ts
import * as fs from 'fs';
import * as ini from 'ini';

const raw = ini.parse(fs.readFileSync('config.ini', 'utf-8'));

export const config = {
    server: {
        port: parseInt(raw.server?.port || process.env.PORT || '3000'),
    },
    tokens: {
        jwt: raw.tokens?.jwt || process.env.JWT_SECRET || (() => { throw new Error('JWT_SECRET not configured'); })(),
    },
    database: {
        url: raw.database?.url || process.env.DATABASE_URL || '',
    },
};
```

**Precedence:** config.ini → environment variables → hard defaults → throw on missing critical values.

---

## Observability — Sentry (PII-Safe)

```typescript
// instrument.ts — MUST be the first import in server.ts
import * as Sentry from '@sentry/node';

Sentry.init({
    dsn: config.sentry.dsn,
    environment: process.env.NODE_ENV || 'development',
    tracesSampleRate: 0.1,
    integrations: [
        Sentry.extraErrorDataIntegration({ depth: 5 }),
        Sentry.prismaIntegration(),
    ],
    beforeSend(event) {
        // Scrub PII before sending
        if (event.request?.url?.includes('/health')) return null; // Filter noise
        if (event.request?.headers) {
            delete event.request.headers['authorization'];
            delete event.request.headers['cookie'];
        }
        if (event.user?.email) {
            // Mask email: "te***@example.com"
            event.user.email = event.user.email.replace(/^(.{2}).*(@.*)$/, '$1***$2');
        }
        return event;
    },
});
```

**Mandatory rules:**
- Sentry `instrument.ts` is the FIRST import in `server.ts` and all cron job entry points
- Never log raw `password`, `token`, `cookie`, `authorization` values
- Always mask email before logging: `user@domain.com` → `us***@domain.com`
- Tag every error with `service` and `operation` for dashboard filtering

---

## Testing Discipline

See `@test-driven-development` for the Iron Law. Node.js-specific conventions:

```typescript
// Unit test — mock repository, test business logic
describe('UserService.create', () => {
    it('throws ConflictError when email already exists', async () => {
        jest.spyOn(userRepository, 'emailExists').mockResolvedValue(true);
        await expect(service.create({ email: 'dup@test.com', name: 'Test', age: 20, roles: ['user'] }))
            .rejects.toThrow(ConflictError);
    });

    it('creates user when email is unique', async () => {
        jest.spyOn(userRepository, 'emailExists').mockResolvedValue(false);
        jest.spyOn(userRepository, 'create').mockResolvedValue({ id: '1', email: 'new@test.com' } as any);
        const user = await service.create({ email: 'new@test.com', name: 'Test', age: 20, roles: ['user'] });
        expect(user.email).toBe('new@test.com');
    });
});
```

**Coverage targets:**
- Unit tests on all service business rules (≥80% coverage of services/)
- Integration tests on critical routes (happy path + 401/403/400/404 paths)
- Repository tests for complex queries

---

## Anti-Patterns (Immediate Rejection)

| Anti-Pattern | Why It's Wrong |
| --- | --- |
| Business logic in routes | Untestable, unreadable, violates SRP |
| Direct Prisma calls in controllers | Skips repository layer, breaks testability |
| `process.env` used directly in app code | No type safety, no validation, scattered |
| Empty catch blocks | Silent failures are production incidents |
| God service with 20+ methods | Violates SRP, impossible to test in isolation |
| `console.log` instead of Sentry | No persistence, no alerting, lost in logs |
| Missing Zod validation | Trust no external input — ever |
| Fire-and-forget without `.catch()` | Unhandled promise rejection crashes Node.js |

---

## Resources

Detailed guides in `resources/`:
- [architecture-overview.md](resources/architecture-overview.md) — Layer diagram, request lifecycle, module organization
- [async-and-errors.md](resources/async-and-errors.md) — Async patterns, custom error types, error propagation
- [validation-patterns.md](resources/validation-patterns.md) — Zod schemas, DTO patterns, advanced composition
- [services-and-repositories.md](resources/services-and-repositories.md) — DI patterns, singleton, caching strategies
- [routing-and-controllers.md](resources/routing-and-controllers.md) — BaseController, refactoring anti-patterns
- [database-patterns.md](resources/database-patterns.md) — Prisma transactions, N+1 prevention, query optimization
- [sentry-and-monitoring.md](resources/sentry-and-monitoring.md) — Full Sentry setup, performance spans, cron monitoring
- [configuration.md](resources/configuration.md) — UnifiedConfig pattern, environment precedence, secrets
- [testing-guide.md](resources/testing-guide.md) — Unit/integration/mock strategies, coverage targets

## Delegation

| Need | Use Instead |
| --- | --- |
| C# equivalent patterns | `dotnet-patterns` + `csharp-reviewer` |
| Resilience (retry, circuit breaker) | `resilience-patterns` |
| API contract design | `api-design` |
| Deep security audit | `securities-audit` + `backend-security-coder` |
| E2E testing | `e2e-testing` |
| Deployment pipelines | `ci-cd-and-automation` |
