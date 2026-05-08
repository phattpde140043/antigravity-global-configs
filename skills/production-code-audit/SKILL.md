---
name: production-code-audit
description: "Tự động quét toàn bộ codebase và biến đổi mã nguồn thành chuẩn Corporate/Enterprise."
---

# Production Code Audit & Transformation

## 🎯 Mục tiêu
1. Thấu hiểu toàn bộ dự án một cách tự trị (Autonomous Discovery).
2. Sửa lỗi và tối ưu hóa trực tiếp (Security, Performance, Quality).
3. Trang bị hạ tầng vận hành Production (Logging, Monitoring, Health Checks, CI/CD).

## 🛠️ Quy trình thực hiện
1. **Discovery (Autonomous)**: 
    - Quét toàn bộ cây thư mục để nhận diện Tech Stack.
    - Đọc file cấu hình chính để hiểu ranh giới hệ thống.
    - Xác định Entry points và Data flow.
2. **Comprehensive Issue Detection**: 
    - Quét line-by-line tìm lỗi: God classes, SQLi, N+1 Query, Magic numbers, Testing gaps.
3. **Automatic Transformation**: 
    - Refactor kiến trúc (Tách God classes).
    - Hardening bảo mật (Parameterized queries, Secret removal).
    - Performance Tuning (Caching, Indexing, Algorithm optimization).
4. **Infra-Injection**:
    - Thêm Middleware (Logging, Error handling).
    - Thêm Endpoints (/health, /ready).
    - Thêm tài liệu (README chuyên nghiệp, API Docs).
5. **Validation & Metrics**: So sánh chỉ số Before/After.

## 📋 Acceptance Criteria (AC)
- [ ] Codebase đạt chuẩn Enterprise (Grade A/B).
- [ ] 0 lỗi Security Critical/High.
- [ ] Có đầy đủ hạ tầng quan sát (Observability).
- [ ] Chỉ số hiệu năng được cải thiện rõ rệt.
