from typing import Tuple, List
import time


class LongestCommonSubstring:
    """
    Implements solutions for finding the longest common substring
    between two strings using different approaches.
    """

    @staticmethod
    def dynamic_programming(s1: str, s2: str) -> Tuple[str, int, List[List[int]]]:
        """
        Finds longest common substring using dynamic programming.

        Args:
            s1: First string
            s2: Second string

        Returns:
            Tuple of (substring, length, dp_table)

        Time Complexity: O(mn)
        Space Complexity: O(mn)
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_length = 0
        end_index = 0

        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        end_index = i

        substring = s1[end_index - max_length : end_index]
        return substring, max_length, dp

    @staticmethod
    def sliding_window(s1: str, s2: str) -> Tuple[str, int]:
        """
        Finds longest common substring using sliding window approach.

        Time Complexity: O(mn * min(m,n))
        Space Complexity: O(1)
        """

        def check_substring(length: int) -> Tuple[bool, str]:
            # Check all substrings of given length
            for i in range(len(s1) - length + 1):
                substring = s1[i : i + length]
                if substring in s2:
                    return True, substring
            return False, ""

        # Binary search on length
        left, right = 0, min(len(s1), len(s2))
        result = ""

        while left <= right:
            mid = (left + right) // 2
            found, substring = check_substring(mid)

            if found:
                result = substring
                left = mid + 1
            else:
                right = mid - 1

        return result, len(result)


def benchmark_methods(s1: str, s2: str) -> None:
    """Compares performance of different methods."""
    # Test dynamic programming
    start = time.perf_counter()
    dp_result = LongestCommonSubstring.dynamic_programming(s1, s2)
    dp_time = time.perf_counter() - start

    # Test sliding window
    start = time.perf_counter()
    sw_result = LongestCommonSubstring.sliding_window(s1, s2)
    sw_time = time.perf_counter() - start

    print("\nPerformance comparison:")
    print(f"Dynamic Programming: {dp_time:.6f} seconds")
    print(f"Sliding Window: {sw_time:.6f} seconds")

    assert dp_result[0] == sw_result[0], "Results don't match!"


def main():
    test_cases = [
        ("ABABC", "BABCA", "Basic case"),
        ("ABCDEF", "BCDEFG", "Overlapping"),
        ("AAAA", "AAAA", "Repeated chars"),
        ("XYZ", "ABC", "No common"),
        ("", "ABC", "Empty string"),
    ]

    for s1, s2, case_type in test_cases:
        print(f"\nCase: {case_type}")
        print(f"String 1: {s1}")
        print(f"String 2: {s2}")

        # Get result using DP
        substring, length, dp = LongestCommonSubstring.dynamic_programming(s1, s2)

        print(f"Longest Common Substring: '{substring}'")
        print(f"Length: {length}")

        # Show dp table for small strings
        if len(s1) <= 5 and len(s2) <= 5:
            print("\nDP Table:")
            for row in dp:
                print(row)

        # Benchmark methods
        if len(s1) * len(s2) <= 100:
            benchmark_methods(s1, s2)


if __name__ == "__main__":
    main()
