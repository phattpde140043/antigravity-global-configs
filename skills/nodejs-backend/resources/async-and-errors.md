# Async Patterns & Error Handling

## Custom Error Hierarchy

```typescript
// types/errors.ts
export class AppError extends Error {
    constructor(message: string, public code: string, public statusCode: number, public isOperational = true) {
        super(message);
        this.name = this.constructor.name;
        Error.captureStackTrace(this, this.constructor);
    }
}

export class ValidationError extends AppError { constructor(m: string) { super(m, 'VALIDATION_ERROR', 400); } }
export class NotFoundError   extends AppError { constructor(m: string) { super(m, 'NOT_FOUND', 404); } }
export class ForbiddenError  extends AppError { constructor(m: string) { super(m, 'FORBIDDEN', 403); } }
export class ConflictError   extends AppError { constructor(m: string) { super(m, 'CONFLICT', 409); } }
export class UnauthorizedError extends AppError { constructor(m: string) { super(m, 'UNAUTHORIZED', 401); } }
```

## asyncErrorWrapper — Required for All Route Handlers

```typescript
// utils/asyncErrorWrapper.ts
export function asyncErrorWrapper(
    handler: (req: Request, res: Response, next: NextFunction) => Promise<any>
) {
    return async (req: Request, res: Response, next: NextFunction) => {
        try { await handler(req, res, next); }
        catch (error) { next(error); } // Passes to errorBoundary middleware
    };
}
```

## Parallel Operations

```typescript
// ✅ Promise.all — fails fast if any throws
const [user, profile] = await Promise.all([
    userService.getById(id),
    profileService.getByUserId(id),
]);

// ✅ Promise.allSettled — handle each result independently
const results = await Promise.allSettled([userService.getAll(), profileService.getAll()]);
results.forEach((result, i) => {
    if (result.status === 'rejected') {
        Sentry.captureException(result.reason, { tags: { operation: ['users', 'profiles'][i] } });
    }
});
```

## Fire-and-Forget (Safe Pattern)

```typescript
// ❌ NEVER — unhandled rejection will crash Node.js
sendEmail(user.email);

// ✅ Intentional background task — always attach error handler
sendEmail(user.email).catch((err) => {
    Sentry.captureException(err, { tags: { context: 'background-email' } });
    logger.error('Background email failed', { userId: user.id, error: err.message });
});
```

## Global Safety Net

```typescript
// server.ts — always register before starting the HTTP server
process.on('unhandledRejection', (reason) => {
    Sentry.captureException(reason, { tags: { type: 'unhandled_rejection' } });
    logger.error('Unhandled Rejection:', reason);
});

process.on('uncaughtException', (error) => {
    Sentry.captureException(error, { tags: { type: 'uncaught_exception' } });
    logger.error('Uncaught Exception:', error);
    process.exit(1); // Non-recoverable — restart via process manager
});
```

## Error Propagation Pattern

```typescript
// Repositories propagate with context tags
async function repositoryOp() {
    try { return await PrismaService.main.user.findMany(); }
    catch (error) {
        Sentry.captureException(error, { tags: { layer: 'repository', op: 'findMany' } });
        throw error; // Always rethrow — never swallow
    }
}
```

**Rule:** Every layer catches, tags with context, and rethrows. The error boundary middleware is the only terminal handler.
