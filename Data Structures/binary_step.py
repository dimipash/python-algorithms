from typing import Union, Callable
import numpy as np
import matplotlib.pyplot as plt


class ActivationFunctions:
    """
    Implementation of binary step activation function and variants.

    Time Complexity: O(n) for n input elements
    Space Complexity: O(1) for computation, O(n) for output storage

    Example:
        >>> activation = ActivationFunctions()
        >>> x = np.array([-2, -1, 0, 1, 2])
        >>> y = activation.binary_step(x)
    """

    def binary_step(self, x: np.ndarray, threshold: float = 0.0) -> np.ndarray:
        """
        Classic binary step activation function.

        f(x) = 1 if x >= threshold else 0

        Args:
            x: Input array
            threshold: Activation threshold

        Returns:
            Binary array of same shape as input
        """
        return np.where(x >= threshold, 1, 0)

    def bipolar_step(self, x: np.ndarray, threshold: float = 0.0) -> np.ndarray:
        """
        Bipolar step function returning {-1, 1} instead of {0, 1}.

        f(x) = 1 if x >= threshold else -1
        """
        return np.where(x >= threshold, 1, -1)

    def symmetric_step(
        self, x: np.ndarray, lower: float = -1, upper: float = 1
    ) -> np.ndarray:
        """
        Symmetric step function with configurable output values.

        f(x) = upper if x >= 0 else lower
        """
        return np.where(x >= 0, upper, lower)

    def plot_activation(
        self,
        func: Callable,
        x_range: tuple = (-5, 5),
        num_points: int = 1000,
        title: str = "Activation Function",
    ) -> None:
        """Plot activation function over specified range"""
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = func(x)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, "b-", label="Activation")
        plt.axhline(y=0, color="k", linestyle="-", alpha=0.3)
        plt.axvline(x=0, color="k", linestyle="-", alpha=0.3)
        plt.grid(True, alpha=0.3)
        plt.title(title)
        plt.xlabel("Input (x)")
        plt.ylabel("Output f(x)")
        plt.legend()
        plt.show()


def compare_activations(x: np.ndarray) -> None:
    """Compare different step activation functions"""
    activation = ActivationFunctions()

    results = {
        "Binary Step": activation.binary_step(x),
        "Bipolar Step": activation.bipolar_step(x),
        "Symmetric Step": activation.symmetric_step(x),
    }

    print("\nActivation Comparison:")
    print(f"Input: {x}")
    for name, output in results.items():
        print(f"{name}: {output}")


if __name__ == "__main__":
    # Example usage
    x = np.array([-2, -1, 0, 1, 2])

    # Create activation functions instance
    activation = ActivationFunctions()

    # Compare different activations
    compare_activations(x)

    # Plot activation functions
    activation.plot_activation(activation.binary_step, title="Binary Step Activation")
    activation.plot_activation(activation.bipolar_step, title="Bipolar Step Activation")
    activation.plot_activation(
        activation.symmetric_step, title="Symmetric Step Activation"
    )
