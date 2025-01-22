def binary_search(arr, target, left, right):
    """
    Perform a recursive binary search on a sorted array to find the index of the target.

    Parameters:
    arr (list): The sorted array to search.
    target (comparable): The value to search for.
    left (int): The starting index of the search range.
    right (int): The ending index of the search range.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    # Base case: target not found
    if left > right:
        return -1  # Target not found

    # Calculate the middle index
    mid = left + (right - left) // 2

    # Check if the middle element is the target
    if arr[mid] == target:
        return mid  # Target found

    # Recursively search the left or right half
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)  # Output: 6 (index of target)
