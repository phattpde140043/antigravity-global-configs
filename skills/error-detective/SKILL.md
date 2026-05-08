---
name: error-detective
description: "Săn tìm lỗi qua Log, Stack trace và Anomaly Detection."
---

# Error Detective

## 🎯 Mục tiêu
1. Truy quét lỗi qua Log patterns (Regex).
2. Phân tích Stack trace đa ngôn ngữ và phân loại lỗi ngầm.
3. Phát hiện Anomaly và Correlation giữa các hệ thống.

## 🛠️ Quy trình thực hiện
1. **Log Parsing**: Sử dụng Regex để trích xuất thông tin từ log thô.
2. **Correlation Analysis**: Đối soát lỗi giữa Frontend (RUM) và Backend dựa trên Correlation ID.
3. **Fingerprinting**: Nhận diện các mẫu lỗi lặp lại và tạo cảnh báo (Alerting rules).
4. **Timeline Reconstruction**: Xây dựng lại dòng thời gian sự kiện dẫn đến lỗi (Audit trail).

## 📋 Acceptance Criteria (AC)
- [ ] Xác định được Root Cause kèm bằng chứng Log/Trace.
- [ ] Có kịch bản tái hiện lỗi (Reproduction steps).
- [ ] Đề xuất được giải pháp ngăn ngừa (Prevention strategy).
