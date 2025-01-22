"""
Chudnovsky Algorithm Implementation

A fast method for calculating digits of π based on the Chudnovsky brothers' 1988 formula.
Provides approximately 14 digits of π per iteration using the formula:
    π = (426880 * √10005) / Σ [((-1)^k * (6k)! * (13591409 + 545140134k)) / ((3k)! * (k!)^3 * 640320^(3k))]

Time Complexity: O(n(log n)^3) where n is the desired precision
Space Complexity: O(n) for storing high-precision decimals
"""

from decimal import Decimal, getcontext


def chudnovsky_algorithm(precision: int) -> Decimal:
    """
    Calculate π using the Chudnovsky algorithm.

    Args:
        precision (int): Number of decimal places to calculate

    Returns:
        Decimal: Value of π to specified precision

    Raises:
        ValueError: If precision is negative
    """
    if precision < 0:
        raise ValueError("Precision must be non-negative")

    # Add extra precision for intermediate calculations
    getcontext().prec = precision + 2

    C = 426880 * Decimal(10005).sqrt()
    L = 13591409
    X = 1
    M = 1
    S = L
    K = 6

    # Each iteration provides ~14 digits of π
    for k in range(1, precision):
        # Update M using the multinomial coefficient
        M = (K**3 - 16 * K) * M // k**3

        # Update L (linear term)
        L += 545140134

        # Update X (exponential term)
        X *= -262537412640768000

        # Update partial sum
        S += Decimal(M * L) / X

        # Increment K by 12 for next iteration
        K += 12

    # Calculate final result
    pi = C / S
    return +pi  # Unary plus normalizes precision


def main() -> None:
    """
    Demonstrate the algorithm with various precision levels.
    """
    test_precisions = [10, 50, 100]

    for precision in test_precisions:
        pi = chudnovsky_algorithm(precision)
        print(f"\nπ to {precision} digits:")
        print(f"{pi}")


if __name__ == "__main__":
    main()
