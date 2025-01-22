import numpy as np
from typing import Union, Callable
import matplotlib.pyplot as plt


class MishActivation:
    """
    Implementation of Mish activation function.

    Time Complexity: O(n) for n input elements
    Space Complexity: O(n) for output storage

    Example:
        >>> activation = MishActivation()
        >>> x = np.array([-2, -1, 0, 1, 2])
        >>> y = activation.forward(x)
    """

    def __init__(self, beta: float = 1.0):
        """
        Args:
            beta: Temperature parameter (default=1.0)
        """
        self.beta = beta

    def softplus(self, x: np.ndarray) -> np.ndarray:
        """Compute softplus: ln(1 + e^x)"""
        return np.log1p(np.exp(self.beta * x))

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass of Mish activation.

        f(x) = x * tanh(ln(1 + e^x))

        Args:
            x: Input array

        Returns:
            Activated values
        """
        return x * np.tanh(self.softplus(x))

    def derivative(self, x: np.ndarray) -> np.ndarray:
        """
        Compute derivative of Mish activation.

        f'(x) = tanh(softplus(x)) + x * sech²(softplus(x)) * sigmoid(x)
        """
        sp = self.softplus(x)
        tanh_sp = np.tanh(sp)
        sigmoid = 1 / (1 + np.exp(-x))
        sech_squared = 1 - tanh_sp**2

        return tanh_sp + x * sech_squared * sigmoid

    def plot_activation(self, x_range: tuple = (-5, 5), num_points: int = 1000) -> None:
        """Plot activation function and its derivative"""
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = self.forward(x)
        dy = self.derivative(x)

        plt.figure(figsize=(12, 5))

        # Plot activation
        plt.subplot(1, 2, 1)
        plt.plot(x, y, "b-", label="Mish")
        plt.plot(x, np.maximum(x, 0), "r--", alpha=0.5, label="ReLU")
        plt.grid(True, alpha=0.3)
        plt.title("Mish vs ReLU")
        plt.xlabel("Input (x)")
        plt.ylabel("Output f(x)")
        plt.legend()

        # Plot derivative
        plt.subplot(1, 2, 2)
        plt.plot(x, dy, "g-", label="Mish derivative")
        plt.grid(True, alpha=0.3)
        plt.title("Mish Derivative")
        plt.xlabel("Input (x)")
        plt.ylabel("Derivative f'(x)")
        plt.legend()

        plt.tight_layout()
        plt.show()


def compare_beta(x: np.ndarray, betas: list = [0.5, 1.0, 2.0]) -> None:
    """Compare Mish with different beta values"""
    print("\nMish Comparison:")
    print(f"Input: {x}")

    f
