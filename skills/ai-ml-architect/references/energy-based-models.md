# Energy-Based Models (EBM)

EBMs define the compatibility between variables by assigning low energy to "correct" configurations and high energy to "incorrect" ones.

## 📐 EBM Theory
Instead of calculating a probability $P(x)$, we calculate an energy $E(x)$. We don't need to normalize (calculate the partition function $Z$), which makes it more stable in high dimensions.
- **Low Energy**: High compatibility/probability.
- **High Energy**: Low compatibility/outlier.

## 💻 PyTorch Implementation Template

```python
import torch
import torch.nn as nn

class EnergyBasedModel(nn.Module):
    """
    EBM: F(x) = Energy of x. 
    We want E_pos < E_neg.
    """
    def __init__(self, latent_dim=512):
        super().__init__()
        self.energy_net = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.SiLU(),
            nn.Linear(256, 128),
            nn.SiLU(),
            nn.Linear(128, 1)  # Scalar: Energy
        )

    def energy(self, x):
        return self.energy_net(x).squeeze(-1)

    def contrastive_loss(self, x_pos, x_neg):
        """
        L = E[F(x_pos)] - E[F(x_neg)] + regularization
        Goal: Minimize energy for positive samples, maximize for negative.
        """
        E_pos = self.energy(x_pos)
        E_neg = self.energy(x_neg)
        loss = E_pos.mean() - E_neg.mean()
        # Regularization to keep energies from drifting to infinity
        reg = 0.1 * (E_pos.pow(2).mean() + E_neg.pow(2).mean())
        return loss + reg
```

## 🎯 Use Cases
- **Anomaly Detection**: High energy = Anomaly.
- **Structured Prediction**: Finding the $y$ that minimizes $E(x, y)$.
- **Self-Supervised Learning**: JEPA can be viewed as an EBM in representation space.
