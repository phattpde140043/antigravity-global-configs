# SAST Analysis Patterns (Security Check)

Use these patterns to identify potential security vulnerabilities during static analysis.

## 🚩 SQL Injection (SQLi)
- **Bad Pattern**: `var sql = "SELECT * FROM Users WHERE Name = '" + userInput + "'";`
- **Good Pattern**: Use parameterized queries or ORMs (EF Core/Dapper).

## 🚩 Cross-Site Scripting (XSS)
- **Bad Pattern**: `innerHtml = userInput;`
- **Good Pattern**: Use `.textContent` or template engines that auto-escape.

## 🚩 Broken Authorization (BOLA)
- **Bad Pattern**: `GET /api/orders/{id}` without checking if the ID belongs to the current user.
- **Good Pattern**: `WHERE Id = @id AND UserId = @currentUserId`.

## 🚩 Insecure Secrets
- **Bad Pattern**: `var apiKey = "12345-abcde";` (Hardcoded)
- **Good Pattern**: Use `Environment.GetEnvironmentVariable("API_KEY")`.

## 🚩 Path Traversal
- **Bad Pattern**: `File.OpenRead("/data/" + userInput);`
- **Good Pattern**: Sanitize paths and use `Path.GetFileName()` to prevent `../` attacks.
