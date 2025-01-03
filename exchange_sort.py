from typing import List
import time


def exchange_sort(arr: List[int]) -> List[int]:
    """
    Sorts array by comparing and swapping pairs of elements.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n^2) for all cases
    Space Complexity: O(1) - in-place sorting
    """
    n = len(arr)

    # Compare each element with all following elements
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                # Swap if elements are in wrong order
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def benchmark_sort(arr: List[int]) -> float:
    """Measure execution time of sorting."""
    start = time.perf_counter()
    exchange_sort(arr.copy())
    return time.perf_counter() - start


def main():
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],  # Random array
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1],  # Single element
        [],  # Empty array
    ]

    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = exchange_sort(arr)
        duration = benchmark_sort(original)

        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}")
        print(f"Time    : {duration:.6f} seconds\n")


if __name__ == "__main__":
    main()
