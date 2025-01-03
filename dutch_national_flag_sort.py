from typing import List


def dutch_national_flag_sort(arr: List[int], pivot: int = 1) -> List[int]:
    """
    Sorts an array containing three distinct values using Dutch National Flag algorithm.

    Args:
        arr: List of integers (typically containing 0s, 1s, and 2s)
        pivot: Middle value to partition around (default 1)

    Returns:
        Sorted array with values partitioned into three sections

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - in-place sorting
    """
    if not arr:
        return arr

    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            # Move smaller elements to left section
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            # Keep middle elements in place
            mid += 1
        else:
            # Move larger elements to right section
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr


def verify_sorting(arr: List[int]) -> bool:
    """Verify if array is correctly sorted in three sections."""
    if not arr:
        return True

    # Check if array is non-decreasing
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def main():
    # Test cases
    test_arrays = [
        [2, 0, 2, 1, 1, 0],  # Mixed array
        [0, 0, 0, 1, 1, 2],  # Nearly sorted
        [2, 2, 1, 1, 0, 0],  # Reverse sorted
        [1, 1, 1],  # Single value
        [0, 2],  # Two values
        [],  # Empty array
    ]

    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = dutch_national_flag_sort(arr)
        is_valid = verify_sorting(sorted_arr)

        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}")
        print(f"Correctly sorted: {is_valid}\n")


if __name__ == "__main__":
    main()
