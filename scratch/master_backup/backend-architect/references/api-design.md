# API Design Principles

## 🏗️ RESTful Standards
- **Resource-based URLs**: Use nouns, not verbs (e.g., `/users`, not `/getUsers`).
- **HTTP Methods**:
    - `GET`: Retrieve resource.
    - `POST`: Create resource.
    - `PUT`: Replace resource.
    - `PATCH`: Partially update resource.
    - `DELETE`: Remove resource.
- **Status Codes**:
    - `200 OK`, `201 Created`.
    - `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`.
    - `500 Internal Server Error`.

## 📄 Documentation
- **OpenAPI / Swagger**: Every API must have an up-to-date Swagger specification.
- **Breaking Changes**: Use versioning (e.g., `/v1/`, `/v2/`) to avoid breaking existing clients.

## 🚀 Performance
- **Pagination**: Always use `limit` and `offset` (or cursor-based) for collection endpoints.
- **Filtering & Sorting**: Use query parameters (e.g., `?sort=name&order=desc`).
- **Compression**: Enable Gzip/Brotli compression for large payloads.
