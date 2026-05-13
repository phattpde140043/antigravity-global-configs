# Self-Supervised Learning (SSL) & SimCLR

SSL allows models to learn from unlabelled data by creating "Pretext Tasks."

## 🔄 SimCLR (Contrastive Learning)
The model learns to bring representations of the same image (augmented differently) closer, while pushing different images apart.

### 💻 SimCLR Loss (NT-Xent)
```python
import torch
import torch.nn.functional as F

class SimCLRLoss(nn.Module):
    """Normalized Temperature-scaled Cross Entropy loss."""
    def __init__(self, temperature=0.5):
        super().__init__()
        self.temp = temperature

    def forward(self, z1, z2):
        """
        z1, z2: [Batch, Dim] — two views of the same batch.
        """
        B = z1.size(0)
        z = torch.cat([z1, z2], dim=0)
        sim = torch.mm(z, z.t()) / self.temp
        
        # Mask out self-similarity
        mask = torch.eye(2*B, device=z.device).bool()
        sim.masked_fill_(mask, float('-inf'))
        
        labels = torch.arange(B, device=z.device)
        labels = torch.cat([labels + B, labels])
        return F.cross_entropy(sim, labels)
```

## 🎨 Data Augmentation Policies
Augmentations define what the model learns to be **invariant** to:
- **Random Crop**: Position invariance.
- **Color Jitter**: Lighting/Color invariance.
- **Gaussian Blur**: Focus/Noise invariance.

## 🍰 The "Cake" Analogy (LeCun)
- **The Cake (Base)**: Self-Supervised Learning (millions of bits of information).
- **The Icing**: Supervised Learning (thousands of bits).
- **The Cherry**: Reinforcement Learning (tens of bits).
*Conclusion: Most of human intelligence comes from SSL (observing the world).*
