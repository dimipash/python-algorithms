from typing import Callable
import numpy as np
from scipy.integrate import quad


class ArcLength:
    """
    Calculates arc length of a curve using numerical integration.

    Arc length is the distance along a curve between two points, calculated using
    the formula: L = ∫[a to b] √(1 + [f'(x)]²) dx

    Time Complexity: O(n) for numerical integration
    Space Complexity: O(1) for computation
    """

    @staticmethod
    def calculate(f: Callable[[float], float], a: float, b: float) -> float:
        """
        Calculates arc length of function f(x) from a to b.

        Args:
            f: Function to integrate
            a: Lower bound
            b: Upper bound

        Returns:
            Arc length of the curve
        """

        def integrand(x: float) -> float:
            # Calculate derivative using numerical differentiation
            h = 1e-5  # Small step size
            derivative = (f(x + h) - f(x - h)) / (2 * h)
            return np.sqrt(1 + derivative**2)

        length, _ = quad(integrand, a, b)
        return length


def main():
    # Test cases
    test_functions = [
        (lambda x: x**2, 0, 1, "f(x) = x²"),
        (lambda x: x**3, 0, 1, "f(x) = x³"),
        (lambda x: np.sin(x), 0, np.pi, "f(x) = sin(x)"),
        (lambda x: np.sqrt(x), 0, 1, "f(x) = √x"),
    ]

    calculator = ArcLength()

    for func, a, b, name in test_functions:
        try:
            length = calculator.calculate(func, a, b)
            print(f"\nFunction: {name}")
            print(f"Interval: [{a}, {b}]")
            print(f"Arc Length: {length:.6f}")

        except Exception as e:
            print(f"Error calculating arc length for {name}: {e}")


if __name__ == "__main__":
    main()
