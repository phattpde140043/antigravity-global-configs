---
name: crewai-orchestration
description: "Expert in CrewAI role-based multi-agent framework. Focuses on agent persona design, task decomposition, and complex workflow orchestration using Processes and Flows."
---

# CrewAI Multi-Agent Orchestration

Master the design and deployment of collaborative AI agent teams using the CrewAI framework.

## 🏗️ Core Components
- **Agents**: Define with specific **Roles**, **Goals**, and **Backstories**. Focus on persona expertise.
- **Tasks**: Define with clear descriptions and **Expected Outputs**. Manage dependencies using `context`.
- **Crews**: Orchestrate agents and tasks into a cohesive team.

## 🚀 Process Types
- **Sequential**: Tasks are executed in a predefined order.
- **Hierarchical**: A **Manager Agent** (or Manager LLM) delegates tasks to worker agents based on their expertise.
- **Flows**: Event-driven orchestration for complex, stateful workflows with branching and routing.

## 🛠️ Advanced Features
- **Memory**: Enable Short-term, Long-term, and Entity memory for cross-task and cross-session consistency.
- **Planning**: Enable the planning feature to generate a structured execution plan before running.
- **Custom Tools**: Extend agent capabilities by integrating specialized tools or APIs.

## 📋 Verification Checklist
- [ ] Are agent personas clearly defined with unique expertise?
- [ ] Are tasks decomposed into manageable units with clear expected outputs?
- [ ] Is the process type (Sequential/Hierarchical) appropriate for the complexity?
- [ ] Is memory enabled if the workflow requires historical context?
- [ ] Are custom tools properly documented and integrated?
