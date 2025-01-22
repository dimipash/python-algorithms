from typing import List
import time


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts array using insertion sort algorithm.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity:
        - Best: O(n) when array is nearly sorted
        - Average/Worst: O(n^2)
    Space Complexity: O(1) - in-place sorting
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1  # Index of last element in sorted portion

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key in its correct position
        arr[j + 1] = key

    return arr


def benchmark_sort(arr: List[int]) -> tuple[List[int], float]:
    """Measures sorting performance."""
    start = time.perf_counter()
    result = insertion_sort(arr.copy())
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases with different characteristics
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], "Random array"),
        ([1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], "Reverse sorted"),
        ([1], "Single element"),
        ([], "Empty array"),
        ([2, 2, 1, 1, 3, 3], "Duplicates"),
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
