# World Models & JEPA (Joint-Embedding Predictive Architecture)

The core architecture for Autonomous Machine Intelligence (AMI), focusing on prediction in latent space rather than pixel-space generation.

## 🏗️ The 6 Modules of AMI
An intelligent agent must possess these components to simulate and plan:

1. **Configurator**: Sets the goals and modulates other modules based on the task.
2. **Perception**: Sensory encoders that feed the world model.
3. **World Model**: The core engine. Predicts the next latent state $s_{t+1}$ given the current state $s_t$ and action $a_t$.
4. **Cost Module**: Calculates the "Energy" or "Cost" of a state. 
   - $E(s) = \alpha \cdot \text{intrinsic\_cost}(s) + \beta \cdot \text{task\_cost}(s)$
5. **Short-term Memory**: Buffers states and simulations.
6. **Actor**: Proposes actions to minimize the predicted cost.

## ⚡ JEPA vs. LLMs
| Feature | LLM (Generative) | JEPA (Predictive) |
| :--- | :--- | :--- |
| **Objective** | Predict next token | Minimize error in representation |
| **World Model** | Implicit/None | Dedicated Central Module |
| **Planning** | Probabilistic text | Real simulation & cost minimization |
| **Input** | Text/Tokens | Multimodal (Video, Audio, Sensor) |
| **Causality** | Correlational | Causal (World dynamics) |

## 🧪 Implementation Logic
- **Joint-Embedding**: Don't predict $x$ from $y$. Embed both into latent space and predict the embedding.
- **Predictive**: Focus on predicting the *consequences* of actions, not just reconstructing the input.
