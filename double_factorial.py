"""
Double Factorial Calculator

Computes n!! for non-negative integers, where n!! is the product of numbers
from n down to 1 that have the same parity as n.

Time Complexity: O(n/2) - Recursive calls decrease by 2 each time
Space Complexity: O(n/2) - Maximum recursion depth
"""


def double_factorial(n: int) -> int:
    """
    Calculate the double factorial of a non-negative integer.

    Args:
        n (int): Non-negative integer input

    Returns:
        int: Double factorial value n!!

    Raises:
        ValueError: If n is negative

    Examples:
        >>> double_factorial(6)
        48
        >>> double_factorial(7)
        105
    """
    if n < 0:
        raise ValueError("Double factorial is not defined for negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * double_factorial(n - 2)


def main() -> None:
    """
    Demonstrate double factorial calculation with examples.
    """
    test_cases = [6, 7, 0, 8, 5]

    for n in test_cases:
        result = double_factorial(n)
        print(f"{n}!! = {result}")


if __name__ == "__main__":
    main()
