---
name: error-resilience
description: "Chuyên gia về Observability, Error Tracking và Phục hồi hệ thống."
---

# Error Resilience & Observability

## 🎯 Mục tiêu
1. Triển khai Structured Logging và Correlation ID cho toàn hệ thống.
2. Thiết lập cơ chế tự phục hồi (Retry, Circuit Breaker).
3. Thực hiện Root Cause Analysis (RCA) chuyên sâu.

## 🛠️ Quy trình thực hiện
1. **Tracing Implementation**: Gắn Correlation ID vào mọi request header và log context.
2. **Structured Logging**: Đảm bảo log đầu ra là JSON với đầy đủ metadata (Service, Version, TraceId).
3. **Resilience Patterns**: 
    - Triển khai Exponential Backoff cho các lời gọi API.
    - Cấu hình Circuit Breaker cho các external dependencies.
4. **Investigation (RCA)**: Sử dụng phương pháp "Five Whys" và "Error Taxonomy" để phân loại lỗi (Critical, High, Medium, Low).

## 📋 Acceptance Criteria (AC)
- [ ] 100% Log là structured JSON.
- [ ] TraceId được truyền xuyên suốt các service (Propagation).
- [ ] Các điểm rủi ro (Network/DB) có cơ chế Retry/Breaker.
