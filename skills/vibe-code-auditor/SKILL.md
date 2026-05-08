---
name: vibe-code-auditor
description: "Kiểm định code AI/Prototype, phát hiện technical debt và chấm điểm Readiness."
---

# Vibe Code Auditor

## 🎯 Mục tiêu
1. Phát hiện code "vibe" (thiếu cấu trúc), code ảo (hallucination).
2. Kiểm tra độ bền (Robustness): bare except, missing timeouts.
3. Chấm điểm Production Readiness (0-100).

## 🛠️ Quy trình thực hiện
1. **Pattern Recognition**: 
    - Tìm `eval()`, `exec()`, bare `except:`.
    - Tìm N+1 query, unbounded loops.
2. **Hallucination Check**: Xác thực các thư viện và API (đảm bảo không gọi method ảo).
3. **Readiness Scoring**:
    - Start: 100đ.
    - Critical: -15đ.
    - High: -8đ.
    - Medium: -3đ.
    - Pervasive patterns: -5đ.

## 📋 Acceptance Criteria (AC)
- [ ] Báo cáo có chỉ số Production Readiness Score.
- [ ] Không còn "AI Slop" (comment thừa, placeholder).
- [ ] Mọi lời gọi API/Thư viện đều tồn tại thực tế.
