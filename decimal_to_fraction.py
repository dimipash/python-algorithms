"""
Decimal to Fraction Converter

Converts decimal numbers to their simplest fractional representation using
Python's Fraction class. The algorithm finds the closest rational number
with the smallest possible denominator.

Time Complexity: O(log n) where n is the denominator
Space Complexity: O(1) for storing the fraction
"""

from fractions import Fraction


def decimal_to_fraction(decimal_number: float) -> Fraction:
    """
    Convert decimal number to its simplest fraction representation.

    Args:
        decimal_number (float): Input decimal number

    Returns:
        Fraction: Simplified fraction representation

    Examples:
        >>> decimal_to_fraction(0.75)
        Fraction(3, 4)
        >>> decimal_to_fraction(0.333)
        Fraction(333, 1000)
    """
    return Fraction(decimal_number).limit_denominator()


def main() -> None:
    """
    Demonstrate decimal to fraction conversion with examples.
    """
    test_cases = [
        0.75,  # Simple fraction (3/4)
        0.333,  # Repeating decimal
        1.5,  # Mixed number
        0.125,  # Power of 2 denominator
        2.0,  # Whole number
    ]

    for decimal in test_cases:
        fraction = decimal_to_fraction(decimal)
        print(f"{decimal} = {fraction}")


if __name__ == "__main__":
    main()
