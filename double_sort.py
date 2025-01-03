from typing import List


class HybridSorter:
    """
    A hybrid sorting implementation combining bubble sort and insertion sort.
    Useful for educational purposes and understanding hybrid sorting approaches.
    """

    @staticmethod
    def bubble_sort(arr: List[int]) -> List[int]:
        """
        First pass: Bubble sort to get rough ordering.
        Time Complexity: O(n^2)
        """
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    @staticmethod
    def insertion_sort(arr: List[int]) -> List[int]:
        """
        Second pass: Insertion sort for fine-tuning.
        Time Complexity: O(n^2) but efficient for nearly sorted arrays
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @classmethod
    def double_sort(cls, arr: List[int]) -> List[int]:
        """
        Hybrid sort combining bubble and insertion sort.

        Args:
            arr: List of integers to sort

        Returns:
            Sorted list in ascending order

        Time Complexity: O(n^2) - dominated by slower algorithm
        Space Complexity: O(n) due to array copy
        """
        # First pass with bubble sort
        bubble_sorted = cls.bubble_sort(arr.copy())

        # Second pass with insertion sort
        return cls.insertion_sort(bubble_sorted)


def main():
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],  # Random array
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1],  # Single element
        [],  # Empty array
    ]

    sorter = HybridSorter()

    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = sorter.double_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}\n")


if __name__ == "__main__":
    main()
