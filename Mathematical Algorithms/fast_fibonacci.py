from typing import List, Tuple, Dict
import time


class FastFibonacci:
    """
    Implements efficient algorithms for computing Fibonacci numbers.
    Includes matrix exponentiation and dynamic programming approaches.
    """

    def __init__(self):
        self.memo: Dict[int, int] = {0: 0, 1: 1}

    @staticmethod
    def matrix_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Matrix multiplication for 2x2 matrices."""
        return [
            [
                A[0][0] * B[0][0] + A[0][1] * B[1][0],
                A[0][0] * B[0][1] + A[0][1] * B[1][1],
            ],
            [
                A[1][0] * B[0][0] + A[1][1] * B[1][0],
                A[1][0] * B[0][1] + A[1][1] * B[1][1],
            ],
        ]

    @staticmethod
    def matrix_power(M: List[List[int]], n: int) -> List[List[int]]:
        """
        Computes M^n using exponentiation by squaring.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if n == 0:
            return [[1, 0], [0, 1]]  # Identity matrix

        if n % 2 == 0:
            half = FastFibonacci.matrix_power(M, n // 2)
            return FastFibonacci.matrix_multiply(half, half)
        else:
            return FastFibonacci.matrix_multiply(
                M, FastFibonacci.matrix_power(M, n - 1)
            )

    def matrix_method(self, n: int) -> int:
        """
        Computes nth Fibonacci number using matrix exponentiation.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if n < 0:
            raise ValueError("Negative indices not supported")
        if n <= 1:
            return n

        matrix = [[1, 1], [1, 0]]
        result = self.matrix_power(matrix, n - 1)
        return result[0][0]

    def dynamic_method(self, n: int) -> int:
        """
        Computes nth Fibonacci number using dynamic programming.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n < 0:
            raise ValueError("Negative indices not supported")
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def memoized_method(self, n: int) -> int:
        """
        Computes nth Fibonacci number using memoization.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n < 0:
            raise ValueError("Negative indices not supported")

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.memoized_method(n - 1) + self.memoized_method(n - 2)
        return self.memo[n]


def benchmark_methods(n: int) -> None:
    """Compares performance of different Fibonacci methods."""
    calculator = FastFibonacci()
    methods = [
        ("Matrix", calculator.matrix_method),
        ("Dynamic", calculator.dynamic_method),
        ("Memoized", calculator.memoized_method),
    ]

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
        print(f"{name:8}: {duration:.6f} seconds")


def main():
    test_cases = [
        0,  # Base case
        1,  # Base case
        10,  # Small number
        30,  # Medium number
        50,  # Large number
    ]

    calculator = FastFibonacci()

    for n in test_cases:
        print(f"\nCalculating F({n})")
        try:
            result = calculator.matrix_method(n)
            print(f"Result: {result}")

            # Only benchmark reasonable sizes
            if n <= 30:
                benchmark_methods(n)
            else:
                print("Skipping benchmark for large number")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
