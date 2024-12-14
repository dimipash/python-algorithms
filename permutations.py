from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generates all possible permutations of a given array.

    Args:
        nums (List[int]): The input array.

    Returns:
        List[List[int]]: A list of all possible permutations of the input array.

    Examples:
        >>> permute([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    Raises:
        TypeError: If the input array is not a list.
    """
    # Check if the input array is a list
    if not isinstance(nums, list):
        raise TypeError("Input array must be a list")

    # Initialize a list to store the permutations
    permutations = []

    def backtrack(start: int) -> None:
        """
        Recursive function to generate permutations.

        Args:
            start (int): The starting index for the current permutation.
        """
        # If the starting index reaches the length of the array, the current permutation is complete
        if start == len(nums):
            # Add a copy of the current permutation to the result list
            permutations.append(nums[:])
            return
        # Iterate over the remaining elements in the array
        for i in range(start, len(nums)):
            # Swap the current element with the element at the starting index
            nums[start], nums[i] = nums[i], nums[start]
            # Recursively generate permutations for the remaining elements
            backtrack(start + 1)
            # Backtrack by swapping the elements back to their original positions
            nums[start], nums[i] = nums[i], nums[start]

    # Start the backtracking process from the first element
    backtrack(0)
    # Return the list of permutations
    return permutations

# Example usage:
arr = [1, 2, 3]
print(permute(arr))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


#### Explanation
#   The `permute` function takes an input array `nums` and returns a list of all possible permutations of the array.
#   The `backtrack` function is a recursive function that generates permutations by swapping elements in the array.
#   The `backtrack` function takes a starting index `start` as an argument and recursively generates permutations for the remaining elements in the array.
#   When the starting index reaches the length of the array, the current permutation is complete, and a copy of the permutation is added to the result list.
#   After exploring one possibility, the elements are swapped back to their original positions to restore the original order for the next iteration (backtracking).

#### Time Complexity
#   The time complexity of this solution is O(n!), where n is the length of the input array. This is because there are n! possible permutations of an array of length n.

#### Space Complexity
#   The space complexity of this solution is O(n!), where n is the length of the input array. This is because we need to store all possible permutations of the array, which requires O(n!) space.