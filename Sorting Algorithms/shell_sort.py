from typing import List
import time


class ShellSort:
    """
    Implements Shell Sort algorithm.
    An optimization over insertion sort that allows exchange of far elements.
    """

    @staticmethod
    def sort(arr: List[int]) -> List[int]:
        """
        Sorts array using shell sort algorithm.

        Args:
            arr: List of integers to sort

        Returns:
            Sorted list in ascending order

        Time Complexity: O(n^2) worst case, O(n log n) average case
        Space Complexity: O(1) - in-place sorting
        """
        n = len(arr)
        gap = n // 2  # Initial gap

        while gap > 0:
            # Do insertion sort for elements gap distance apart
            for i in range(gap, n):
                temp = arr[i]
                j = i

                # Shift elements until correct position is found
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp

            gap //= 2  # Reduce gap for next phase

        return arr


def benchmark_sort(arr: List[int]) -> tuple[List[int], float]:
    """Measures sorting performance."""
    start = time.perf_counter()
    result = ShellSort.sort(arr.copy())
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases with different characteristics
    test_cases = [
        ([12, 34, 54, 2, 3], "Random array"),
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
