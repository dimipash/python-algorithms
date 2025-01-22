from typing import Dict
import time
import math


class Factorial:
    """
    Implements multiple approaches for calculating factorials.
    Includes iterative, recursive, and memoized solutions.
    """

    def __init__(self):
        self.memo: Dict[int, int] = {0: 1, 1: 1}

    def iterative(self, n: int) -> int:
        """
        Calculates factorial iteratively.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")

        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def recursive(self, n: int) -> int:
        """
        Calculates factorial recursively.

        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")

        if n <= 1:
            return 1
        return n * self.recursive(n - 1)

    def memoized(self, n: int) -> int:
        """
        Calculates factorial using memoization.

        Time Complexity: O(n)
        Space Complexity: O(n) for memo dictionary
        """
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = n * self.memoized(n - 1)
        return self.memo[n]

    @staticmethod
    def math_factorial(n: int) -> int:
        """Uses Python's math.factorial."""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        return math.factorial(n)


def benchmark_methods(n: int) -> None:
    """Compares performance of different factorial methods."""
    calculator = Factorial()
    methods = [
        ("Iterative", calculator.iterative),
        ("Recursive", calculator.recursive),
        ("Memoized", calculator.memoized),
        ("Math", calculator.math_factorial),
    ]

    results = []
    for name, method in methods:
        start = time.perf_counter()
        result = method(n)
        duration = time.perf_counter() - start
        results.append((name, result, duration))

    # Verify all methods give same result
    assert len(set(r[1] for r in results)) == 1, "Results don't match!"

    # Print performance comparison
    print("\nPerformance comparison:")
    for name, _, duration in results:
        print(f"{name:10}: {duration:.6f} seconds")


def main():
    test_cases = [
        0,  # Base case
        1,  # Base case
        5,  # Small number
        10,  # Medium number
        20,  # Larger number
    ]

    calculator = Factorial()

    for n in test_cases:
        print(f"\nCalculating {n}!")
        try:
            result = calculator.iterative(n)
            print(f"Result: {result}")

            # Only benchmark for reasonable sizes
            if n <= 20:
                benchmark_methods(n)
            else:
                print("Skipping benchmark for large number")

        except ValueError as e:
            print(f"Error: {e}")

        # Show some interesting facts
        if n <= 10:
            print(f"\nInteresting facts about {n}!:")
            print(f"- Number of digits: {len(str(result))}")
            print(f"- Sum of digits: {sum(int(d) for d in str(result))}")


if __name__ == "__main__":
    main()
