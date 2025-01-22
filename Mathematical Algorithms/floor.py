"""
Floor Function Implementation

Rounds a number down to the nearest integer. For negative numbers,
rounds toward negative infinity.

Time Complexity: O(1) - Constant time operation
Space Complexity: O(1) - Uses fixed amount of memory
"""


def floor(x: float) -> int:
    """
    Compute the floor of a number.

    Args:
        x (float): Input number

    Returns:
        int: Largest integer less than or equal to x

    Examples:
        >>> floor(3.7)
        3
        >>> floor(-3.7)
        -4
    """
    # Handle integer case
    if x == int(x):
        return int(x)

    # For positive numbers, truncate to integer
    if x > 0:
        return int(x)

    # For negative numbers, subtract 1 from truncated value
    return int(x) - 1


def main() -> None:
    """
    Demonstrate floor function with various test cases.
    """
    test_numbers = [
        3.7,  # Regular positive
        -2.1,  # Regular negative
        5.0,  # Integer
        -3.8,  # Negative with fraction
        4.9,  # Close to next integer
    ]

    for num in test_numbers:
        result = floor(num)
        print(f"floor({num}) = {result}")


if __name__ == "__main__":
    main()
