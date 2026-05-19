import os
import sys
import json
import re

def migrate_skill(skill_dir):
    skill_dir = os.path.abspath(skill_dir)
    skill_name = os.path.basename(skill_dir)
    
    print(f"MIGRATING SKILL: {skill_name}")
    print(f"Path: {skill_dir}")
    print("----------------------------------------")
    
    if not os.path.exists(skill_dir):
        print(f"Error: Directory {skill_dir} does not exist.")
        return False
        
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(skill_md_path):
        print(f"Error: SKILL.md not found at {skill_md_path}")
        return False
        
    # Create sub-folders
    examples_dir = os.path.join(skill_dir, "examples")
    evals_dir = os.path.join(skill_dir, "evals")
    os.makedirs(examples_dir, exist_ok=True)
    os.makedirs(evals_dir, exist_ok=True)
    
    # 1. Create activation.yaml
    activation_path = os.path.join(skill_dir, "activation.yaml")
    if not os.path.exists(activation_path):
        keywords = [skill_name.replace("-", " ")]
        if "_" in skill_name:
            keywords.append(skill_name.replace("_", " "))
        
        yaml_content = f"""---
skill_name: {skill_name}
domain: backend-architecture
priority: 80
trigger_conditions:
  file_patterns:
    - "**/sub-skills/{skill_name}/**"
  query_keywords:
    - "{keywords[0]}"
conflict_resolutions:
  override: []
  delegate_before: []
---
"""
        with open(activation_path, "w", encoding="utf-8") as f:
            f.write(yaml_content)
        print("Created: activation.yaml")
    else:
        print("Skip: activation.yaml already exists")
        
    # 2. Prepend Contract block to SKILL.md
    with open(skill_md_path, "r", encoding="utf-8") as f:
        skill_content = f.read()
        
    if "EXECUTION CONTRACT" not in skill_content:
        # Generate generic but meaningful contract rules based on skill name
        contract_rules = [
            f"ALWAYS prioritize production-ready best practices for {skill_name}.",
            f"NEVER introduce raw, unvalidated patterns under {skill_name} context.",
            f"ALWAYS write clean, self-documenting code with comprehensive error bounds."
        ]
        
        # Parse frontmatter to insert contract right after frontmatter
        frontmatter_match = re.match(r"^(---\s*\n.*?\n---\s*\n)", skill_content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            rest_of_content = skill_content[len(frontmatter):]
            
            # Find the title header or place at top
            title_match = re.search(r"^(#\s+.*?\n)", rest_of_content)
            if title_match:
                title = title_match.group(1)
                body = rest_of_content[len(title):]
                new_skill_content = frontmatter + title + f"""
> [!IMPORTANT]
> ### 📜 EXECUTION CONTRACT (MANDATORY BEHAVIORS)
> 1. {contract_rules[0]}
> 2. {contract_rules[1]}
> 3. {contract_rules[2]}

---
## ⚡ ACTIVATION TRIGGERS
### 1. Input Signals (Kích hoạt khi phát hiện)
- **Files changed/created:** `**/sub-skills/{skill_name}/**`
- **Keywords in prompt:** `{keywords[0]}`
### 2. Output Expectation (Đầu ra bắt buộc)
- Domain-optimized implementation following clean multi-layer standards.

---
""" + body
            else:
                new_skill_content = frontmatter + f"""
# {skill_name.replace('-', ' ').title()}

> [!IMPORTANT]
> ### 📜 EXECUTION CONTRACT (MANDATORY BEHAVIORS)
> 1. {contract_rules[0]}
> 2. {contract_rules[1]}
> 3. {contract_rules[2]}

---
## ⚡ ACTIVATION TRIGGERS
### 1. Input Signals (Kích hoạt khi phát hiện)
- **Files changed/created:** `**/sub-skills/{skill_name}/**`
- **Keywords in prompt:** `{keywords[0]}`
### 2. Output Expectation (Đầu ra bắt buộc)
- Domain-optimized implementation following clean multi-layer standards.

---
""" + rest_of_content
        else:
            new_skill_content = f"""# {skill_name.replace('-', ' ').title()}

> [!IMPORTANT]
> ### 📜 EXECUTION CONTRACT (MANDATORY BEHAVIORS)
> 1. {contract_rules[0]}
> 2. {contract_rules[1]}
> 3. {contract_rules[2]}

---
## ⚡ ACTIVATION TRIGGERS
### 1. Input Signals (Kích hoạt khi phát hiện)
- **Files changed/created:** `**/sub-skills/{skill_name}/**`
- **Keywords in prompt:** `{keywords[0]}`
### 2. Output Expectation (Đầu ra bắt buộc)
- Domain-optimized implementation following clean multi-layer standards.

---
""" + skill_content
            
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(new_skill_content)
        print("Updated: SKILL.md with Execution Contract template")
    else:
        print("Skip: SKILL.md already contains Execution Contract")
        
    # 3. Create Good Example template
    good_path = os.path.join(examples_dir, "good_response.md")
    if not os.path.exists(good_path):
        good_content = f"""# Example: Golden Response for {skill_name}

This file presents the golden standard reasoning and code output format when using {skill_name}.

## 🪐 Recommended Design Pattern
- Demonstrate clean multi-layer separation (Controller, Service, Repository).
- Explicit validation at the entry boundaries.
- Adhere to every rule in the {skill_name} execution contract.
"""
        with open(good_path, "w", encoding="utf-8") as f:
            f.write(good_content)
        print("Created: examples/good_response.md")
    else:
        print("Skip: examples/good_response.md already exists")
        
    # 4. Create Bad Example template
    bad_path = os.path.join(examples_dir, "bad_response.md")
    if not os.path.exists(bad_path):
        bad_content = f"""# Example: Bad Response (Anti-Patterns to Avoid)

This file demonstrates the common AI slop, shortcuts, and structural errors under {skill_name}.

## ❌ Rejected Patterns
- Mixing architectural layers in a single mega-file.
- Swallowing exceptions or lacking boundary validation.
- Missing rate-limiting, tenant isolation, or explicit contracts.
"""
        with open(bad_path, "w", encoding="utf-8") as f:
            f.write(bad_content)
        print("Created: examples/bad_response.md")
    else:
        print("Skip: examples/bad_response.md already exists")
        
    # 5. Create Evals templates
    prompts_path = os.path.join(evals_dir, "prompts.json")
    if not os.path.exists(prompts_path):
        prompts_content = [
            {
                "id": f"tc_{skill_name.replace('-', '_')}_01",
                "category": "standard_evaluation",
                "description": f"Standard test case to verify compliance with {skill_name} best practices.",
                "prompt": f"Write a clean, production-ready implementation utilizing the {skill_name} capability. Explain security and architectural trade-offs."
            }
        ]
        with open(prompts_path, "w", encoding="utf-8") as f:
            json.dump(prompts_content, f, indent=2)
        print("Created: evals/prompts.json")
    else:
        print("Skip: evals/prompts.json already exists")
        
    expected_path = os.path.join(evals_dir, "expected.json")
    if not os.path.exists(expected_path):
        expected_content = [
            {
                "id": f"tc_{skill_name.replace('-', '_')}_01",
                "assertions": [
                  {
                    "target": "architecture",
                    "criteria": "Must demonstrate clean separation of concerns and use asynchronous calls where applicable.",
                    "grade": "mandatory"
                  }
                ]
            }
        ]
        with open(expected_path, "w", encoding="utf-8") as f:
            json.dump(expected_content, f, indent=2)
        print("Created: evals/expected.json")
    else:
        print("Skip: evals/expected.json already exists")
        
    print(f"Migration for {skill_name} completed successfully!\n")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python migrate_skill_structure.py <path_to_sub_skill_dir>")
        sys.exit(1)
        
    target_dir = sys.argv[1]
    migrate_skill(target_dir)
