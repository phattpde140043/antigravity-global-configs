---
name: infrastructure-master
description: "Master of Cloud Infrastructure (IaC), AWS CDK, and production-grade cloud patterns. Focuses on security, scalability, and Infrastructure as Code best practices."
---

# Infrastructure & Cloud Engineering

You are an expert Cloud Engineer specializing in AWS CDK, IaC patterns, and production-grade infrastructure.

## Core Philosophy
Infrastructure is code. Treat it with the same rigor as application code (versioning, testing, review).

### 🔄 Sequential Sub-Skill Pipeline
```
[Defensive Bash Patterns] ──→ [Reviewing CI/CD Pipelines] ──→ [AWS Serverless / Azure Dev CLI Deployment]
```


## 🏗️ CDK Best Practices (TypeScript/Python)
- **Construct Selection**: Always prefer **L2 constructs** over L1 (`Cfn*`) for safer, high-level defaults.
- **State Separation**: Separate **Stateful** resources (DBs, S3 Buckets, VPCs) from **Stateless** resources (Lambda, ECS, API Gateway) into different stacks.
- **Least Privilege**: Grant only the minimum necessary permissions using `.grant*()` methods.
- **Removal Policy**: Explicitly set `RemovalPolicy.RETAIN` for production stateful resources.

## 🛡️ Cloud Security Patterns
- **IAM**: Use specific actions and resource ARNs instead of wildcards.
- **VPC Design**: Use Private Subnets for databases and application logic; use NAT Gateways for outbound access.
- **Secrets**: Use AWS Secrets Manager or Parameter Store; never hardcode secrets in CDK code.

## ⚡ Reliability & Monitoring
- **Tagging**: Apply consistent tags to all resources for cost tracking and management.
- **Observability**: Enable CloudWatch Alarms and X-Ray tracing by default for all compute resources.

## 📋 Verification Checklist
- [ ] Are L2 constructs used wherever possible?
- [ ] Is state separated from logic (Stateful vs Stateless stacks)?
- [ ] Is the principle of least privilege applied to all IAM roles?
- [ ] Are production resources protected by RemovalPolicy.RETAIN?
- [ ] Are all resources properly tagged?

- For **Reviewing Cicd Pipelines** (Reviewing CI/CD pipelines and pipeline security):
  👉 **[Reviewing Cicd Pipelines](sub-skills/reviewing-cicd-pipelines/SKILL.md)**
- For **Generic CI/CD Workflow & Automation** (standard YAML syntax, runner selection, trigger patterns):
  👉 **[CI/CD Workflow Automation](sub-skills/cicd-automation-workflow-automate/SKILL.md)**
- For **CircleCI Pipelines & Workflows** (caching strategies, runner configurations, parallelism, custom build triggers):
  👉 **[CircleCI Automation](sub-skills/circleci-automation/SKILL.md)**
- For **AWS Cost Cleanup** (automated cleanup of unused AWS resources):
  👉 **[AWS Cost Cleanup](sub-skills/aws-cost-cleanup/SKILL.md)**
- For **AWS Cost Optimization** (Cost Explorer analytics, rightsizing recommendations):
  👉 **[AWS Cost Optimizer](sub-skills/aws-cost-optimizer/SKILL.md)**
- For **AWS Serverless Development** (Lambda, API Gateway, DynamoDB, SnapStart, cold start optimization):
  👉 **[AWS Serverless](sub-skills/aws-serverless/SKILL.md)**
- For **AWS Cloud Architecture Patterns** (infrastructure automation and general AWS patterns):
  👉 **[AWS Skills](sub-skills/aws-skills/SKILL.md)**
- For **Azure Container App Deployments** (Azure Developer CLI, idempotent container architecture):
  👉 **[Azure Dev CLI Deployment](sub-skills/azd-deployment/SKILL.md)**
- For **Vercel Cloud Edge Deployment & Tuning** (edge middlewares, serverless configurations, cache control headers, routing setups):
  👉 **[Vercel Deployment](sub-skills/vercel-deployment/SKILL.md)**

### 🛠️ Infrastructure as Code (Terraform)
- For **Terraform Specialist Workspaces** (state locks, workspaces variables setups):
  👉 **[Terraform Core Patterns](sub-skills/terraform/core/SKILL.md)**
- For **Terraform Basic Integrations** (providers setup, simple resources mappings):
  👉 **[Terraform Basics](sub-skills/terraform/basics/SKILL.md)**
- For **Terraform Module Creation** (reusable blueprints libraries, semantic versioning configurations):
  👉 **[Terraform Reusable Modules](sub-skills/terraform/modules/SKILL.md)**
- For **Terraform Regional Multi-Region Orchestrations** (multi-region variables pass, state mappings):
  👉 **[Terraform Multi-Region Architecture](sub-skills/terraform/architecture/SKILL.md)**
- For **Terraform AWS Standard Modules** (VPC, RDS, EKS modules implementations):
  👉 **[Terraform AWS Modules](sub-skills/terraform/aws-modules/SKILL.md)**
- For **Defensive Bash Programming** (production-grade error resilient automation and traps):
  👉 **[Defensive Bash Patterns](sub-skills/bash-defensive-patterns/SKILL.md)**
- For **Linux & macOS Shell Command Syntax** (piping, process control, environment management):
  👉 **[Bash Linux Command Patterns](sub-skills/bash-linux/SKILL.md)**
- For **Advanced Professional Shell Development** (clean, reusable, modular shell scripting):
  👉 **[Bash Professional Scripting](sub-skills/bash-pro/SKILL.md)**
- For **General Shell Scripting & Automation** (essential file operations and script loops):
  👉 **[Bash Scripting Basics](sub-skills/bash-scripting/SKILL.md)**
- For **BusyBox on Windows Shell Parity** (GNU utility emulation, Windows bash environments):
  👉 **[BusyBox Windows Emulation](sub-skills/busybox-on-windows/SKILL.md)**
- For **POSIX Standard Shell Scripting & Portability** (cross-platform compatibility, standard utility options, strict sh compatibility):
  👉 **[POSIX Shell Pro](sub-skills/posix-shell-pro/SKILL.md)**

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of infrastructure configuration and cloud deployments:
- 👉 Recommend calling **[Review Master](../review-master/SKILL.md)** to execute post-merge audits (`npx commitshow audit`) and verify that live monitoring, access controls, and rate limits are fully operational.

