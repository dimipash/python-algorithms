from typing import List, Optional
import math
import time


class JumpSearch:
    """
    Implements Jump Search algorithm for sorted arrays.
    Combines linear and binary search approaches.

    Time Complexity: O(√n)
    Space Complexity: O(1)
    """

    @staticmethod
    def search(arr: List[int], target: int) -> Optional[int]:
        """
        Searches for target value using jump search.

        Args:
            arr: Sorted list of integers
            target: Value to find

        Returns:
            Index of target if found, None otherwise
        """
        if not arr:
            return None

        n = len(arr)
        # Optimal jump size is √n
        step = int(math.sqrt(n))

        # Find the block where element is present
        prev = 0
        while prev < n and arr[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))

            # If we've exceeded array bounds
            if prev >= n:
                return None

        # Linear search in identified block
        while prev < min(step, n):
            if arr[prev] == target:
                return prev
            if arr[prev] > target:
                return None
            prev += 1

        return None


def benchmark_search(arr: List[int], target: int) -> tuple[Optional[int], float]:
    """Measures search performance."""
    start = time.perf_counter()
    result = JumpSearch.search(arr, target)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        # Regular cases
        (list(range(1, 20, 2)), 11, "Regular array"),
        # Edge cases
        ([1, 2, 3, 4, 5], 1, "First element"),
        ([1, 2, 3, 4, 5], 5, "Last element"),
        ([1, 2, 3, 4, 5], 6, "Not present"),
        ([], 1, "Empty array"),
        ([1], 1, "Single element"),
        # Large array
        (list(range(0, 1000, 2)), 500, "Large array"),
    ]

    for arr, target, case_type in test_cases:
        result, duration = benchmark_search(arr, target)

        print(f"\nCase: {case_type}")
        print(f"Array length: {len(arr)}")
        print(f"Target: {target}")
        print(f"Found at index: {result}")
        print(f"Time: {duration:.6f} seconds")


if __name__ == "__main__":
    main()
