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

## 🧭 Sub-Skill Catalog

### 🔁 CI/CD & Pipelines
- **[Reviewing Cicd Pipelines](sub-skills/reviewing-cicd-pipelines/SKILL.md)** — audits CI/CD pipeline changes for correctness and security. **Use when:** reviewing GitHub Actions workflows or deployment configs for secret injection, environment targeting, and pipeline-security issues. **Not for:** authoring new pipelines from scratch (see CI/CD Workflow Automation).
- **[CI/CD Workflow Automation](sub-skills/cicd-automation-workflow-automate/SKILL.md)** — designs and builds CI/CD pipelines and GitHub Actions workflows. **Use when:** creating or refactoring automated build/test/deploy workflows, choosing runners, or defining trigger patterns. **Not for:** security review of existing pipelines (see Reviewing Cicd Pipelines).
- **[CircleCI Automation](sub-skills/circleci-automation/SKILL.md)** — drives CircleCI programmatically via Rube MCP (Composio). **Use when:** triggering CircleCI pipelines, monitoring workflows/jobs, or retrieving artifacts and test metadata. **Not for:** GitHub Actions or provider-agnostic pipeline authoring.

### ☁️ Cloud & AWS
- **[AWS Skills](sub-skills/aws-skills/SKILL.md)** — general AWS development, infrastructure automation, and cloud-architecture patterns. **Use when:** you need broad AWS guidance not covered by a more specialized AWS skill. **Not for:** serverless builds (see AWS Serverless) or cost work (see the AWS Cost skills).
- **[AWS Serverless](sub-skills/aws-serverless/SKILL.md)** — builds production-ready serverless apps on AWS. **Use when:** implementing Lambda, API Gateway, DynamoDB, or SQS/SNS event-driven patterns with SAM/CDK, or fixing cold starts/SnapStart. **Not for:** non-serverless compute such as EC2/ECS/EKS.
- **[AWS Cost Optimizer](sub-skills/aws-cost-optimizer/SKILL.md)** — analyzes AWS spend and produces optimization recommendations. **Use when:** investigating cost drivers or rightsizing via AWS CLI and Cost Explorer. **Not for:** actually deleting resources (see AWS Cost Cleanup).
- **[AWS Cost Cleanup](sub-skills/aws-cost-cleanup/SKILL.md)** — automated cleanup of unused or orphaned AWS resources. **Use when:** reclaiming idle resources (unattached EBS volumes, unused Elastic IPs, stale snapshots) to cut cost. **Not for:** spend analysis or recommendations (see AWS Cost Optimizer).

### 🚀 Deployment (Azure / Vercel)
- **[Azure Dev CLI Deployment](sub-skills/azd-deployment/SKILL.md)** — deploys containerized frontend + backend apps to Azure Container Apps via the Azure Developer CLI. **Use when:** deploying containers to Azure with remote builds, managed identity, and idempotent infrastructure. **Not for:** AWS or Vercel targets.
- **[Vercel Deployment](sub-skills/vercel-deployment/SKILL.md)** — deploys and tunes Next.js apps on Vercel's edge. **Use when:** configuring edge middleware, serverless functions, cache-control headers, or routing on Vercel. **Not for:** non-Vercel hosts.

### 🐳 Containers
- **[Docker Expert](sub-skills/docker-expert/SKILL.md)** — container image optimization, multi-stage builds, security hardening, and orchestration patterns. **Use when:** writing or optimizing Dockerfiles/Compose, shrinking image size, or hardening containers for production (e.g. Rails 8 / Ruby service images). **Not for:** cloud IaC provisioning (see Terraform) or CI/CD pipeline authoring (see CI/CD Workflow Automation).

### 🛠️ Infrastructure as Code (Terraform)
- **[Terraform Core Patterns](sub-skills/terraform/core/SKILL.md)** — advanced/enterprise Terraform & OpenTofu automation and state management. **Use when:** designing remote state backends, workspaces, policy-as-code, or multi-cloud stacks at enterprise scale. **Not for:** one-off manual changes or a non-Terraform IaC tool.
- **[Terraform Basics](sub-skills/terraform/basics/SKILL.md)** — Terraform/OpenTofu best-practices and testing guidance. **Use when:** creating new configs/modules, choosing a testing approach (validate/plan/frameworks), or reviewing/refactoring existing IaC. **Not for:** basic syntax lookups or provider API reference.
- **[Terraform Reusable Modules](sub-skills/terraform/modules/SKILL.md)** — production-ready, multi-cloud Terraform module patterns. **Use when:** building reusable modules across AWS, Azure, and GCP or standardizing organizational module conventions. **Not for:** AWS-only modules (see Terraform AWS Modules).
- **[Terraform AWS Modules](sub-skills/terraform/aws-modules/SKILL.md)** — Terraform module creation specifically for AWS. **Use when:** building or reviewing VPC, RDS, or EKS modules and AWS-focused HCL. **Not for:** Azure/GCP or multi-cloud modules (see Terraform Reusable Modules).
- **[Terraform Infrastructure Workflow](sub-skills/terraform/architecture/SKILL.md)** — end-to-end Terraform provisioning workflow orchestrating setup → modules → multi-environment deployment. **Use when:** running the full IaC lifecycle (init, backend, providers, multi-environment infra) rather than a single focused task. **Not for:** a narrow single-step change (use a specific Terraform skill above).

### 🐚 Bash & Shell
- **[Defensive Bash Patterns](sub-skills/bash-defensive-patterns/SKILL.md)** — catalog of defensive Bash techniques (strict mode, traps, safe argument handling). **Use when:** hardening shell scripts, CI/CD pipelines, or system utilities for fault tolerance and safety. **Not for:** interactive one-liners (see Bash Linux Command Patterns).
- **[Bash Professional Scripting](sub-skills/bash-pro/SKILL.md)** — professional, testable Bash script authoring and review. **Use when:** writing or reviewing automation/CI/CD/ops scripts and adding Bats/ShellCheck tests. **Not for:** POSIX-only sh (see POSIX Shell Pro) or Windows PowerShell.
- **[Bash Scripting Workflow](sub-skills/bash-scripting/SKILL.md)** — guided end-to-end workflow for producing production-ready Bash scripts (design → implement → test). **Use when:** you want a phased process that invokes the bash-pro and defensive-patterns skills to build a script from scratch. **Not for:** quick command lookups.
- **[Bash Linux Command Patterns](sub-skills/bash-linux/SKILL.md)** — interactive Linux/macOS shell command syntax. **Use when:** composing pipes, process control, and environment management at the terminal on Unix-like systems. **Not for:** writing hardened scripts (see the Bash scripting skills).
- **[POSIX Shell Pro](sub-skills/posix-shell-pro/SKILL.md)** — strict POSIX `sh` scripting for maximum portability. **Use when:** targeting dash/ash/busybox `sh` or any POSIX-compliant shell where Bash features are unavailable. **Not for:** Bash-specific features (see Bash Professional Scripting).
- **[BusyBox Windows Emulation](sub-skills/busybox-on-windows/SKILL.md)** — runs standard UNIX CLI tools on Windows via a Win32 BusyBox build. **Use when:** you need GNU/UNIX utilities inside a Windows environment. **Not for:** native Windows PowerShell scripting.

---

## 🔄 Sequential Master Chains (Next Recommended Action)

Upon completion of infrastructure configuration and cloud deployments:
- 👉 Recommend calling **[Review Master](../review-master/SKILL.md)** to execute post-merge audits (`npx commitshow audit`) and verify that live monitoring, access controls, and rate limits are fully operational.

