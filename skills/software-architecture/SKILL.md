---
name: software-architecture
description: "Kiến trúc phần mềm chuẩn Clean Architecture & DDD."
---

# Software Architecture Excellence

## 🎯 Mục tiêu
1. Đảm bảo tính module hóa và tách biệt trách nhiệm (SoC).
2. Áp dụng Library-First (Sử dụng thư viện thay vì tự code thủ công các utils).
3. Kiểm soát độ phức tạp mã nguồn qua các giới hạn cứng (Limit check).

## 🛠️ Quy tắc thực thi
1. **Naming Standard**: 
    - CẤM: `utils`, `helpers`, `common`, `shared`.
    - NÊN: `OrderCalculator`, `InvoiceGenerator`, `AuthService`.
2. **Code Limits**: 
    - Function: < 50 lines.
    - File: < 200 lines.
    - Nesting: Max 3 levels.
3. **Coding Style**:
    - Ưu tiên **Early Return**.
    - Sử dụng Arrow functions khi có thể.
4. **Library-First Policy**: 
    - Kiểm tra thư viện chuẩn (npm/nuget) trước khi tự viết logic xử lý chung (Retry, Validation, Mapping).

## 📋 Acceptance Criteria (AC)
- [ ] Không có file nào vượt quá 200 dòng.
- [ ] Tên module phản ánh đúng nghiệp vụ (Domain-specific).
- [ ] Không có logic lồng nhau quá 3 cấp.
