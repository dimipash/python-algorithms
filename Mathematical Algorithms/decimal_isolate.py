"""
Decimal Isolation Algorithm

Separates a decimal number into its integer and fractional components.
Uses simple arithmetic to extract parts while handling floating-point
precision issues.

Time Complexity: O(1) - Constant time operations
Space Complexity: O(1) - Only stores two numeric values
"""


def decimal_isolate(number: float) -> tuple:
    """
    Separate decimal number into integer and fractional parts.

    Args:
        number (float): Input decimal number

    Returns:
        tuple: (integer_part, fractional_part)

    Examples:
        >>> decimal_isolate(12.34)
        (12, 0.34)
        >>> decimal_isolate(-3.14)
        (-3, -0.14)
    """
    # Extract integer part using type conversion
    integer_part = int(number)

    # Get fractional part by subtracting integer part
    fractional_part = number - integer_part

    return integer_part, fractional_part


def main() -> None:
    """
    Demonstrate decimal isolation with example cases.
    """
    test_cases = [
        12.34,  # Positive decimal
        -3.14,  # Negative decimal
        5.0,  # Whole number
        0.75,  # Fraction only
    ]

    for number in test_cases:
        int_part, frac_part = decimal_isolate(number)
        print(f"{number} = {int_part} + {frac_part:.2f}")


if __name__ == "__main__":
    main()
