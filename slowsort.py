from typing import List
import time


class SlowSort:
    """
    Implements SlowSort algorithm - a deliberately inefficient sorting algorithm.
    Used primarily for educational purposes to demonstrate multiply-and-surrender
    paradigm, a pessimization of divide-and-conquer.
    """

    def sort(self, arr: List[int], i: int, j: int) -> None:
        """
        Sorts array using slowsort algorithm.

        Args:
            arr: List to sort
            i: Start index
            j: End index

        Time Complexity: O(n^(log n)) - extremely inefficient
        Space Complexity: O(log n) - recursive stack depth
        """
        if i >= j:
            return

        # Find midpoint
        mid = (i + j) // 2

        # Recursively sort both halves
        self.sort(arr, i, mid)
        self.sort(arr, mid + 1, j)

        # Compare and swap if needed
        if arr[j] < arr[mid]:
            arr[mid], arr[j] = arr[j], arr[mid]

        # Recursively sort all but maximum
        self.sort(arr, i, j - 1)


def benchmark_sort(arr: List[int]) -> tuple[List[int], float]:
    """Measures sorting performance."""
    start = time.perf_counter()
    result = arr.copy()
    SlowSort().sort(result, 0, len(result) - 1)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Warning: Only use small arrays due to algorithm's inefficiency
    test_cases = [
        ([3, 1, 4, 1, 5], "Small random array"),
        ([1, 2, 3], "Already sorted"),
        ([3, 2, 1], "Reverse sorted"),
        ([1], "Single element"),
        ([], "Empty array"),
    ]

    for arr, case_type in test_cases:
        original = arr.copy()
        try:
            sorted_arr, duration = benchmark_sort(arr)
            print(f"\nCase: {case_type}")
            print(f"Original: {original}")
            print(f"Sorted  : {sorted_arr}")
            print(f"Time    : {duration:.6f} seconds")
        except RecursionError:
            print(f"\nCase: {case_type}")
            print("Array too large for SlowSort - RecursionError")


if __name__ == "__main__":
    main()
