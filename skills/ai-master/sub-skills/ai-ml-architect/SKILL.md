---
name: ai-ml-architect
description: "Advanced neural architecture design (JEPA, EBM) and representation learning. Part of the ai-master discipline."
category: engineering
metadata:
  triggers: [machine-learning, pytorch, jepa, world-models, self-supervised-learning, neural-networks]
---

# AI/ML Architect (Advanced)

Design and implement state-of-the-art machine intelligence systems focusing on representation learning and objective-driven architectures.

## 🏗️ Operating Pipeline

### 1. Representation Design
- Define the latent space and embedding dimensions.
- Select between Generative vs. Predictive (JEPA) approaches.

### 2. Objective & Cost Definition
- Define intrinsic and task-specific cost functions.
- Design contrastive or energy-based loss modules (EBM).

### 3. Training & SSL Strategy
- Implement self-supervised pre-training (SimCLR, MAE).
- Define augmentation invariance policies.

### 4. Evaluation & Rigor
- Verify world-model accuracy and predictive stability.
- **LeCun Review**: Mandatory critique to eliminate probabilistic "guessing" in favor of world-model logic.

## 🧪 AI Pillars
1. **Representations over Tokens**: Focus on learning data structure, not just sequence prediction.
2. **Objective-Driven**: Every model must have a clear cost minimization objective.
3. **World Modeling**: Build systems that simulate and predict consequences of actions.
4. **Energy-Based Stability**: Use energy functions to define compatibility between states.

## ⚠️ Safety Boundaries
- Avoid black-box models without clear objective functions.
- Ensure data privacy and ethical alignment in cost module definitions.
