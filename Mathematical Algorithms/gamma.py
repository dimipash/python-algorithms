"""
Gamma Function Calculator

Computes the gamma function for real numbers using math.gamma().
The gamma function extends factorial to non-integer values:
Γ(n) = (n-1)! for positive integers n

Time Complexity: O(1) for built-in implementation
Space Complexity: O(1) for scalar values
"""

import math


def gamma(x: float) -> float:
    """
    Calculate the gamma function value for a number.

    Args:
        x (float): Input value (non-negative, non-zero)

    Returns:
        float: Gamma function value

    Raises:
        ValueError: If x is negative integer or zero
    """
    if x <= 0 and x.is_integer():
        raise ValueError("Gamma function not defined for zero or negative integers")

    return math.gamma(x)


def main() -> None:
    """
    Demonstrate gamma function calculation with examples.
    """
    test_cases = [
        5.0,  # Integer (returns 24.0 = 4!)
        2.5,  # Non-integer
        1.0,  # Γ(1) = 1
        0.5,  # Γ(0.5) = √π
    ]

    for x in test_cases:
        result = gamma(x)
        print(f"Γ({x}) = {result}")


if __name__ == "__main__":
    main()
