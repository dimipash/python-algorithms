from typing import List, Optional
import time


class BinarySearch:
    """
    Implements Binary Search algorithm for finding elements in sorted arrays.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    @staticmethod
    def search(arr: List[int], target: int) -> Optional[int]:
        """
        Searches for target value in sorted array.

        Args:
            arr: Sorted list of integers
            target: Value to find

        Returns:
            Index of target if found, None otherwise
        """
        if not arr:
            return None

        left, right = 0, len(arr) - 1

        while left <= right:
            # Use bit shift for efficient division
            mid = left + ((right - left) >> 1)

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None

    @staticmethod
    def search_recursive(
        arr: List[int], target: int, left: int, right: int
    ) -> Optional[int]:
        """Recursive implementation of binary search."""
        if left > right:
            return None

        mid = left + ((right - left) >> 1)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return BinarySearch.search_recursive(arr, target, mid + 1, right)
        else:
            return BinarySearch.search_recursive(arr, target, left, mid - 1)


def benchmark_search(arr: List[int], target: int) -> tuple[Optional[int], float]:
    """Measures search performance."""
    start = time.perf_counter()
    result = BinarySearch.search(arr, target)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, "Middle element"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, "First element"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, "Last element"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, "Not present"),
        ([], 1, "Empty array"),
    ]

    for arr, target, case_type in test_cases:
        result, duration = benchmark_search(arr, target)

        print(f"\nCase: {case_type}")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Found at index: {result}")
        print(f"Time: {duration:.6f} seconds")


if __name__ == "__main__":
    main()
