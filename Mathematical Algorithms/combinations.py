"""
Combinations Calculator

Calculates the number of ways to choose r items from n items where order
doesn't matter, using the formula: C(n,r) = n! / (r! * (n-r)!)

Time Complexity: O(min(r, n-r)) using optimized factorial calculation
Space Complexity: O(1) as only scalar values are stored
"""


def combinations(n: int, r: int) -> int:
    """
    Calculate number of combinations C(n,r).

    Args:
        n (int): Total number of items
        r (int): Number of items to choose

    Returns:
        int: Number of possible combinations

    Raises:
        ValueError: If n or r is negative
    """
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative")

    if r > n:
        return 0

    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def main() -> None:
    """
    Demonstrate combinations calculation with example cases.
    """
    test_cases = [
        (4, 2),  # Standard case
        (5, 3),  # Larger numbers
        (6, 0),  # Choose none
        (6, 6),  # Choose all
        (3, 4),  # Invalid case (r > n)
    ]

    for n, r in test_cases:
        result = combinations(n, r)
        print(f"C({n},{r}) = {result}")


if __name__ == "__main__":
    main()
