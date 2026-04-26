# Validation Patterns — Zod

## Why Zod

- ✅ Full TypeScript inference — schema IS the type definition
- ✅ Runtime + compile-time validation in one declaration
- ✅ Composable: merge, extend, pick, omit
- ✅ Transform & preprocess support

## Core Patterns

```typescript
import { z } from 'zod';

// --- Primitives ---
const emailSchema   = z.string().email();
const uuidSchema    = z.string().uuid();
const positiveInt   = z.number().int().positive();
const isoDateSchema = z.string().datetime(); // ISO 8601

// --- Objects with DTO inference ---
export const createUserSchema = z.object({
    email:  z.string().email(),
    name:   z.string().min(2).max(100),
    age:    z.number().int().min(18).max(120),
    roles:  z.array(z.enum(['admin', 'user'])).nonempty(),
});
export type CreateUserDTO = z.infer<typeof createUserSchema>; // Never define this manually

// --- Optional & Nullable ---
export const updateUserSchema = z.object({
    email: z.string().email().optional(),
    name:  z.string().min(2).max(100).optional(),
});
export type UpdateUserDTO = z.infer<typeof updateUserSchema>;
```

## Advanced Patterns

```typescript
// --- Cross-field validation with refine ---
const dateRangeSchema = z.object({
    startsAt:  z.string().datetime(),
    expiresAt: z.string().datetime(),
}).refine(
    (data) => new Date(data.expiresAt) > new Date(data.startsAt),
    { message: 'expiresAt must be after startsAt', path: ['expiresAt'] }
);

// --- Discriminated union ---
const notificationSchema = z.discriminatedUnion('type', [
    z.object({ type: z.literal('email'), recipient: z.string().email(), subject: z.string() }),
    z.object({ type: z.literal('sms'),   phoneNumber: z.string(), message: z.string() }),
]);

// --- Preprocess (sanitize before validate) ---
const sanitizedEmailSchema = z.object({
    email: z.preprocess(
        (val) => typeof val === 'string' ? val.trim().toLowerCase() : val,
        z.string().email()
    ),
});

// --- Schema composition ---
const timestampsSchema = z.object({ createdAt: z.string().datetime(), updatedAt: z.string().datetime() });
const auditSchema      = z.object({ createdBy: z.string(), updatedBy: z.string() });
const fullEntitySchema = z.object({ id: z.string().uuid(), name: z.string() })
    .merge(timestampsSchema)
    .merge(auditSchema);
```

## Validation Middleware Pattern

```typescript
// Reusable middleware factory
export function validateBody<T extends z.ZodType>(schema: T) {
    return (req: Request, res: Response, next: NextFunction): void => {
        const result = schema.safeParse(req.body);
        if (!result.success) {
            res.status(400).json({
                success: false,
                error: {
                    message: 'Validation failed',
                    details: result.error.errors.map((e) => ({
                        field: e.path.join('.'),
                        message: e.message,
                    })),
                },
            });
            return;
        }
        req.body = result.data; // Replace with validated + transformed data
        next();
    };
}

// Usage in route
router.post('/', validateBody(createUserSchema), (req, res) => controller.createUser(req, res));
```

## Error Formatting Helper

```typescript
export function formatZodError(error: z.ZodError) {
    return {
        message: 'Validation failed',
        errors: error.errors.map((e) => ({ field: e.path.join('.'), message: e.message, code: e.code })),
    };
}
```
