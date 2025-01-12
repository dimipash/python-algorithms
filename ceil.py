"""
Ceiling Function Implementation

Rounds a number up to the nearest integer. For negative numbers, 
rounds toward positive infinity.

Time Complexity: O(1) - Constant time operation
Space Complexity: O(1) - Uses fixed amount of memory
"""


def ceil(x: float) -> int:
    """
    Compute the ceiling of a number.

    Args:
        x (float): Input number

    Returns:
        int: Smallest integer greater than or equal to x

    Examples:
        >>> ceil(3.7)
        4
        >>> ceil(-3.7)
        -3
    """
    # Handle integer case
    if x == int(x):
        return int(x)

    # For positive numbers, add 1 to truncated value
    if x > 0:
        return int(x) + 1

    # For negative numbers, truncate to integer
    return int(x)


def main() -> None:
    """
    Demonstrate ceiling function with various test cases.
    """
    test_numbers = [
        1.2,  # Regular positive
        2.0,  # Integer
        -3.1,  # Negative
        4.9,  # Close to next integer
        0.1,  # Close to zero
    ]

    for num in test_numbers:
        result = ceil(num)
        print(f"ceil({num}) = {result}")


if __name__ == "__main__":
    main()
