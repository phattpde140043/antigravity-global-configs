# Batch Refactoring Orchestration

Plan and execute large-scale refactors safely using dependency-aware work packets and multi-agent coordination. Use this when a refactor spans multiple files or subsystems.

## 🛠️ Core Workflow

### 1. Discovery & Parallel Analysis
- Split the target scope into logical analysis lanes.
- Analyze intent maps, coupling risks, and dependencies across all lanes.
- **Output**: A comprehensive report of candidate work packets and risks.

### 2. Dependency-Aware Planning
- Merge analysis results into a single **Work Graph**.
- Create **Work Packets** with strict file ownership.
- Sequence packets based on dependency levels (Execute independent packets in parallel).

### 3. Multi-Agent Execution
- Spawn worker agents for each independent packet.
- **Ownership Rule**: One owner per file per wave. No overlapping edits.
- Workers must ignore unrelated code and focus strictly on their assigned packet.

### 4. Verification & Integration Gate
- Review packet outputs for logic consistency.
- Run targeted tests per packet, followed by the full suite for the integrated scope.
- Resolve any merge conflicts or logic overlaps.

---

## 📋 Work Packet Rules
- **Atomic**: Each packet must have a narrow, measurable goal.
- **Owner-Exclusive**: Only the assigned agent can modify the files in a packet.
- **Dependency-Locked**: Do not start a packet until its dependencies are 100% verified.
- **Done Criteria**: Every packet must include specific validation commands (Tests, Lint, Build).

## 🗂️ Templates
- **[Work Packet Template](./templates/work-packet.md)**
- **[Batch Prompt Templates](./templates/batch-prompts.md)**
