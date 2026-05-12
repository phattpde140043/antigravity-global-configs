import os

def append_links(base_path, links_map):
    for filename, links in links_map.items():
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            with open(filepath, "a") as f:
                f.write("\n\n---\n\n## 🔗 Related References\n")
                for link in links:
                    # link is a tuple (label, filename)
                    f.write(f"- **[{link[0]}]({link[1]})**\n")
            print(f"Linked {filename}")
        else:
            print(f"File {filename} not found in {base_path}")

# Security Master
sec_base = "/Users/macos/.antigravity-global/skills/security-master/references/"
sec_links = {
    "api-security.md": [("OWASP Guide", "owasp-guide.md"), ("Secrets Infrastructure", "secrets-infrastructure.md"), ("Threat Modeling", "threat-modeling.md")],
    "owasp-guide.md": [("API Security", "api-security.md"), ("SAST Patterns", "sast-patterns.md"), ("Threat Modeling", "threat-modeling.md")],
    "threat-modeling.md": [("OWASP Guide", "owasp-guide.md"), ("API Security", "api-security.md"), ("Multi-Tenant Safety", "multi-tenant-safety.md")],
    "multi-tenant-safety.md": [("Threat Modeling", "threat-modeling.md"), ("API Security", "api-security.md")],
    "secrets-infrastructure.md": [("API Security", "api-security.md"), ("Memory Security", "memory-security.md")],
    "commitshow-audit.md": [("SAST Patterns", "sast-patterns.md"), ("Threat Modeling", "threat-modeling.md")],
    "sast-patterns.md": [("OWASP Guide", "owasp-guide.md"), ("API Security", "api-security.md")]
}
append_links(sec_base, sec_links)

# Senior QA
qa_base = "/Users/macos/.antigravity-global/skills/senior-qa/references/"
qa_links = {
    "playbook.md": [("Flake Fixing", "flake-fixing.md"), ("Pairwise Testing (PyPICT)", "pypict.md")],
    "flake-fixing.md": [("Testing Playbook", "playbook.md")]
}
append_links(qa_base, qa_links)

# Backend Architect
arch_base = "/Users/macos/.antigravity-global/skills/backend-architect/references/"
arch_links = {
    "clean-architecture.md": [("SOLID Principles", "solid-principles.md"), ("Design Patterns", "design-patterns.md"), ("Architecture Patterns", "architecture-patterns.md")],
    "solid-principles.md": [("Clean Architecture", "clean-architecture.md"), ("Clean Code Heuristics", "clean-code-heuristics.md")],
    "dotnet-best-practices.md": [("EF Core & Dapper", "ef-core-dapper.md"), ("API Design", "api-design.md")],
    "api-design.md": [("Production Readiness", "production-readiness.md"), ("Documentation Standards", "documentation-standards.md")],
    "production-readiness.md": [("Observability", "observability.md"), ("Tech Decisions", "tech-decisions.md")],
    "architecture-patterns.md": [("Clean Architecture", "clean-architecture.md"), ("C4 Model", "c4-model.md")],
    "design-patterns.md": [("SOLID Principles", "solid-principles.md"), ("Clean Code Heuristics", "clean-code-heuristics.md")]
}
append_links(arch_base, arch_links)
