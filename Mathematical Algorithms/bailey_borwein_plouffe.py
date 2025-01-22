"""
Bailey-Borwein-Plouffe (BBP) Algorithm Implementation

This module provides an implementation of the BBP formula for calculating
the n-th digit of π in base 16 (hexadecimal) without needing to compute
the preceding digits. The BBP formula is particularly useful for its
ability to compute π to high precision efficiently.

The BBP formula is given by:
    π = Σ (1 / (16^k)) * [4/(8k + 1) - 2/(8k + 4) - 1/(8k + 5) - 1/(8k + 6)]
    where the summation is from k = 0 to n_terms - 1.

Time Complexity:
    O(n) - Linear time complexity where n is the number of terms.
    Each term requires constant time operations.

Space Complexity:
    O(1) - Constant space complexity as only a fixed number of variables
    are used regardless of input size.

Best/Average/Worst Case:
    All cases are O(n) as the algorithm performs the same operations
    regardless of input values.

Trade-offs and Limitations:
    - Efficient for computing individual hexadecimal digits of π
    - Slower convergence compared to some other π calculation methods
    - Not optimal for high-precision decimal calculations due to base conversion overhead

"""


def bbp_pi(n_terms: int) -> float:
    """
    Compute an approximation of π using the Bailey-Borwein-Plouffe formula.

    Args:
        n_terms (int): Number of terms to sum in the BBP series.

    Returns:
        float: Approximation of π to the specified precision.

    Raises:
        ValueError: If n_terms is negative.
    """
    if n_terms < 0:
        raise ValueError("Number of terms must be non-negative")

    pi = 0.0
    for k in range(n_terms):
        # Calculate the denominator terms
        d1 = 8 * k + 1
        d4 = 8 * k + 4
        d5 = 8 * k + 5
        d6 = 8 * k + 6

        # Calculate the power of 16 for current term
        power_16 = 16**k

        # Compute the k-th term using the BBP formula
        term = (1 / power_16) * (4 / d1 - 2 / d4 - 1 / d5 - 1 / d6)
        pi += term

    return pi


def main() -> None:
    """
    Example usage of the BBP algorithm with different precisions.
    """
    # Test cases with different numbers of terms
    test_terms = [10, 50, 100]

    for terms in test_terms:
        pi_value = bbp_pi(terms)
        print(f"π approximation with {terms:3d} terms: {pi_value:.15f}")


if __name__ == "__main__":
    main()
