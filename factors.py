"""
Factor Calculator

Finds all factors of a given integer by checking divisibility
from 1 to n. A factor is an integer that divides n with no remainder.

Time Complexity: O(n) - Linear scan from 1 to n
Space Complexity: O(k) where k is number of factors
"""


def find_factors(n: int) -> list:
    """
    Find all factors of a given integer.

    Args:
        n (int): Integer to find factors for

    Returns:
        list: List of all factors in ascending order

    Raises:
        ValueError: If n is not a positive integer

    Examples:
        >>> find_factors(12)
        [1, 2, 3, 4, 6, 12]
        >>> find_factors(7)
        [1, 7]
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    factors = []
    for i in range(1, n + 1):
        if n % i == 0:  # Check divisibility
            factors.append(i)
    return factors


def main() -> None:
    """
    Demonstrate factor finding with example numbers.
    """
    test_cases = [
        12,  # Composite number
        7,  # Prime number
        1,  # Unit
        16,  # Perfect square
    ]

    for num in test_cases:
        factors = find_factors(num)
        print(f"Factors of {num}: {factors}")


if __name__ == "__main__":
    main()
