---
name: ai-ml-architect
description: "Use when designing machine intelligence systems, world models, or implementing advanced neural architectures (JEPA, EBM)."
category: engineering
metadata:
  triggers: [machine-learning, pytorch, jepa, world-models, self-supervised-learning, neural-networks]
---

# AI/ML Architect (Tier 2)

Design and implement state-of-the-art machine intelligence systems. Focus on representation learning, predictive modeling, and efficient neural architectures.

## ⚡ Quick References (MANDATORY)
- **[World Models & JEPA](references/world-models-jepa.md)**: Joint-Embedding Predictive Architecture and autonomous intelligence.
- **[Energy-Based Models (EBM)](references/energy-based-models.md)**: Energy-based learning, contrastive loss, and EBM theory.
- **[Self-Supervised Learning](references/self-supervised-learning.md)**: SSL, SimCLR, and data augmentation strategies.
- **[Vision Architectures](references/vision-architectures.md)**: CNNs, LeNet-5, and modern vision backbones.
- **[Scientific Rigor](references/scientific-rigor-critique-lecun.md)**: The LeCun critique protocol (integrated).

---

## 🏗️ Operating Pipeline

### 1. Representation Design
- Define the latent space and embedding dimensions.
- Select between Generative vs. Predictive (JEPA) approaches.

### 2. Objective & Cost Definition
- Define the intrinsic and task-specific cost functions.
- Design the contrastive or energy-based loss modules.

### 3. Training & SSL Strategy
- Implement self-supervised pre-training (SimCLR, MAE).
- Define augmentation invariance policies.

### 4. Evaluation & Rigor
- Verify world-model accuracy and predictive stability.
- Perform the **LeCun Review** to eliminate probabilistic "guessing."

---

## 🧪 AI Pillars
1. **Representations over Tokens**: Focus on learning the structure of data, not just predicting sequences.
2. **Objective-Driven**: Every model must have a clear cost minimization objective.
3. **World Modeling**: Build systems that can simulate and predict the consequences of actions.
4. **Energy-Based Stability**: Use energy functions to define compatibility between states.

## ⚠️ Safety Boundaries
- Avoid black-box models without clear objective functions.
- Be critical of "Doomerism" hype; focus on engineering physics and constraints.
- Ensure data privacy and ethical alignment in cost module definitions.
