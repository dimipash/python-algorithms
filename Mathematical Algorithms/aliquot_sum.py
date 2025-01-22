import math


def aliquot_sum(n):
    """
    Calculate the aliquot sum of a positive integer n.

    The aliquot sum is the sum of all proper divisors of n, excluding n itself.
    A proper divisor of n is a positive integer that divides n without leaving a remainder.

    Parameters:
    n (int): The positive integer to calculate the aliquot sum for.

    Returns:
    int: The aliquot sum of n.

    Examples:
    >>> aliquot_sum(12)
    16
    >>> aliquot_sum(6)
    6
    >>> aliquot_sum(1)
    0
    >>> aliquot_sum(0)
    0
    >>> aliquot_sum(-5)
    0
    """
    if n < 1:
        return 0  # Return 0 for non-positive numbers
    total = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i != n:
                total += i
            pair = n // i
            if pair != i and pair != n:
                total += pair
    return total


# Example usage
if __name__ == "__main__":
    print(aliquot_sum(12))  # Output: 16
    print(aliquot_sum(6))  # Output: 6
    print(aliquot_sum(1))  # Output: 0
    print(aliquot_sum(0))  # Output: 0
    print(aliquot_sum(-5))  # Output: 0
