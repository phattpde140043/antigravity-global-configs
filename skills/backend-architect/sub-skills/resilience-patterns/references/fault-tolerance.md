# Fault Tolerance Patterns: Retry & Circuit Breaker

## 🔄 Retry with Exponential Backoff
- **Concept**: Automatically retry transient failures with increasing wait times to avoid overloading the target system.
- **Rules**:
    - Max retries: 3-5 times.
    - Base delay: 1s, 2s, 4s...
    - **Jitter**: Add a small random delay to prevent "Thundering Herd" effects.

**ASP.NET Core (Polly):**
```csharp
var retryPolicy = HttpPolicyExtensions
    .HandleTransientHttpError()
    .WaitAndRetryAsync(3, retryAttempt => 
        TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));
```

## 🔌 Circuit Breaker
- **Concept**: Disconnect when a service repeatedly fails to protect the system and allow the target service time to recover.
- **States**:
    - **Closed**: Normal state, requests flow through.
    - **Open**: Service failure exceeds threshold, all requests blocked immediately.
    - **Half-Open**: Trialing a few requests to check if the service has recovered.

**Polly Implementation:**
```csharp
var circuitBreakerPolicy = HttpPolicyExtensions
    .HandleTransientHttpError()
    .CircuitBreakerAsync(5, TimeSpan.FromSeconds(30));
```
