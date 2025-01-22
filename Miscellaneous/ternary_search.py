from typing import List, Optional
import time


class TernarySearch:
    """
    Implements Ternary Search algorithm for sorted arrays.
    Divides array into three parts for searching.

    Time Complexity: O(log3 n)
    Space Complexity: O(log3 n) due to recursion
    """

    @staticmethod
    def search_recursive(
        arr: List[int], left: int, right: int, target: int
    ) -> Optional[int]:
        """
        Recursive ternary search implementation.

        Args:
            arr: Sorted list to search
            left: Left boundary
            right: Right boundary
            target: Value to find

        Returns:
            Index of target if found, None otherwise
        """
        if right >= left:
            # Calculate two midpoints
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            # Check midpoints
            if arr[mid1] == target:
                return mid1
            if arr[mid2] == target:
                return mid2

            # Determine which segment to search
            if target < arr[mid1]:
                return TernarySearch.search_recursive(arr, left, mid1 - 1, target)
            elif target > arr[mid2]:
                return TernarySearch.search_recursive(arr, mid2 + 1, right, target)
            else:
                return TernarySearch.search_recursive(arr, mid1 + 1, mid2 - 1, target)

        return None

    @staticmethod
    def search_iterative(arr: List[int], target: int) -> Optional[int]:
        """
        Iterative ternary search implementation.
        """
        left, right = 0, len(arr) - 1

        while right >= left:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            if arr[mid1] == target:
                return mid1
            if arr[mid2] == target:
                return mid2

            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1

        return None


def benchmark_search(arr: List[int], target: int) -> tuple[Optional[int], float]:
    """Measures search performance."""
    start = time.perf_counter()
    result = TernarySearch.search_iterative(arr, target)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        (list(range(1, 11)), 7, "Middle element"),
        (list(range(1, 11)), 1, "First element"),
        (list(range(1, 11)), 10, "Last element"),
        (list(range(1, 11)), 11, "Not present"),
        ([1], 1, "Single element"),
        ([], 1, "Empty array"),
    ]

    for arr, target, case_type in test_cases:
        # Test iterative version
        result, duration = benchmark_search(arr, target)

        print(f"\nCase: {case_type}")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Found at index: {result}")
        print(f"Time: {duration:.6f} seconds")

        # Compare with recursive version
        if arr:
            start = time.perf_counter()
            recursive_result = TernarySearch.search_recursive(
                arr, 0, len(arr) - 1, target
            )
            recursive_time = time.perf_counter() - start
            print(f"Recursive time: {recursive_time:.6f} seconds")


if __name__ == "__main__":
    main()
