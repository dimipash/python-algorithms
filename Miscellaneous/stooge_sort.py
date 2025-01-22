from typing import List
import time


class StoogeSort:
    """
    Implements Stooge Sort algorithm - a highly inefficient recursive sorting algorithm.
    Used primarily for theoretical study and as an example of inefficient algorithm design.
    """

    def sort(self, arr: List[int], low: int, high: int) -> None:
        """
        Sorts array using stooge sort algorithm.

        Args:
            arr: List to sort
            low: Starting index
            high: Ending index

        Time Complexity: O(n^(log 3 / log 1.5)) ≈ O(n^2.7095)
        Space Complexity: O(log n) for recursion stack
        """
        if low >= high:
            return

        # If first element is larger than last, swap them
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]

        # If at least 3 elements remain
        if high - low + 1 > 2:
            third = (high - low + 1) // 3

            # Recursively sort first 2/3
            self.sort(arr, low, high - third)

            # Recursively sort last 2/3
            self.sort(arr, low + third, high)

            # Recursively sort first 2/3 again
            self.sort(arr, low, high - third)


def benchmark_sort(arr: List[int]) -> tuple[List[int], float]:
    """Measures sorting performance."""
    start = time.perf_counter()
    result = arr.copy()
    StoogeSort().sort(result, 0, len(result) - 1)
    duration = time.perf_counter() - start
    return result, duration


def verify_sorted(arr: List[int]) -> bool:
    """Verifies if array is sorted."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def main():
    # Warning: Only use very small arrays due to extreme inefficiency
    test_cases = [
        ([5, 3, 2, 4, 1], "Small random array"),
        ([1, 2, 3], "Already sorted"),
        ([3, 2, 1], "Reverse sorted"),
        ([1], "Single element"),
        ([], "Empty array"),
    ]

    for arr, case_type in test_cases:
        original = arr.copy()
        try:
            sorted_arr, duration = benchmark_sort(arr)
            is_sorted = verify_sorted(sorted_arr)

            print(f"\nCase: {case_type}")
            print(f"Original: {original}")
            print(f"Sorted  : {sorted_arr}")
            print(f"Correctly sorted: {is_sorted}")
            print(f"Time    : {duration:.6f} seconds")

        except RecursionError:
            print(f"\nCase: {case_type}")
            print("Array too large for StoogeSort - RecursionError")


if __name__ == "__main__":
    main()
