from typing import List, Dict
import time


class IntegerPartition:
    """
    Implements multiple approaches for solving the Integer Partition problem.
    Calculates number of ways to break down an integer into sum of smaller integers.
    """

    def __init__(self):
        self.memo: Dict[int, int] = {0: 1, 1: 1}

    def dynamic_programming(self, n: int) -> int:
        """
        Solves partition problem using dynamic programming.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if n < 0:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # Base case

        # For each number i
        for i in range(1, n + 1):
            # Update partitions for all numbers >= i
            for j in range(i, n + 1):
                dp[j] += dp[j - i]

        return dp[n]

    def recursive_memoized(self, n: int, k: int = None) -> int:
        """
        Recursive solution with memoization.
        k represents the largest part allowed.
        """
        if k is None:
            k = n

        if n == 0:
            return 1
        if n < 0 or k == 0:
            return 0

        key = (n, k)
        if key in self.memo:
            return self.memo[key]

        # Include k in partition + exclude k from partition
        result = self.recursive_memoized(n - k, k) + self.recursive_memoized(n, k - 1)

        self.memo[key] = result
        return result

    @staticmethod
    def generate_partitions(n: int) -> List[List[int]]:
        """
        Generates all possible partitions.
        Warning: Exponential complexity.
        """

        def backtrack(target: int, current: List[int], start: int):
            if target == 0:
                result.append(current[:])
                return

            for i in range(start, target + 1):
                if i <= target:
                    current.append(i)
                    backtrack(target - i, current, i)
                    current.pop()

        result = []
        backtrack(n, [], 1)
        return result


def benchmark_methods(n: int) -> None:
    """Compares performance of different partition methods."""
    calculator = IntegerPartition()

    # Test dynamic programming
    start = time.perf_counter()
    dp_result = calculator.dynamic_programming(n)
    dp_time = time.perf_counter() - start

    # Test recursive memoized
    start = time.perf_counter()
    rec_result = calculator.recursive_memoized(n)
    rec_time = time.perf_counter() - start

    print("\nPerformance comparison:")
    print(f"Dynamic Programming: {dp_time:.6f} seconds")
    print(f"Recursive Memoized: {rec_time:.6f} seconds")

    assert dp_result == rec_result, "Results don't match!"


def main():
    test_cases = [4, 5, 10, 15, 20]

    calculator = IntegerPartition()

    for n in test_cases:
        print(f"\nCalculating partitions for {n}:")

        # Get count using DP
        count = calculator.dynamic_programming(n)
        print(f"Number of partitions: {count}")

        # For small numbers, show all partitions
        if n <= 10:
            partitions = calculator.generate_partitions(n)
            print("All partitions:")
            for p in partitions:
                print(f"  {p} (sum: {sum(p)})")

        # Benchmark methods
        if n <= 20:
            benchmark_methods(n)
        else:
            print("Skipping benchmark for large number")


if __name__ == "__main__":
    main()
