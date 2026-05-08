---
name: differential-review
description: "Security-focused code review tập trung vào Blast Radius và Git History."
---

# Differential Security Review

## 🎯 Mục tiêu
1. Phân tích rủi ro dựa trên lịch sử commit (Git Blame/History).
2. Tính toán Blast Radius (Bán kính ảnh hưởng) cho các thay đổi HIGH-RISK.
3. Áp dụng chiến lược Review thích ứng:
    - SMALL (<20 files): DEEP (Đọc toàn bộ deps).
    - MEDIUM (20-200 files): FOCUSED (1-hop deps).
    - LARGE (200+ files): SURGICAL (Chỉ critical paths).

## 🛠️ Quy trình thực hiện
1. **Triage**: Phân loại mức độ rủi ro (HIGH: Auth/Crypto, MEDIUM: Logic, LOW: UI/Docs).
2. **Git Analysis**: Kiểm tra code bị xóa có phải là security fix trước đó không.
3. **Blast Radius**: Xác định các transitive callers. Nếu Blast Radius > 50 ➔ Nâng mức độ rủi ro.
4. **Adversarial Modeling**: Xây dựng kịch bản tấn công (Exploit scenarios) thực tế.

## 📋 Acceptance Criteria (AC)
- [ ] Báo cáo có phân tích Blast Radius cho các thay đổi nhạy cảm.
- [ ] Mọi lỗ hổng đều có kịch bản tấn công minh họa.
