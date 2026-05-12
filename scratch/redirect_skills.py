import os

redirects = {
    # Security -> security-master
    "backend-security-coder": "security-master",
    "infrastructure-security": "security-master",
    "penetration-testing": "security-master",
    "securities-audit": "security-master",
    "security-and-hardening": "security-master",
    "security-auditor": "security-master",
    "security-checklists": "security-master",
    "security-design": "security-master",
    "security-review": "security-master",
    
    # Testing -> senior-qa
    "e2e-testing": "senior-qa",
    "test-engineer": "senior-qa",
    "test-generator": "senior-qa",
    "testing-anti-patterns": "senior-qa",
    "testing-workflow": "senior-qa",
    "python-unit-testing": "senior-qa",
    "frontend-unit-testing": "senior-qa",
    
    # Review -> review-master
    "code-review-excellence": "review-master",
    "code-reviewer": "review-master",
    "codex-review": "review-master",
    "csharp-reviewer": "review-master",
    "differential-review": "review-master",
    "pr-review": "review-master",
    "vibe-code-auditor": "review-master",
    
    # Architecture -> backend-architect
    "architect": "backend-architect",
    "architecture-design": "backend-architect",
    "code-architect": "backend-architect",
    "software-architecture": "backend-architect",
}

skills_dir = "/Users/macos/.antigravity-global/skills/"

for old_skill, new_skill in redirects.items():
    skill_path = os.path.join(skills_dir, old_skill, "SKILL.md")
    if os.path.exists(skill_path):
        content = f"""---
name: {old_skill}
description: "DEPRECATED. This skill has been consolidated into `{new_skill}`. Please refer to `{new_skill}` for the latest standards and instructions."
metadata:
  deprecated: true
  successor: {new_skill}
---

# 🛑 DEPRECATED: {old_skill}

This skill has been merged into the **[{new_skill}](../{new_skill}/SKILL.md)** master discipline to ensure systemic consistency and reduce context noise.

**Action Required**:
- Update your triggers to use `{new_skill}`.
- All existing standards, code patterns, and instructions from this skill have been preserved in the successor.
"""
        with open(skill_path, "w") as f:
            f.write(content)
        print(f"Redirected {old_skill} to {new_skill}")
    else:
        print(f"Skipped {old_skill} (not found)")
