from typing import List, Set, Dict
import time


class PalindromePartitioning:
    """
    Implements solutions for palindrome partitioning problem
    using different approaches including backtracking and dynamic programming.
    """

    def __init__(self):
        self.palindrome_cache: Dict[str, bool] = {}

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        """Checks if substring is palindrome with caching."""
        substring = s[start : end + 1]
        if substring in self.palindrome_cache:
            return self.palindrome_cache[substring]

        left, right = 0, len(substring) - 1
        while left < right:
            if substring[left] != substring[right]:
                self.palindrome_cache[substring] = False
                return False
            left += 1
            right -= 1

        self.palindrome_cache[substring] = True
        return True

    def find_all_partitions(self, s: str) -> List[List[str]]:
        """
        Finds all possible palindrome partitions using backtracking.

        Time Complexity: O(n * 2^n)
        Space Complexity: O(n) for recursion stack
        """
        result = []
        current = []

        def backtrack(start: int):
            if start >= len(s):
                result.append(current[:])
                return

            for end in range(start, len(s)):
                if self.is_palindrome(s, start, end):
                    current.append(s[start : end + 1])
                    backtrack(end + 1)
                    current.pop()

        backtrack(0)
        return result

    def min_cuts(self, s: str) -> int:
        """
        Finds minimum number of cuts needed for palindrome partitioning.
        Uses dynamic programming.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(s)
        if n <= 1:
            return 0

        # dp[i] represents min cuts needed for s[0:i]
        dp = list(range(-1, n))  # Initialize with worst case

        for i in range(n):
            # Odd length palindromes
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                dp[right + 1] = min(dp[right + 1], dp[left] + 1)
                left -= 1
                right += 1

            # Even length palindromes
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                dp[right + 1] = min(dp[right + 1], dp[left] + 1)
                left -= 1
                right += 1

        return dp[n]


def benchmark_methods(s: str) -> None:
    """Compares performance of different methods."""
    solver = PalindromePartitioning()

    # Test all partitions
    start = time.perf_counter()
    partitions = solver.find_all_partitions(s)
    partitions_time = time.perf_counter() - start

    # Test min cuts
    start = time.perf_counter()
    min_cut = solver.min_cuts(s)
    min_cut_time = time.perf_counter() - start

    print("\nPerformance comparison:")
    print(f"All partitions: {partitions_time:.6f} seconds")
    print(f"Min cuts: {min_cut_time:.6f} seconds")


def main():
    test_cases = [
        "aab",  # Basic case
        "aba",  # Already palindrome
        "abba",  # Even length palindrome
        "amanaplanacanal",  # Longer string
        "x",  # Single character
    ]

    solver = PalindromePartitioning()

    for s in test_cases:
        print(f"\nString: {s}")

        # Find all partitions
        partitions = solver.find_all_partitions(s)
        print(f"All palindrome partitions ({len(partitions)}):")
        for p in partitions[:5]:  # Show first 5 partitions
            print(f"  {p}")
        if len(partitions) > 5:
            print("  ...")

        # Find minimum cuts
        cuts = solver.min_cuts(s)
        print(f"Minimum cuts needed: {cuts}")

        # Benchmark if string is not too long
        if len(s) <= 10:
            benchmark_methods(s)


if __name__ == "__main__":
    main()
