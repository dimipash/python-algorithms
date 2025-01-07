from typing import List, Tuple
import time


class EditDistance:
    """
    Calculates minimum edit distance (Levenshtein distance) between strings.
    Supports insertion, deletion, and substitution operations.
    """

    @staticmethod
    def min_distance_dp(word1: str, word2: str) -> Tuple[int, List[List[int]]]:
        """
        Calculates edit distance using dynamic programming.

        Args:
            word1: First string
            word2: Second string

        Returns:
            Tuple of (distance, dp_table)

        Time Complexity: O(mn)
        Space Complexity: O(mn)
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],  # deletion
                        dp[i][j - 1],  # insertion
                        dp[i - 1][j - 1],  # substitution
                    )

        return dp[m][n], dp

    @staticmethod
    def get_operations(word1: str, word2: str, dp: List[List[int]]) -> List[str]:
        """Reconstructs sequence of operations from dp table."""
        operations = []
        i, j = len(word1), len(word2)

        while i > 0 or j > 0:
            if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
                i -= 1
                j -= 1
            else:
                if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
                    operations.append(f"Replace {word1[i-1]} with {word2[j-1]}")
                    i -= 1
                    j -= 1
                elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                    operations.append(f"Delete {word1[i-1]}")
                    i -= 1
                elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                    operations.append(f"Insert {word2[j-1]}")
                    j -= 1

        return operations[::-1]  # Reverse to get correct order


def benchmark_distance(word1: str, word2: str) -> tuple[int, float]:
    """Measures performance of edit distance calculation."""
    start = time.perf_counter()
    distance, _ = EditDistance.min_distance_dp(word1, word2)
    duration = time.perf_counter() - start
    return distance, duration


def main():
    test_cases = [
        ("horse", "ros", "Basic case"),
        ("intention", "execution", "Longer strings"),
        ("", "abc", "Empty string"),
        ("abc", "abc", "Identical strings"),
        ("kitten", "sitting", "Classic example"),
    ]

    for word1, word2, case_type in test_cases:
        print(f"\nCase: {case_type}")
        print(f"Word1: {word1}")
        print(f"Word2: {word2}")

        # Calculate distance and get operations
        distance, dp = EditDistance.min_distance_dp(word1, word2)
        operations = EditDistance.get_operations(word1, word2, dp)

        print(f"Edit Distance: {distance}")
        print("Operations:")
        for op in operations:
            print(f"  {op}")

        # Benchmark
        _, duration = benchmark_distance(word1, word2)
        print(f"Time: {duration:.6f} seconds")


if __name__ == "__main__":
    main()
