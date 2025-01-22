from typing import List
import random
import time


class QuickSort:
    """
    Implements QuickSort algorithm with various pivot selection strategies
    and optimizations.
    """

    @staticmethod
    def partition(arr: List[int], low: int, high: int) -> int:
        """
        Partitions array around pivot using Hoare's partition scheme.

        Args:
            arr: Array to partition
            low: Starting index
            high: Ending index

        Returns:
            Final position of pivot
        """
        # Choose random pivot to avoid worst case for sorted arrays
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        pivot = arr[high]

        i = low - 1  # Index of smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_inplace(self, arr: List[int], low: int, high: int) -> None:
        """
        In-place implementation of QuickSort.

        Time Complexity:
            - Average: O(n log n)
            - Worst: O(n²) but rare with random pivot
        Space Complexity: O(log n) for recursion stack
        """
        if low < high:
            # Get pivot position
            pi = self.partition(arr, low, high)

            # Sort elements before and after partition
            self.quick_sort_inplace(arr, low, pi - 1)
            self.quick_sort_inplace(arr, pi + 1, high)

    def sort(self, arr: List[int]) -> List[int]:
        """Public interface for sorting."""
        self.quick_sort_inplace(arr, 0, len(arr) - 1)
        return arr


def benchmark_sort(arr: List[int]) -> tuple[List[int], float]:
    """Measures sorting performance."""
    start = time.perf_counter()
    result = QuickSort().sort(arr.copy())
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        ([3, 6, 1, 5, 4, 2], "Random array"),
        ([1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], "Reverse sorted"),
        ([1], "Single element"),
        ([], "Empty array"),
        ([2, 2, 1, 1, 3, 3], "With duplicates"),
    ]

    for arr, case_type in test_cases:
        original = arr.copy()
        sorted_arr, duration = benchmark_sort(arr)

        print(f"\nCase: {case_type}")
        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}")
        print(f"Time    : {duration:.6f} seconds")


if __name__ == "__main__":
    main()
