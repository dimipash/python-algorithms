import numpy as np
from typing import Union, Callable
import matplotlib.pyplot as plt


class LeakyReLU:
    """
    Implementation of Leaky ReLU activation function.

    Time Complexity: O(n) for n input elements
    Space Complexity: O(n) for output storage

    Example:
        >>> activation = LeakyReLU(alpha=0.01)
        >>> x = np.array([-2, -1, 0, 1, 2])
        >>> y = activation.forward(x)
    """

    def __init__(self, alpha: float = 0.01):
        """
        Args:
            alpha: Slope for negative values
        """
        self.alpha = alpha

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass of Leaky ReLU activation.

        f(x) = x if x > 0
        f(x) = αx if x ≤ 0

        Args:
            x: Input array

        Returns:
            Activated values
        """
        return np.where(x >= 0, x, self.alpha * x)

    def derivative(self, x: np.ndarray) -> np.ndarray:
        """
        Compute derivative of Leaky ReLU activation.

        f'(x) = 1 if x > 0
        f'(x) = α if x ≤ 0
        """
        return np.where(x >= 0, 1, self.alpha)

    def plot_activation(self, x_range: tuple = (-5, 5), num_points: int = 1000) -> None:
        """Plot activation function and its derivative"""
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = self.forward(x)
        dy = self.derivative(x)

        plt.figure(figsize=(12, 5))

        # Plot activation
        plt.subplot(1, 2, 1)
        plt.plot(x, y, "b-", label="Leaky ReLU")
        plt.plot(x, np.maximum(x, 0), "r--", alpha=0.5, label="ReLU")
        plt.grid(True, alpha=0.3)
        plt.title("Leaky ReLU vs ReLU")
        plt.xlabel("Input (x)")
        plt.ylabel("Output f(x)")
        plt.legend()

        # Plot derivative
        plt.subplot(1, 2, 2)
        plt.plot(x, dy, "g-", label="Leaky ReLU derivative")
        plt.grid(True, alpha=0.3)
        plt.title("Leaky ReLU Derivative")
        plt.xlabel("Input (x)")
        plt.ylabel("Derivative f'(x)")
        plt.legend()

        plt.tight_layout()
        plt.show()


def compare_alphas(x: np.ndarray, alphas: list = [0.01, 0.1, 0.2]) -> None:
    """Compare Leaky ReLU with different alpha values"""
    print("\nLeaky ReLU Comparison:")
    print(f"Input: {x}")

    for alpha in alphas:
        lrelu = LeakyReLU(alpha=alpha)
        output = lrelu.forward(x)
        print(f"Alpha = {alpha}: {output}")


if __name__ == "__main__":
    # Example usage
    x = np.array([-2, -1, 0, 1, 2])

    # Create Leaky ReLU with default alpha
    lrelu = LeakyReLU()

    # Forward pass
    output = lrelu.forward(x)
    print(f"Input: {x}")
    print(f"Leaky ReLU Output: {output}")

    # Compare different alpha values
    compare_alphas(x)

    # Plot activation and derivative
    lrelu.plot_activation()
