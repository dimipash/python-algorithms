from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array using bubble sort algorithm.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity:
        - Best: O(n) when array is already sorted
        - Average/Worst: O(n^2)
    Space Complexity: O(1) - in-place sorting
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        # Compare adjacent elements
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is sorted
        if not swapped:
            break

    return arr


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
        sorted_arr = bubble_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}\n")


if __name__ == "__main__":
    main()
