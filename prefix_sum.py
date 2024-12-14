from typing import List

def prefix_sum(arr: List[int]) -> List[int]:
    """
    Calculates the prefix sum array for a given array.

    Args:
        arr (List[int]): The input array.

    Returns:
        List[int]: The prefix sum array.

    Examples:
        >>> prefix_sum([1, 2, 3, 4, 5])
        [0, 1, 3, 6, 10, 15]

    Raises:
        TypeError: If the input array is not a list.
    """
    # Check if the input array is a list
    if not isinstance(arr, list):
        raise TypeError("Input array must be a list")

    # Initialize a new array prefix with a length of len(arr) + 1
    prefix = [0] * (len(arr) + 1)

    # Iterate through the original array
    for i in range(len(arr)):
        # Add each element to the cumulative sum stored at prefix[i + 1]
        prefix[i + 1] = prefix[i] + arr[i]

    # Return the prefix sum array
    return prefix

# Example usage:
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
print(prefix)  # Output: [0, 1, 3, 6, 10, 15]