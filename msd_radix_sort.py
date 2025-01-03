from typing import List


def msd_radix_sort(arr: List[int], base: int = 10, digit_index: int = 0) -> List[int]:
    """
    Sorts array using Most Significant Digit (MSD) Radix Sort.

    Args:
        arr: List of integers to sort
        base: Number base (default 10 for decimal)
        digit_index: Current digit position being processed

    Returns:
        Sorted list in ascending order

    Time Complexity: O(w * n) where w is the max number of digits
    Space Complexity: O(n) for the buckets
    """
    # Base case: array is sorted or no more digits
    if len(arr) <= 1 or digit_index >= len(str(max(arr) if arr else 0)):
        return arr

    # Create buckets for each possible digit
    buckets = [[] for _ in range(base)]

    # Distribute numbers to buckets based on current digit
    for num in arr:
        digit = (num // (base**digit_index)) % base
        buckets[digit].append(num)

    # Recursively sort each bucket and combine results
    return [
        num
        for bucket in buckets
        for num in msd_radix_sort(bucket, base, digit_index + 1)
    ]


def main():
    # Test cases
    test_arrays = [
        [170, 45, 75, 90, 802, 24, 2, 66],  # Mixed numbers
        [1000, 100, 10, 1],  # Decreasing digits
        [5, 5, 5, 5],  # Equal numbers
        [1],  # Single element
        [],  # Empty array
    ]

    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = msd_radix_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}\n")


if __name__ == "__main__":
    main()
