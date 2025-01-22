def kth_largest(arr, k):
    """
    KTH LARGEST ELEMENT
    ==================
    The task is to find the Kth largest element in an unsorted array.
    The Kth largest element means the element that would be at position K
    if the array were sorted in descending order.

    Approach: Sorting
    ---------------
    This function uses a sorting approach to find the Kth largest element.
    The array is sorted in descending order, and the element at index k-1
    is returned.

    Args:
        arr (list): The input array.
        k (int): The position of the element to find (1-indexed).

    Returns:
        int: The Kth largest element.

    Example:
        >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
        5

    Explanation:
        1. The array is sorted in descending order.
        2. The element at index k-1 is returned.
        3. For arr = [3, 2, 1, 5, 6, 4] and k = 2, the sorted array is [6, 5, 4, 3, 2, 1].
           The 2nd largest element is 5.

    Time Complexity:
        The time complexity of this solution is O(n log n), where n is the length of the input array.
        This is because the sorting operation takes O(n log n) time.

    Space Complexity:
        The space complexity of this solution is O(n), where n is the length of the input array.
        This is because the sorting operation creates a new sorted array.
    """
    return sorted(arr, reverse=True)[k - 1]


# Example usage:
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(arr, k))  # Output: 5
