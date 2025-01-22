from typing import List
import time


def gnome_sort(arr: List[int]) -> List[int]:
    """
    Implements Gnome Sort algorithm (also known as Stupid Sort).

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n^2) worst/average case, O(n) for nearly sorted
    Space Complexity: O(1) - in-place sorting
    """
    index = 0
    n = len(arr)

    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            # Move forward if current element is in correct position
            index += 1
        else:
            # Swap with previous element and move backward
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    return arr


def benchmark_sort(func, arr: List[int]) -> tuple[List[int], float]:
    """Measure execution time of sorting function."""
    start = time.perf_counter()
    result = func(arr.copy())
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases with different array characteristics
    test_arrays = [
        [34, 2, 10, -9, 6],  # Random array
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1, 1, 1, 1],  # Equal elements
        [1],  # Single element
        [],  # Empty array
    ]

    for arr in test_arrays:
        original = arr.copy()
        sorted_arr, duration = benchmark_sort(gnome_sort, arr)

        print(f"Original array: {original}")
        print(f"Sorted array : {sorted_arr}")
        print(f"Time taken  : {duration:.6f} seconds\n")


if __name__ == "__main__":
    main()
