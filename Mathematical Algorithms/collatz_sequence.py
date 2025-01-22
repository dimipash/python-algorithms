"""
Collatz Sequence Calculator

Generates the Collatz sequence (3n + 1 sequence) starting from any positive integer.
The sequence follows two rules:
- If n is even: n → n/2
- If n is odd:  n → 3n + 1

Time Complexity: O(k) where k is sequence length
Space Complexity: O(k) to store the sequence
"""


def collatz_sequence(n: int) -> list:
    """
    Generate the Collatz sequence starting from n.

    Args:
        n (int): Starting positive integer

    Returns:
        list: Complete Collatz sequence from n to 1

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # If n is even
            n //= 2
        else:  # If n is odd
            n = 3 * n + 1
        sequence.append(n)

    return sequence
