from typing import List
import time


class ClimbingStairs:
    """
    Solves the Climbing Stairs problem using dynamic programming.
    Calculates the number of distinct ways to climb n stairs,
    taking 1 or 2 steps at a time.
    """

    @staticmethod
    def climb_recursive(n: int) -> int:
        """
        Recursive solution (inefficient for large n).

        Time Complexity: O(2^n)
        Space Complexity: O(n) due to recursion stack
        """
        if n <= 1:
            return 1
        return ClimbingStairs.climb_recursive(n - 1) + ClimbingStairs.climb_recursive(
            n - 2
        )

    @staticmethod
    def climb_dp(n: int) -> int:
        """
        Dynamic programming solution.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    @staticmethod
    def climb_optimized(n: int) -> int:
        """
        Space-optimized solution.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n <= 1:
            return 1

        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

    @staticmethod
    def climb_generalized(n: int, steps: List[int]) -> int:
        """
        Generalized solution for any number of step sizes.

        Time Complexity: O(n * len(steps))
        Space Complexity: O(n)
        """
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = sum(dp[i - step] for step in steps if i >= step)

        return dp[n]


def benchmark(func, *args):
    start = time.perf_counter()
    result = func(*args)
    duration = time.perf_counter() - start
    return result, duration


def main():
    test_cases = [5, 10, 20, 30]

    for n in test_cases:
        print(f"\nClimbing {n} stairs:")

        # Basic DP solution
        result, duration = benchmark(ClimbingStairs.climb_dp, n)
        print(f"DP Solution: {result} ways, Time: {duration:.6f} seconds")

        # Optimized solution
        result, duration = benchmark(ClimbingStairs.climb_optimized, n)
        print(f"Optimized Solution: {result} ways, Time: {duration:.6f} seconds")

        # Generalized solution (1 and 2 steps)
        result, duration = benchmark(ClimbingStairs.climb_generalized, n, [1, 2])
        print(f"Generalized Solution: {result} ways, Time: {duration:.6f} seconds")

        # Recursive solution (only for small n)
        if n <= 20:
            result, duration = benchmark(ClimbingStairs.climb_recursive, n)
            print(f"Recursive Solution: {result} ways, Time: {duration:.6f} seconds")
        else:
            print("Recursive solution skipped for large n")


if __name__ == "__main__":
    main()
