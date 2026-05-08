---
name: codex-review
description: "Chuyên gia quản lý lịch sử thay đổi (CHANGELOG) và quy ước commit (Conventional Commits). Tích hợp tư duy Codex AI để review các đợt refactoring lớn."
---

# Codex Review & Changelog Specialist

## 🎯 Mục tiêu
1. Đảm bảo mọi thay đổi mã nguồn đều được ghi lại trong `CHANGELOG.md` một cách tự động và chuyên nghiệp.
2. Kiểm soát chất lượng thông điệp commit (Conventional Commits).
3. Hỗ trợ review các đợt Refactoring quy mô lớn (Large-scale refactoring).

## 🛠️ Quy trình thực hiện
1. **Quét thay đổi (Diff Scan)**: Phân tích các thay đổi chính trong logic, tính năng hoặc sửa lỗi.
2. **Phân loại (Categorization)**: Chia thay đổi thành: `feat`, `fix`, `refactor`, `perf`, `docs`, `chore`.
3. **Cập nhật CHANGELOG**: 
    - Kiểm tra sự tồn tại của `CHANGELOG.md` tại root dự án.
    - Chèn nội dung thay đổi mới nhất vào đầu file theo định dạng chuẩn.
4. **Kiểm tra Commit Message**: Đảm bảo tuân thủ cấu trúc: `<type>(scope): <description>`.

## 📋 Acceptance Criteria (AC)
- [ ] `CHANGELOG.md` được cập nhật khớp với các thay đổi thực tế.
- [ ] Commit message gợi ý tuân thủ Conventional Commits (feat, fix, refactor...).
- [ ] Các thay đổi Refactoring lớn được giải thích rõ "Tại sao" thay vì chỉ "Cái gì".
