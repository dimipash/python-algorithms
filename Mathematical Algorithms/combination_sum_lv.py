from typing import List, Set
import time


class CombinationSum:
    """
    Finds all unique combinations of numbers that sum to target.
    Implements backtracking approach with various optimizations.
    """

    def __init__(self, candidates: List[int]):
        self.candidates = sorted(candidates)  # Sort for optimization
        self.result: List[List[int]] = []

    def find_combinations(self, target: int) -> List[List[int]]:
        """
        Finds all combinations that sum to target.

        Args:
            target: Target sum to achieve

        Returns:
            List of all valid combinations

        Time Complexity: O(2^n) worst case
        Space Complexity: O(target/min(candidates)) for recursion depth
        """
        self.result = []
        self._backtrack([], 0, target)
        return self.result

    def _backtrack(self, path: List[int], start: int, remaining: int) -> None:
        """
        Recursive backtracking helper function.

        Args:
            path: Current combination being built
            start: Starting index in candidates
            remaining: Remaining sum to achieve
        """
        if remaining == 0:
            self.result.append(path[:])
            return

        for i in range(start, len(self.candidates)):
            # Early stopping if candidate too large
            if self.candidates[i] > remaining:
                break

            # Add candidate to path and continue search
            path.append(self.candidates[i])
            self._backtrack(path, i, remaining - self.candidates[i])
            path.pop()  # Backtrack by removing the last element

    def find_combinations_iterative(self, target: int) -> List[List[int]]:
        """Iterative version using stack."""
        result = []
        stack = [([], 0, target)]

        while stack:
            path, start, remaining = stack.pop()

            if remaining == 0:
                result.append(path)
                continue

            for i in range(start, len(self.candidates)):
                if self.candidates[i] > remaining:
                    break

                new_path = path + [self.candidates[i]]
                stack.append((new_path, i, remaining - self.candidates[i]))

        return result


def benchmark_solutions(candidates: List[int], target: int) -> None:
    """Compares recursive and iterative solutions."""
    solver = CombinationSum(candidates)

    # Test recursive solution
    start = time.perf_counter()
    recursive_result = solver.find_combinations(target)
    recursive_time = time.perf_counter() - start

    # Test iterative solution
    start = time.perf_counter()
    iterative_result = solver.find_combinations_iterative(target)
    iterative_time = time.perf_counter() - start

    print(f"Recursive time: {recursive_time:.6f} seconds")
    print(f"Iterative time: {iterative_time:.6f} seconds")
    assert recursive_result == iterative_result, "Results don't match!"


def main():
    test_cases = [
        ([2, 3, 6, 7], 7, "Basic case"),
        ([2, 3, 5], 8, "Multiple solutions"),
        ([2], 1, "No solution"),
        ([1], 1, "Single element"),
        ([1, 2, 3, 4, 5], 15, "Large target"),
    ]

    for candidates, target, case_type in test_cases:
        print(f"\nCase: {case_type}")
        print(f"Candidates: {candidates}")
        print(f"Target: {target}")

        solver = CombinationSum(candidates)
        combinations = solver.find_combinations(target)

        print(f"Found {len(combinations)} combinations:")
        for combo in combinations:
            print(f"  {combo} (sum: {sum(combo)})")

        benchmark_solutions(candidates, target)


if __name__ == "__main__":
    main()
