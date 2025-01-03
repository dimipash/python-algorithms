from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array of non-negative integers using counting sort.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(k) for the counting array

    Note: Efficient when k (range) is not much larger than n (length)
    """
    if not arr:
        return arr

    # Find range of input values
    max_val = max(arr)

    # Initialize counting array
    count = [0] * (max_val + 1)

    # Count occurrences of each value
    for num in arr:
        count[num] += 1

    # Reconstruct sorted array
    sorted_arr = []
    for val, freq in enumerate(count):
        sorted_arr.extend([val] * freq)

    return sorted_arr


def counting_sort_with_range(arr: List[int], min_val: int, max_val: int) -> List[int]:
    """
    Variant that handles negative numbers and specified range.
    """
    if not arr:
        return arr

    # Create counting array for the range
    range_size = max_val - min_val + 1
    count = [0] * range_size

    # Count occurrences
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct sorted array
    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


def main():
    # Test cases
    test_arrays = [
        [4, 2, 2, 8, 3, 3, 1],  # Regular case
        [1, 1, 1, 1],  # All same elements
        [5],  # Single element
        [],  # Empty array
        [10, 5, 0, 3, 8, 5],  # With zeros
    ]

    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = counting_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}\n")


if __name__ == "__main__":
    main()
