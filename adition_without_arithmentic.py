def add_without_arithmetic(a, b):
    """
    Add two integers without using arithmetic operators.

    This function adds two numbers using bitwise operations:
    - XOR (^) to calculate the sum without carry.
    - AND (&) to find the carry, which is then shifted left (<<) by one.

    Parameters:
    a (int): The first integer to add.
    b (int): The second integer to add.

    Returns:
    int: The sum of a and b.

    Examples:
    >>> add_without_arithmetic(5, 7)
    12
    >>> add_without_arithmetic(-1, 1)
    0
    >>> add_without_arithmetic(0, 0)
    0
    >>> add_without_arithmetic(10, -5)
    5
    """
    while b != 0:
        # Calculate carry
        carry = a & b
        # Sum without carry
        a = a ^ b
        # Shift carry to the left
        b = carry << 1
    return a


# Example usage
if __name__ == "__main__":
    # Positive numbers
    print(add_without_arithmetic(5, 7))  # Output: 12

    # Negative and positive
    print(add_without_arithmetic(-1, 1))  # Output: 0

    # Zero
    print(add_without_arithmetic(0, 0))  # Output: 0

    # Larger numbers
    print(add_without_arithmetic(123456, 7890))  # Output: 131346

    # Negative numbers
    print(add_without_arithmetic(-10, -20))  # Output: -30
