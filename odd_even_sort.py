from typing import List
import time


class OddEvenSorter:
    """
    Implements Odd-Even Sort algorithm, a variation of bubble sort
    designed for parallel processing environments.
    """

    @staticmethod
    def sort(arr: List[int]) -> List[int]:
        """
        Sorts array using odd-even sort algorithm.

        Args:
            arr: List of integers to sort

        Returns:
            Sorted list in ascending order

        Time Complexity: O(n^2) worst/average case
        Space Complexity: O(1) - in-place sorting
        """
        n = len(arr)
        is_sorted = False

        while not is_sorted:
            is_sorted = True

            # Odd phase - compare odd-indexed pairs
            for i in range(1, n - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False

            # Even phase - compare even-indexed pairs
            for i in range(0, n - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False

        return arr


def benchmark_sort(arr: List[int]) -> tuple[List[int], float]:
    """Measures sorting performance."""
    start = time.perf_counter()
    result = OddEvenSorter.sort(arr.copy())
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], "Random array"),
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
