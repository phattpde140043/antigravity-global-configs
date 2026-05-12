import os
import shutil

base_path = "/Users/macos/.antigravity-global/skills/"

mapping = {
    "security-master": [
        "backend-security-coder", "infrastructure-security", "penetration-testing",
        "securities-audit", "security-and-hardening", "security-auditor",
        "security-checklists", "security-design", "security-review"
    ],
    "senior-qa": [
        "e2e-testing", "test-engineer", "testing-anti-patterns", 
        "test-driven-development", "tdd-workflow"
    ],
    "review-master": [
        "code-review-excellence", "code-reviewer", "codex-review", 
        "csharp-reviewer", "differential-review", "pr-review", "vibe-code-auditor"
    ],
    "backend-architect": [
        "architect", "architecture-design", "code-architect", "software-architecture"
    ]
}

for master, subs in mapping.items():
    master_sub_dir = os.path.join(base_path, master, "sub-skills")
    if not os.path.exists(master_sub_dir):
        os.makedirs(master_sub_dir)
    
    for sub in subs:
        src = os.path.join(base_path, sub)
        dst = os.path.join(master_sub_dir, sub)
        if os.path.exists(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.move(src, dst)
            print(f"Moved {sub} to {master}/sub-skills/")
        else:
            print(f"Source {sub} not found at root.")
