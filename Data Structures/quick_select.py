from typing import List
import random
import time


class QuickSelect:
    """
    Implements QuickSelect algorithm for finding k-th smallest element.
    Average Time Complexity: O(n)
    Worst Case: O(n²) but rare with random pivot
    """

    @staticmethod
    def partition(arr: List[int], low: int, high: int, pivot_idx: int) -> int:
        """
        Partitions array around pivot value.
        Returns final position of pivot.
        """
        pivot_value = arr[pivot_idx]
        # Move pivot to end
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

        store_idx = low
        for i in range(low, high):
            if arr[i] < pivot_value:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1

        # Place pivot in final position
        arr[store_idx], arr[high] = arr[high], arr[store_idx]
        return store_idx

    def select(self, arr: List[int], low: int, high: int, k: int) -> int:
        """
        Recursive QuickSelect implementation.
        Returns k-th smallest element (0-based index).
        """
        if low == high:
            return arr[low]

        # Choose random pivot
        pivot_idx = random.randint(low, high)
        pivot_idx = self.partition(arr, low, high, pivot_idx)

        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return self.select(arr, low, pivot_idx - 1, k)
        else:
            return self.select(arr, pivot_idx + 1, high, k)

    def find_kth_smallest(self, arr: List[int], k: int) -> int:
        """
        Public interface to find k-th smallest element.
        k is 1-based index.
        """
        if not 1 <= k <= len(arr):
            raise ValueError("k is out of bounds")
        return self.select(arr, 0, len(arr) - 1, k - 1)


def benchmark_selection(arr: List[int], k: int) -> tuple[int, float]:
    """Measures selection performance."""
    start = time.perf_counter()
    result = QuickSelect().find_kth_smallest(arr.copy(), k)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Test cases
    test_cases = [
        ([7, 10, 4, 3, 20, 15], 3, "Random array"),
        ([1, 2, 3, 4, 5], 1, "First element"),
        ([1, 2, 3, 4, 5], 5, "Last element"),
        ([2, 2, 2, 2, 2], 3, "All same elements"),
        (list(range(100)), 50, "Large sorted array"),
        (list(range(100, 0, -1)), 50, "Large reverse sorted"),
    ]

    for arr, k, case_type in test_cases:
        try:
            result, duration = benchmark_selection(arr, k)

            print(f"\nCase: {case_type}")
            print(f"Array length: {len(arr)}")
            print(f"k: {k}")
            print(f"{k}-th smallest: {result}")
            print(f"Time: {duration:.6f} seconds")

            # Verify result
            assert result == sorted(arr)[k - 1], "Incorrect result!"

        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
