# Production Readiness Checklist

## Health Checks

Every service MUST expose health check endpoints:

```csharp
// ASP.NET Core Health Checks
builder.Services.AddHealthChecks()
    .AddCheck("self", () => HealthCheckResult.Healthy())
    .AddCheck<DatabaseHealthCheck>("database")
    .AddCheck<ExternalServiceHealthCheck>("external-api");

app.MapHealthChecks("/health", new HealthCheckOptions
{
    ResponseWriter = UIResponseWriter.WriteHealthCheckUIResponse
});

app.MapHealthChecks("/health/ready", new HealthCheckOptions
{
    Predicate = check => check.Tags.Contains("ready")
});

app.MapHealthChecks("/health/live", new HealthCheckOptions
{
    Predicate = _ => false // Just checks the app is running
});
```

## Infrastructure Injection Pattern

### Correlation ID Middleware
```csharp
public class CorrelationIdMiddleware
{
    public async Task InvokeAsync(HttpContext context, RequestDelegate next)
    {
        var correlationId = context.Request.Headers["X-Correlation-Id"].FirstOrDefault()
            ?? Guid.NewGuid().ToString();
        context.Items["CorrelationId"] = correlationId;
        context.Response.Headers["X-Correlation-Id"] = correlationId;
        using (LogContext.PushProperty("CorrelationId", correlationId))
        {
            await next(context);
        }
    }
}
```

## Deployment Checklist

- [ ] Health check endpoints configured (`/health`, `/health/ready`, `/health/live`)
- [ ] Structured logging with correlation IDs
- [ ] Graceful shutdown handling (`IHostApplicationLifetime`)
- [ ] Connection string from secure config (Key Vault / env vars)
- [ ] HTTPS enforced (HSTS headers)
- [ ] Rate limiting configured
- [ ] Response caching where appropriate
- [ ] Compression middleware enabled
- [ ] Exception handling middleware (no stack traces in production)
- [ ] Metrics endpoint for monitoring
