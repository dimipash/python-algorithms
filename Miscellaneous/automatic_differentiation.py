class DualNumber:
    """
    Implements forward-mode automatic differentiation using dual numbers.

    Time Complexity: O(1) for all operations
    Space Complexity: O(1) for storing value and derivative

    Attributes:
        value (float): Primal value
        derivative (float): Derivative value
    """

    def __init__(self, value: float, derivative: float):
        self.value = value
        self.derivative = derivative

    def __add__(self, other: "DualNumber") -> "DualNumber":
        """Addition of dual numbers following the chain rule"""
        return DualNumber(self.value + other.value, self.derivative + other.derivative)

    def __mul__(self, other: "DualNumber") -> "DualNumber":
        """Multiplication of dual numbers following the product rule"""
        return DualNumber(
            self.value * other.value,
            self.value * other.derivative + self.derivative * other.value,
        )

    def __repr__(self) -> str:
        return f"DualNumber(value={self.value}, derivative={self.derivative})"


def compute_derivative(f, x: float) -> tuple[float, float]:
    """
    Computes both function value and derivative at point x using forward-mode AD.

    Args:
        f: Function to differentiate
        x: Point at which to evaluate

    Returns:
        tuple[float, float]: (function value, derivative)

    Example:
        >>> def f(x): return x * x + x
        >>> compute_derivative(f, 2.0)
        (6.0, 5.0)  # f(2) = 6, f'(2) = 5
    """
    x_dual = DualNumber(x, 1.0)  # Seed derivative as 1.0
    result = f(x_dual)
    return result.value, result.derivative
