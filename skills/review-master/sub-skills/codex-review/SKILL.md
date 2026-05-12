---
name: codex-review
description: "Expert in changelog management (CHANGELOG) and commit conventions (Conventional Commits). Integrates Codex AI reasoning to review large-scale refactoring."
category: development
metadata:
  triggers: [changelog, conventional-commits, refactoring-review, commit-message]
---

# Codex Review & Changelog Specialist

## 🎯 Objectives
1. Ensure all source code changes are recorded in `CHANGELOG.md` automatically and professionally.
2. Maintain the quality of commit messages (Conventional Commits).
3. Support the review of large-scale refactorings.

## 🛠️ Execution Workflow
1. **Diff Scan**: Analyze major changes in logic, features, or bug fixes.
2. **Categorization**: Categorize changes into: `feat`, `fix`, `refactor`, `perf`, `docs`, `chore`.
3. **CHANGELOG Update**: 
    - Verify the existence of `CHANGELOG.md` at the project root.
    - Insert the latest changes at the top of the file in the standard format.
4. **Commit Message Validation**: Ensure compliance with the structure: `<type>(scope): <description>`.

## 📋 Acceptance Criteria (AC)
- [ ] `CHANGELOG.md` is updated to match actual changes.
- [ ] Suggested commit messages comply with Conventional Commits (feat, fix, refactor...).
- [ ] Large-scale refactorings are explained with "Why" rather than just "What."
