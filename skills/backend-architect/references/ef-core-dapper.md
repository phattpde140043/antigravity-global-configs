# EF Core & Dapper: High Performance Data Access

## 🚀 Entity Framework Core (EF Core 8+)
- **AsNoTracking()**: Always use for read-only queries.
- **Split Queries**: Use `.AsSplitQuery()` when there are multiple `.Include()` calls to avoid "Cartesian Explosion".
- **Compiled Queries**: Use for frequently repeated high-frequency queries.
- **ExecuteUpdate / ExecuteDelete**: Perform bulk updates/deletes directly at the Database level without loading entities into memory.
- **Global Query Filters**: Automatically apply filters like `IsDeleted = false` or `TenantId = X`.
- **Interceptors**: Use to automatically populate `CreatedAt`, `UpdatedAt`, or log slow SQL.

## ⚡ Dapper (Micro-ORM)
- **When to Use**: Use for performance-critical queries or when specific SQL features (CTE, Window Functions) are required.
- **Multi-Mapping**: Map results from multiple joined tables into complex object graphs.
- **Dynamic Parameters**: Build dynamic SQL statements safely.
- **Table-Valued Parameters (TVP)**: Send lists of IDs or large datasets to the Database in a single round-trip.

## 🔄 Transaction Management
- **Unit of Work**: Ensure all data changes in a single request are committed or rolled back together.
- **Isolation Levels**: Choose appropriate isolation levels (ReadCommitted is default, Snapshot for heavy reporting).

## 🚩 N+1 Prevention Checklist
- [ ] Are related data items fetched using `.Include()`?
- [ ] No database queries inside `foreach` loops?
- [ ] Using `Select` to fetch only required columns?
- [ ] Checked SQL logs to confirm the actual number of queries?
