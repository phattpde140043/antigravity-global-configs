# Database Patterns — Prisma

## Repository Pattern

### When to Use a Repository

| Use Repository | Skip Repository |
| --- | --- |
| Complex queries with joins/includes | Simple one-off queries in scripts |
| Query reused in multiple places | Prototyping (can refactor later) |
| Need caching layer | |
| Want to mock for testing | |

### Repository Template

```typescript
// repositories/UserRepository.ts
import { PrismaService } from '@org/database';
import type { User, Prisma } from '@prisma/client';

export class UserRepository {
    async findById(id: string): Promise<User | null> {
        return PrismaService.main.user.findUnique({
            where: { id },
            select: { id: true, email: true, name: true, isActive: true, roles: true }, // Always project
        });
    }

    async findActive(orderBy?: Prisma.UserOrderByWithRelationInput): Promise<User[]> {
        return PrismaService.main.user.findMany({
            where: { isActive: true },
            orderBy: orderBy ?? { name: 'asc' },
            select: { id: true, email: true, name: true },
        });
    }

    async emailExists(email: string): Promise<boolean> {
        const count = await PrismaService.main.user.count({ where: { email } });
        return count > 0;
    }

    async create(data: Prisma.UserCreateInput): Promise<User> {
        return PrismaService.main.user.create({ data });
    }

    async update(id: string, data: Prisma.UserUpdateInput): Promise<User> {
        return PrismaService.main.user.update({ where: { id }, data });
    }

    async softDelete(id: string): Promise<User> {
        return PrismaService.main.user.update({
            where: { id },
            data: { isActive: false, deletedAt: new Date() },
        });
    }
}

export const userRepository = new UserRepository();
```

## Transactions

```typescript
// Simple transaction
const result = await PrismaService.main.$transaction(async (tx) => {
    const user    = await tx.user.create({ data: userData });
    const profile = await tx.userProfile.create({ data: { userId: user.id, ...profileData } });
    return { user, profile };
});

// Interactive transaction with timeout
const result = await PrismaService.main.$transaction(
    async (tx) => {
        const user = await tx.user.findUnique({ where: { id } });
        if (!user) throw new NotFoundError('User not found');
        return tx.user.update({ where: { id }, data: { lastLogin: new Date() } });
    },
    { maxWait: 5000, timeout: 10000 }
);
```

## N+1 Prevention

```typescript
// ❌ N+1 — 1 query for users + N queries for profiles
const users = await PrismaService.main.user.findMany();
for (const user of users) {
    const profile = await PrismaService.main.profile.findUnique({ where: { userId: user.id } });
}

// ✅ Single query with include
const users = await PrismaService.main.user.findMany({ include: { profile: true } });

// ✅ Or batch query (when include would over-fetch)
const userIds = users.map(u => u.id);
const profiles = await PrismaService.main.profile.findMany({ where: { userId: { in: userIds } } });
```

## Query Projection (Always)

```typescript
// ❌ Returns all columns — wasteful, may expose sensitive fields
const users = await PrismaService.main.user.findMany();

// ✅ Only what the caller needs
const users = await PrismaService.main.user.findMany({
    select: { id: true, email: true, profile: { select: { firstName: true, lastName: true } } },
});
```

## Prisma Error Handling

```typescript
import { Prisma } from '@prisma/client';

try {
    await PrismaService.main.user.create({ data });
} catch (error) {
    if (error instanceof Prisma.PrismaClientKnownRequestError) {
        if (error.code === 'P2002') throw new ConflictError('Duplicate value — unique constraint violated');
        if (error.code === 'P2025') throw new NotFoundError('Record not found');
        if (error.code === 'P2003') throw new ValidationError('Invalid foreign key reference');
    }
    Sentry.captureException(error);
    throw error;
}
```

## Prisma Error Codes Reference

| Code | Meaning | Map To |
| --- | --- | --- |
| P2002 | Unique constraint violation | `ConflictError` |
| P2003 | Foreign key constraint | `ValidationError` |
| P2025 | Record not found | `NotFoundError` |
| P2024 | Connection pool timeout | Retry / `503` |
