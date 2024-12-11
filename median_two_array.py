def find_median_sorted_arrays(nums1, nums2):
    """
    Median of Two Sorted Arrays
    ==========================
    The task is to find the median of two sorted arrays. The median is the middle element in a sorted list of numbers. If the total number of elements is even, the median is the average of the two middle elements.

    Approach: Binary Search
    ------------------------
    To solve this problem efficiently in O(log(min(m,n))) time complexity, we can use a binary search approach on the smaller array.

    Python Implementation
    ---------------------
    This function takes two sorted arrays nums1 and nums2 as input and returns the median of the two arrays.

    Args:
        nums1 (list): The first sorted array.
        nums2 (list): The second sorted array.

    Returns:
        float: The median of the two arrays.

    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # Calculate the total length
    total_length = len(nums1) + len(nums2)

    # Initialize the binary search range
    left, right = 0, len(nums1)

    while left <= right:
        # Calculate the partition point for nums1
        partition_nums1 = (left + right) // 2

        # Calculate the partition point for nums2
        partition_nums2 = (total_length + 1) // 2 - partition_nums1

        # Calculate the maximum element on the left side of nums1
        max_left_nums1 = (
            float("-inf") if partition_nums1 == 0 else nums1[partition_nums1 - 1]
        )

        # Calculate the minimum element on the right side of nums1
        min_right_nums1 = (
            float("inf") if partition_nums1 == len(nums1) else nums1[partition_nums1]
        )

        # Calculate the maximum element on the left side of nums2
        max_left_nums2 = (
            float("-inf") if partition_nums2 == 0 else nums2[partition_nums2 - 1]
        )

        # Calculate the minimum element on the right side of nums2
        min_right_nums2 = (
            float("inf") if partition_nums2 == len(nums2) else nums2[partition_nums2]
        )

        # Check if the partition is correct
        if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
            # If the total length is odd, return the maximum of the left partitions
            if total_length % 2 == 1:
                return max(max_left_nums1, max_left_nums2)
            # If the total length is even, return the average of the maximum element from the left and the minimum element from the right
            else:
                return (
                    max(max_left_nums1, max_left_nums2)
                    + min(min_right_nums1, min_right_nums2)
                ) / 2
        # If the partition is not correct, adjust the binary search range
        elif max_left_nums1 > min_right_nums2:
            right = partition_nums1 - 1
        else:
            left = partition_nums1 + 1


# Example usage:
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))  # Output: 2.0


def main():
    """
    Example usage of the find_median_sorted_arrays function.
    """
    nums1 = [1, 3]
    nums2 = [2]
    result = find_median_sorted_arrays(nums1, nums2)
    print(f"The median of the two arrays {nums1} and {nums2} is: {result}")


if __name__ == "__main__":
    main()

"""
Explanation:
    1.  The function find_median_sorted_arrays takes two sorted arrays nums1 and nums2 as input.
    2.  It ensures that nums1 is the smaller array by swapping them if necessary.
    3.  It calculates the total length of the two arrays.
    4.  It initializes the binary search range to be from 0 to the length of nums1.
    5.  It enters a loop where it calculates the partition point for nums1 and nums2 based on the current binary search range.
    6.  It calculates the maximum element on the left side of nums1 and nums2, and the minimum element on the right side of nums1 and nums2.
    7.  It checks if the partition is correct by comparing the maximum element on the left side with the minimum element on the right side.
    8.  If the partition is correct, it returns the median based on whether the total length is odd or even.
    9.  If the partition is not correct, it adjusts the binary search range and repeats the process.

Time Complexity:
    The time complexity of this solution is O(log(min(m,n))), where m and n are the lengths of the two input arrays. This is because the binary search range is reduced by half at each iteration, resulting in a logarithmic number of iterations.

Space Complexity:
    The space complexity of this solution is O(1), as it only uses a constant amount of space to store the partition points and the maximum and minimum elements.
"""
