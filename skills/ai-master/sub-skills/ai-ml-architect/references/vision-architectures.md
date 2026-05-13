# Vision Architectures

Modern implementations of classic and state-of-the-art vision backbones.

## 🏛️ LeNet-5 (Modern PyTorch)
The architecture that pioneered convolutional networks in production.

```python
import torch.nn as nn

class LeNet5(nn.Module):
    """
    LeNet-5 (LeCun et al. 1998)
    Optimized for handwritten digit recognition (MNIST).
    """
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5, padding=2),
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Conv2d(6, 16, kernel_size=5),
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Conv2d(16, 120, kernel_size=5),
            nn.Tanh(),
        )
        self.classifier = nn.Sequential(
            nn.Linear(120, 84),
            nn.Tanh(),
            # Final output layer
            nn.Linear(84, num_classes),
        )

    def forward(self, x):
        x = self.features(x)    # Output: [Batch, 120, 1, 1]
        x = x.view(x.size(0), -1)
        return self.classifier(x)
```

## 📜 Key Papers
- **LeCun et al. (1998)**: Gradient-Based Learning Applied to Document Recognition.
- **LeCun et al. (2015)**: Deep Learning (Nature Review).
- **Assran et al. (2023)**: I-JEPA (Image-based Joint-Embedding Predictive Architecture).
