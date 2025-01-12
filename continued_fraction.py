"""
Continued Fraction Calculator

Converts a rational number p/q into its continued fraction representation
[a0; a1, a2, ..., an] where each ai is an integer term in the expansion.
The algorithm uses successive division with remainder.

Time Complexity: O(log min(p,q)) - Euclidean algorithm complexity
Space Complexity: O(log min(p,q)) to store the terms
"""


def continued_fraction(p: int, q: int) -> list:
    """
    Convert rational number p/q to continued fraction representation.

    Args:
        p (int): Numerator
        q (int): Denominator

    Returns:
        list: Sequence of integers representing continued fraction

    Raises:
        ValueError: If denominator is zero
    """
    if q == 0:
        raise ValueError("Denominator cannot be zero")

    result = []
    while q:
        # Get integer quotient
        a = p // q
        result.append(a)

        # Update p and q using remainder
        p, q = q, p - a * q

    return result


def main() -> None:
    """
    Demonstrate continued fraction conversion with examples.
    """
    test_cases = [
        (22, 7),  # Approximation of π
        (1, 2),  # Simple fraction
        (13, 11),  # Coprime numbers
        (45, 16),  # Larger numbers
    ]

    for p, q in test_cases:
        cf = continued_fraction(p, q)
        print(f"{p}/{q} = {cf}")


if __name__ == "__main__":
    main()
