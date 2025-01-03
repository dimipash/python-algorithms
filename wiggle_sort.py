from typing import List


def wiggle_sort(nums: List[int]) -> List[int]:
    """
    Sorts array into a wiggle pattern where nums[0] <= nums[1] >= nums[2] <= nums[3]...

    Args:
        nums: List of integers to sort

    Returns:
        List sorted in wiggle pattern

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - in-place sorting
    """
    for i in range(len(nums) - 1):
        if (i % 2 == 0) == (nums[i] > nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def verify_wiggle(nums: List[int]) -> bool:
    """Verifies if array follows wiggle pattern."""
    if len(nums) <= 1:
        return True

    for i in range(len(nums) - 1):
        if i % 2 == 0 and nums[i] > nums[i + 1]:
            return False
        if i % 2 == 1 and nums[i] < nums[i + 1]:
            return False
    return True


def main():
    test_cases = [
        [3, 5, 2, 1, 6, 4],  # Random array
        [1, 5, 1, 1, 6, 4],  # With duplicates
        [1],  # Single element
        [],  # Empty array
        [1, 2, 3, 4, 5],  # Sorted array
    ]

    for arr in test_cases:
        original = arr.copy()
        sorted_arr = wiggle_sort(arr)
        is_valid = verify_wiggle(sorted_arr)

        print(f"Original: {original}")
        print(f"Wiggled : {sorted_arr}")
        print(f"Valid wiggle: {is_valid}\n")


if __name__ == "__main__":
    main()
