from typing import List
import time


class SelectionSort:
    """
    Implements Selection Sort algorithm.
    Repeatedly selects minimum element from unsorted portion
    and places it at the beginning.
    """

    @staticmethod
    def sort(arr: List[int]) -> List[int]:
        """
        Sorts array using selection sort algorithm.

        Args:
            arr: List of integers to sort

        Returns:
            Sorted list in ascending order

        Time Complexity: O(n^2) for all cases
        Space Complexity: O(1) - in-place sorting
        """
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):
            # Find minimum element in unsorted portion
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            # Swap minimum element with first unsorted position
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr


def benchmark_sort(arr: List[int]) -> tuple[List[int], float]:
    """Measures sorting performance."""
    start = time.perf_counter()
    result = SelectionSort.sort(arr.copy())
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases with different characteristics
    test_cases = [
        ([64, 25, 12, 22, 11], "Random array"),
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
