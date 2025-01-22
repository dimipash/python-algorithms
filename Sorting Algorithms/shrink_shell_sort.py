from typing import List
import time


class ShrinkShellSort:
    """
    Implements Shrink Shell Sort algorithm.
    A variation of Shell Sort with customizable gap reduction factor.
    """

    @staticmethod
    def sort(arr: List[int], shrink_factor: float = 1.3) -> List[int]:
        """
        Sorts array using shrink shell sort algorithm.

        Args:
            arr: List of integers to sort
            shrink_factor: Factor to reduce gap in each iteration (default 1.3)

        Returns:
            Sorted list in ascending order

        Time Complexity: O(n^2) worst case, better average case
        Space Complexity: O(1) - in-place sorting
        """
        n = len(arr)
        gap = int(n // shrink_factor)  # Initial gap

        while gap > 0:
            # Perform gap insertion sort
            for i in range(gap, n):
                temp = arr[i]
                j = i

                # Shift elements until correct position found
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp

            gap = int(gap // shrink_factor)  # Reduce gap

        return arr


def benchmark_sort(arr: List[int], factors: List[float]) -> None:
    """Compares performance with different shrink factors."""
    for factor in factors:
        start = time.perf_counter()
        result = ShrinkShellSort.sort(arr.copy(), factor)
        duration = time.perf_counter() - start
        print(f"Shrink factor {factor:.1f}: {duration:.6f} seconds")


def main():
    # Test cases
    test_cases = [
        ([12, 34, 54, 2, 3], "Random array"),
        ([1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], "Reverse sorted"),
        ([2, 2, 1, 1, 3, 3], "With duplicates"),
    ]

    # Test different shrink factors
    shrink_factors = [1.3, 1.5, 2.0]

    for arr, case_type in test_cases:
        print(f"\nCase: {case_type}")
        print(f"Original array: {arr}")
        sorted_arr = ShrinkShellSort.sort(arr.copy())
        print(f"Sorted array : {sorted_arr}")
        print("Performance with different shrink factors:")
        benchmark_sort(arr, shrink_factors)


if __name__ == "__main__":
    main()
