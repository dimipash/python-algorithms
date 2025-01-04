from typing import List, Optional
import time


class LinearSearch:
    """
    Implements Linear Search algorithm.
    Sequentially searches through array elements.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    @staticmethod
    def search(arr: List[int], target: int) -> Optional[int]:
        """
        Searches for target value using linear search.

        Args:
            arr: List of integers (sorted or unsorted)
            target: Value to find

        Returns:
            Index of target if found, None otherwise
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return None

    @staticmethod
    def search_with_sentinel(arr: List[int], target: int) -> Optional[int]:
        """
        Optimized linear search using sentinel value.
        Eliminates bound checking in loop.
        """
        if not arr:
            return None

        # Save last element and put target at end
        last = arr[-1]
        arr[-1] = target

        i = 0
        while arr[i] != target:
            i += 1

        # Restore last element
        arr[-1] = last

        if i < len(arr) - 1 or arr[-1] == target:
            return i
        return None


def benchmark_search(arr: List[int], target: int) -> tuple[Optional[int], float]:
    """Measures search performance."""
    start = time.perf_counter()
    result = LinearSearch.search(arr, target)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        ([5, 3, 8, 4, 2], 4, "Random array"),
        ([1, 2, 3, 4, 5], 1, "First element"),
        ([1, 2, 3, 4, 5], 5, "Last element"),
        ([1, 2, 3, 4, 5], 6, "Not present"),
        ([], 1, "Empty array"),
        ([1], 1, "Single element"),
        ([2, 2, 2, 2, 2], 2, "All same elements"),
    ]

    for arr, target, case_type in test_cases:
        # Test regular linear search
        result, duration = benchmark_search(arr.copy(), target)

        print(f"\nCase: {case_type}")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Found at index: {result}")
        print(f"Time: {duration:.6f} seconds")

        # Compare with sentinel search if array not empty
        if arr:
            start = time.perf_counter()
            sentinel_result = LinearSearch.search_with_sentinel(arr.copy(), target)
            sentinel_duration = time.perf_counter() - start
            print(f"Sentinel search time: {sentinel_duration:.6f} seconds")


if __name__ == "__main__":
    main()
