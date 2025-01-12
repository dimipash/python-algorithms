"""
Binary Exponentiation Algorithm

Efficiently computes base raised to an exponent using binary representation
of the exponent. The algorithm reduces computation time by squaring the base
and halving the exponent in each iteration.

Time Complexity: O(log n) - Logarithmic in the exponent value
Space Complexity: O(1) - Uses constant extra space
"""


def binary_exponentiation(base: float, exponent: int) -> float:
    """
    Compute base raised to exponent using binary exponentiation.

    Args:
        base (float): The base number
        exponent (int): The power to raise the base to

    Returns:
        float: Result of base^exponent

    Examples:
        >>> binary_exponentiation(2, 10)
        1024.0
        >>> binary_exponentiation(2, -2)
        0.25
    """
    if not isinstance(exponent, int):
        raise ValueError("Exponent must be an integer")

    # Handle negative exponents
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1.0
    while exponent > 0:
        # If current bit is 1, multiply result by base
        if exponent & 1:
            result *= base
        # Square the base for next bit
        base *= base
        # Right shift exponent by 1 (divide by 2)
        exponent >>= 1

    return result


def main() -> None:
    """
    Demonstrate binary exponentiation with sample cases.
    """
    test_cases = [
        (2, 10),  # Regular positive case
        (2, -2),  # Negative exponent
        (5, 0),  # Zero exponent
        (3, 5),  # Odd exponent
        (10, 3),  # Base > exponent
    ]

    for base, exponent in test_cases:
        result = binary_exponentiation(base, exponent)
        print(f"{base}^{exponent} = {result}")


if __name__ == "__main__":
    main()
