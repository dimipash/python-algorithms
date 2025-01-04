from typing import List
import math
import time


class CatalanNumbers:
    """
    Implements methods for generating and working with Catalan numbers.

    Catalan numbers are a sequence that appear in many combinatorial problems:
    - Valid parentheses combinations
    - Binary trees
    - Polygon triangulation
    - Mountain ranges
    """

    @staticmethod
    def generate_dynamic(n: int) -> List[int]:
        """
        Generates Catalan numbers using dynamic programming.

        Args:
            n: Number of Catalan numbers to generate

        Returns:
            List of first n+1 Catalan numbers

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if n < 0:
            raise ValueError("n must be non-negative")

        catalan = [0] * (n + 1)
        catalan[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - 1 - j]

        return catalan

    @staticmethod
    def generate_formula(n: int) -> List[int]:
        """
        Generates Catalan numbers using direct formula:
        C(n) = (1 / (n + 1)) * C(2n,n)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n < 0:
            raise ValueError("n must be non-negative")

        def binomial(n: int, k: int) -> int:
            return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

        return [binomial(2 * i, i) // (i + 1) for i in range(n + 1)]

    @staticmethod
    def nth_catalan(n: int) -> int:
        """Calculates nth Catalan number directly."""
        if n < 0:
            raise ValueError("n must be non-negative")
        return math.comb(2 * n, n) // (n + 1)


def benchmark_methods(n: int) -> None:
    """Compares performance of different generation methods."""

    # Dynamic programming method
    start = time.perf_counter()
    dp_result = CatalanNumbers.generate_dynamic(n)
    dp_time = time.perf_counter() - start

    # Direct formula method
    start = time.perf_counter()
    formula_result = CatalanNumbers.generate_formula(n)
    formula_time = time.perf_counter() - start

    print(f"\nTime comparison for n={n}:")
    print(f"Dynamic Programming: {dp_time:.6f} seconds")
    print(f"Direct Formula: {formula_time:.6f} seconds")

    # Verify results match
    assert dp_result == formula_result, "Results don't match!"


def main():
    # Test cases
    test_cases = [5, 10, 15]

    for n in test_cases:
        print(f"\nGenerating first {n+1} Catalan numbers:")

        catalan = CatalanNumbers.generate_dynamic(n)
        print(f"Numbers: {catalan}")

        # Show some applications
        print(f"\nApplications for C({n})={catalan[n]}:")
        print(f"- Number of valid parentheses expressions of length {2*n}")
        print(f"- Number of binary trees with {n} nodes")
        print(f"- Number of ways to triangulate a {n+2}-sided polygon")

        # Benchmark methods
        benchmark_methods(n)


if __name__ == "__main__":
    main()
