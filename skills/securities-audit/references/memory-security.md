# Memory Security & Data Zeroization

## 🧹 Zeroization (Secure Wiping)
Securely wipe sensitive data from memory immediately after use to prevent leaks through Memory Dumps or Cold Boot Attacks.

### Execution Rules (.NET/C#):
- **FORBIDDEN**: Storing passwords/keys in `string` types (since `string` is immutable and lingers in the Heap).
- **PREFERENCE**: Use `byte[]` or `char[]` and wipe them after use:
```csharp
// Securely wipe byte array after use
Array.Clear(sensitiveBytes, 0, sensitiveBytes.Length);
```
- **SecureString**: Use `SecureString` for highly sensitive data in RAM.

### Compiler Optimization Risks
Compilers may automatically remove (optimize away) memory clearing commands if they determine the data is no longer accessed. 
- **Solution**: Use OS-specific memory clearing methods or specialized security libraries (e.g., `CryptCleanMemory` in Windows or dedicated Cryptography libraries).

## 🛡️ Missing Zeroization on Error Paths
Vulnerabilities occur when sensitive data is cleared in successful flows but missed during Exceptions or logic failures.

**Secure Code Pattern:**
```csharp
byte[] key = GetSecret();
try 
{
    // Process key
}
finally 
{
    // Always ensure key is wiped whether success or failure
    Array.Clear(key, 0, key.Length);
}
```

## 🔍 Memory Audit Checklist
- [ ] Are all buffers containing passwords, keys, or tokens wiped (`Array.Clear`) after use?
- [ ] Are variables containing sensitive data cleared in the `finally` block?
- [ ] Is no sensitive data leaked into Logs or Error Messages?
- [ ] Have you checked for data leaks through temporary variables?
