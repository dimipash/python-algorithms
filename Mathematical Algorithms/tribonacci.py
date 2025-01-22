from typing import List, Dict
import time


class Tribonacci:
    """
    Implements multiple approaches for calculating Tribonacci numbers.
    Each number is sum of previous three numbers.
    Sequence: 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, ...
    """

    def __init__(self):
        self.memo: Dict[int, int] = {0: 0, 1: 1, 2: 1}

    def recursive(self, n: int) -> int:
        """
        Basic recursive implementation (inefficient).

        Time Complexity: O(3^n)
        Space Complexity: O(n) for recursion stack
        """
        if n < 0:
            raise ValueError("n must be non-negative")

        if n <= 2:
            return self.memo[n]

        return self.recursive(n - 1) + self.recursive(n - 2) + self.recursive(n - 3)

    def memoized(self, n: int) -> int:
        """
        Recursive implementation with memoization.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n < 0:
            raise ValueError("n must be non-negative")

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = (
            self.memoized(n - 1) + self.memoized(n - 2) + self.memoized(n - 3)
        )
        return self.memo[n]

    def iterative(self, n: int) -> int:
        """
        Iterative implementation using constant space.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n < 0:
            raise ValueError("n must be non-negative")
        if n <= 2:
            return self.memo[n]

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c

    def generate_sequence(self, n: int) -> List[int]:
        """Generates first n numbers in the sequence."""
        sequence = []
        for i in range(n):
            sequence.append(self.iterative(i))
        return sequence


def benchmark_methods(n: int) -> None:
    """Compares performance of different methods."""
    calculator = Tribonacci()
    methods = [("Iterative", calculator.iterative), ("Memoized", calculator.memoized)]

    if n <= 20:  # Only test recursive for small n
        methods.append(("Recursive", calculator.recursive))

    results = []
    for name, method in methods:
        start = time.perf_counter()
        result = method(n)
        duration = time.perf_counter() - start
        results.append((name, result, duration))

    # Verify all methods give same result
    assert len(set(r[1] for r in results)) == 1, "Results don't match!"

    print("\nPerformance comparison:")
    for name, _, duration in results:
        print(f"{name:10}: {duration:.6f} seconds")


def main():
    test_cases = [5, 10, 20, 30]

    calculator = Tribonacci()

    for n in test_cases:
        print(f"\nCalculating Tribonacci({n})")

        try:
            # Calculate using iterative method
            result = calculator.iterative(n)
            print(f"Result: {result}")

            # Show sequence up to n
            if n <= 10:
                sequence = calculator.generate_sequence(n + 1)
                print(f"Sequence: {sequence}")

            # Benchmark methods
            benchmark_methods(n)

        except ValueError as e:
            print(f"Error: {e}")

        # Show some properties
        if n <= 10:
            sequence = calculator.generate_sequence(n + 1)
            ratios = [
                sequence[i] / sequence[i - 1] if sequence[i - 1] != 0 else 0
                for i in range(1, len(sequence))
            ]
            print("\nRatios between consecutive terms:")
            print(ratios)


if __name__ == "__main__":
    main()
