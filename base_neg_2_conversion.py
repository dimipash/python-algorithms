"""
Base Negabinary (-2) Conversion Algorithm

Converts decimal integers to negabinary (base -2) representation. The negabinary 
system represents both positive and negative integers without a sign bit by using
-2 as the base for positional notation.

Time Complexity: O(log|n|) - Logarithmic in input magnitude
Space Complexity: O(log|n|) - Storage grows with number of output digits
"""


def decimal_to_negabinary(n: int) -> str:
    """
    Convert a decimal integer to its negabinary (base -2) representation.

    Args:
        n (int): The decimal integer to convert.

    Returns:
        str: The negabinary representation as a string of 0s and 1s.

    Raises:
        ValueError: If the input is not an integer.

    Examples:
        >>> decimal_to_negabinary(10)
        '11110'
        >>> decimal_to_negabinary(-10)
        '1010'
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    if n == 0:
        return "0"

    negabinary = []
    while n != 0:
        # Perform division and get quotient and remainder
        n, remainder = divmod(n, -2)

        # Adjust negative remainders
        if remainder < 0:
            remainder += 2
            n += 1

        negabinary.append(str(remainder))

    return "".join(reversed(negabinary))


def main() -> None:
    """
    Demonstrate the usage of the negabinary conversion algorithm.
    """
    test_numbers = [10, -10, 0, 42, -42]

    for number in test_numbers:
        result = decimal_to_negabinary(number)
        print(f"Decimal: {number:3d} -> Negabinary: {result}")


if __name__ == "__main__":
    main()
