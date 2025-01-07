from typing import List, Set, Dict
import time


class WordBreak:
    """
    Implements solutions for Word Break problem using different approaches.
    Determines if a string can be segmented into dictionary words.
    """

    def __init__(self, dictionary: List[str]):
        self.word_set = set(dictionary)
        self.memo: Dict[str, bool] = {}

    def dp_solution(self, s: str) -> bool:
        """
        Dynamic programming solution.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is valid

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in self.word_set:
                    dp[i] = True
                    break

        return dp[n]

    def recursive_solution(self, s: str) -> bool:
        """
        Recursive solution with memoization.

        Time Complexity: O(n^2) with memoization
        Space Complexity: O(n) for recursion stack
        """
        if s in self.memo:
            return self.memo[s]

        if not s:
            return True

        for i in range(1, len(s) + 1):
            if s[:i] in self.word_set and self.recursive_solution(s[i:]):
                self.memo[s] = True
                return True

        self.memo[s] = False
        return False

    def find_all_breaks(self, s: str) -> List[List[str]]:
        """
        Finds all possible word breaks.
        Warning: Can be exponential in worst case.
        """
        result = []

        def backtrack(start: int, current: List[str]):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in self.word_set:
                    current.append(word)
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])
        return result


def benchmark_methods(solver: WordBreak, s: str) -> None:
    """Compares performance of different methods."""
    # Test DP solution
    start = time.perf_counter()
    dp_result = solver.dp_solution(s)
    dp_time = time.perf_counter() - start

    # Test recursive solution
    start = time.perf_counter()
    rec_result = solver.recursive_solution(s)
    rec_time = time.perf_counter() - start

    print("\nPerformance comparison:")
    print(f"DP Solution: {dp_time:.6f} seconds")
    print(f"Recursive: {rec_time:.6f} seconds")

    assert dp_result == rec_result, "Results don't match!"


def main():
    test_cases = [
        ("leetcode", ["leet", "code"], "Basic case"),
        ("applepenapple", ["apple", "pen"], "Repeated words"),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], "Not possible"),
        ("", [""], "Empty string"),
        ("a", ["a"], "Single character"),
    ]

    for s, dictionary, case_type in test_cases:
        print(f"\nCase: {case_type}")
        print(f"String: {s}")
        print(f"Dictionary: {dictionary}")

        solver = WordBreak(dictionary)

        # Check if breakable
        can_break = solver.dp_solution(s)
        print(f"Can be broken: {can_break}")

        # Find all breaks for small strings
        if len(s) <= 10 and can_break:
            all_breaks = solver.find_all_breaks(s)
            print("All possible breaks:")
            for break_sequence in all_breaks:
                print(f"  {' '.join(break_sequence)}")

        # Benchmark methods
        benchmark_methods(solver, s)


if __name__ == "__main__":
    main()
