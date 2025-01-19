import numpy as np
from typing import Union, Callable
import matplotlib.pyplot as plt


class GaussianErrorUnit:
    """
    Implementation of Gaussian Error Unit (GEU) activation function.

    Time Complexity: O(n) for n input elements
    Space Complexity: O(n) for output storage

    Example:
        >>> activation = GaussianErrorUnit()
        >>> x = np.array([-2, -1, 0, 1, 2])
        >>> y = activation.forward(x)
    """

    def __init__(self, sigma: float = 1.0):
        """
        Args:
            sigma: Standard deviation parameter
        """
        self.sigma = sigma
        self.sqrt_2pi = np.sqrt(2 * np.pi)

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass of GEU activation.

        f(x) = (1/√(2π)) * exp(-x²/2) if x >= 0
        f(x) = 0 if x < 0

        Args:
            x: Input array

        Returns:
            Activated values
        """
        return np.where(
            x >= 0, (1 / self.sqrt_2pi) * np.exp(-0.5 * (x / self.sigma) ** 2), 0
        )

    def derivative(self, x: np.ndarray) -> np.ndarray:
        """
        Compute derivative of GEU activation.

        f'(x) = -x * exp(-x²/2)/√(2π) if x >= 0
        f'(x) = 0 if x < 0
        """
        return np.where(
            x >= 0, -x * np.exp(-0.5 * (x / self.sigma) ** 2) / self.sqrt_2pi, 0
        )

    def plot_activation(self, x_range: tuple = (-5, 5), num_points: int = 1000) -> None:
        """Plot activation function and its derivative"""
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = self.forward(x)
        dy = self.derivative(x)

        plt.figure(figsize=(12, 5))

        # Plot activation
        plt.subplot(1, 2, 1)
        plt.plot(x, y, "b-", label="GEU")
        plt.grid(True, alpha=0.3)
        plt.title("Gaussian Error Unit")
        plt.xlabel("Input (x)")
        plt.ylabel("Output f(x)")
        plt.legend()

        # Plot derivative
        plt.subplot(1, 2, 2)
        plt.plot(x, dy, "g-", label="GEU derivative")
        plt.grid(True, alpha=0.3)
        plt.title("GEU Derivative")
        plt.xlabel("Input (x)")
        plt.ylabel("Derivative f'(x)")
        plt.legend()

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Example usage
    x = np.array([-2, -1, 0, 1, 2])

    # Create GEU with default sigma
    geu = GaussianErrorUnit()

    # Forward pass
    output = geu.forward(x)
    print(f"Input: {x}")
    print(f"GEU Output: {output}")

    # Plot activation and derivative
    geu.plot_activation()
