def is_monotonic(arr):
    """
    MONOTONIC ARRAY
    ==============
    A array is said to be monotonic if it is either entirely non-increasing or
    non-decreasing. This function determines whether a given array is monotonic.

    Approach: Flag Tracking
    ----------------------
    We track two flags: increasing and decreasing. We traverse through the array
    and update the flags based on whether the current element is larger or smaller
    than the previous one. If the array is entirely increasing or decreasing, one of
    the flags will remain True. If both flags are False, the array is neither increasing
    nor decreasing.

    Args:
        arr (list): The input array.

    Returns:
        bool: True if the array is monotonic, False otherwise.

    Example:
        >>> is_monotonic([1, 2, 2, 3])
        True
        >>> is_monotonic([6, 5, 4, 4])
        True
        >>> is_monotonic([1, 3, 2])
        False

    Explanation:
        1. We initialize two flags: increasing and decreasing, both set to True.
        2. We traverse through the array, starting from the second element.
        3. For each element, we check if it is larger or smaller than the previous one.
        4. If the current element is larger, we set the decreasing flag to False.
        5. If the current element is smaller, we set the increasing flag to False.
        6. After traversing the entire array, we return True if either the increasing
           or decreasing flag is still True, indicating that the array is monotonic.
        7. If both flags are False, we return False, indicating that the array is not monotonic.

    Time Complexity:
        The time complexity of this solution is O(n), where n is the length of the input array.
        This is because we traverse through the array once.

    Space Complexity:
        The space complexity of this solution is O(1), as we only use a constant amount of space
        to store the flags.
    """
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing


# Example usage:
arr = [1, 2, 2, 3]
print(is_monotonic(arr))  # Output: True
arr = [6, 5, 4, 4]
print(is_monotonic(arr))  # Output: True
arr = [1, 3, 2]
print(is_monotonic(arr))  # Output: False
