import numpy as np
from typing import Union, Callable
import matplotlib.pyplot as plt


class SquarePlusActivation:
    """
    Implementation of Squareplus activation function.

    Time Complexity: O(n) for n input elements
    Space Complexity: O(n) for output storage

    Example:
        >>> activation = SquarePlusActivation()
        >>> x = np.array([-2, -1, 0, 1, 2])
        >>> y = activation.forward(x)
    """

    def __init__(self, alpha: float = 1.0):
        """
        Args:
            alpha: Scale parameter for quadratic term
        """
        self.alpha = alpha

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass of Squareplus activation.

        f(x) = x² + x

        Args:
            x: Input array

        Returns:
            Activated values
        """
        return self.alpha * x**2 + x

    def derivative(self, x: np.ndarray) -> np.ndarray:
        """
        Compute derivative of Squareplus activation.

        f'(x) = 2x + 1
        """
        return 2 * self.alpha * x + 1

    def plot_activation(self, x_range: tuple = (-5, 5), num_points: int = 1000) -> None:
        """Plot activation function and its derivative"""
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = self.forward(x)
        dy = self.derivative(x)

        plt.figure(figsize=(12, 5))

        # Plot activation
        plt.subplot(1, 2, 1)
        plt.plot(x, y, "b-", label="Squareplus")
        plt.plot(x, np.maximum(x, 0), "r--", alpha=0.5, label="ReLU")
        plt.grid(True, alpha=0.3)
        plt.title("Squareplus vs ReLU")
        plt.xlabel("Input (x)")
        plt.ylabel("Output f(x)")
        plt.legend()

        # Plot derivative
        plt.subplot(1, 2, 2)
        plt.plot(x, dy, "g-", label="Squareplus derivative")
        plt.grid(True, alpha=0.3)
        plt.title("Squareplus Derivative")
        plt.xlabel("Input (x)")
        plt.ylabel("Derivative f'(x)")
        plt.legend()

        plt.tight_layout()
        plt.show()


def compare_alphas(x: np.ndarray, alphas: list = [0.5, 1.0, 2.0]) -> None:
    """Compare Squareplus with different alpha values"""
    print("\nSquareplus Comparison:")
    print(f"Input: {x}")

    for alpha in alphas:
        activation = SquarePlusActivation(alpha=alpha)
        output = activation.forward(x)
        print(f"Alpha = {alpha}: {output}")


if __name__ == "__main__":
    # Example usage
    x = np.array([-2, -1, 0, 1, 2])

    # Create Squareplus with default alpha
    activation = SquarePlusActivation()

    # Forward pass
    output = activation.forward(x)
    print(f"Input: {x}")
    print(f"Squareplus Output: {output}")

    # Compare different alpha values
    compare_alphas(x)

    # Plot activation and derivative
    activation.plot_activation()
