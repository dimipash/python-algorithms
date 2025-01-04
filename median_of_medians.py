from typing import List, Any
import time


class MedianOfMedians:
    """
    Implements Median of Medians algorithm for selection.
    Provides guaranteed O(n) worst-case time complexity for selection.
    """

    @staticmethod
    def find_median(arr: List[int], group_size: int = 5) -> int:
        """
        Finds median of medians in array.

        Args:
            arr: Input array
            group_size: Size of groups for median calculation

        Returns:
            Median of medians value

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(arr)

        # Base case: small array
        if n <= group_size:
            return sorted(arr)[n // 2]

        # Divide into groups and find medians
        medians = []
        for i in range(0, n, group_size):
            group = arr[i : min(i + group_size, n)]
            group_median = sorted(group)[len(group) // 2]
            medians.append(group_median)

        # Recursively find median of medians
        return MedianOfMedians.find_median(medians)

    @staticmethod
    def partition(arr: List[int], pivot: int) -> tuple[List[int], List[int], List[int]]:
        """Partitions array around pivot value."""
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return left, middle, right

    @classmethod
    def select_kth(cls, arr: List[int], k: int) -> int:
        """
        Selects k-th smallest element using median of medians.

        Args:
            arr: Input array
            k: Position to find (1-based)

        Returns:
            k-th smallest element

        Raises:
            ValueError: If k is out of bounds
        """
        if not 1 <= k <= len(arr):
            raise ValueError("k is out of bounds")

        # Find pivot using median of medians
        pivot = cls.find_median(arr)

        # Partition around pivot
        left, middle, right = cls.partition(arr, pivot)

        # Determine which partition contains k-th element
        if k <= len(left):
            return cls.select_kth(left, k)
        elif k <= len(left) + len(middle):
            return pivot
        else:
            return cls.select_kth(right, k - len(left) - len(middle))


def main():
    # Test cases
    test_cases = [
        ([7, 10, 4, 3, 20, 15], 3, "Random array"),
        ([1, 2, 3, 4, 5], 1, "First element"),
        ([1, 2, 3, 4, 5], 5, "Last element"),
        ([2, 2, 2, 2, 2], 3, "All same elements"),
    ]

    for arr, k, case_type in test_cases:
        try:
            start = time.perf_counter()
            result = MedianOfMedians.select_kth(arr.copy(), k)
            duration = time.perf_counter() - start

            print(f"\nCase: {case_type}")
            print(f"Array: {arr}")
            print(f"k: {k}")
            print(f"{k}-th smallest: {result}")
            print(f"Time: {duration:.6f} seconds")

            # Verify result
            sorted_arr = sorted(arr)
            assert result == sorted_arr[k - 1], "Incorrect result!"

        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
