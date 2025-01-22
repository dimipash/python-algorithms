from typing import List, Tuple

def find_pairs_with_sum(arr: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Finds all pairs of elements in an array that sum up to a given target.

    Args:
        arr (List[int]): The input array.
        target (int): The target sum.

    Returns:
        List[Tuple[int, int]]: A list of pairs of elements that sum up to the target.

    Examples:
        >>> find_pairs_with_sum([1, 5, 7, -1, 5], 6)
        [(1, 5), (7, -1)]

    Raises:
        TypeError: If the input array is not a list or the target is not an integer.
    """
    # Check if the input array is a list and the target is an integer
    if not isinstance(arr, list) or not isinstance(target, int):
        raise TypeError("Input array must be a list and target must be an integer")

    # Initialize a set to store the numbers we've already encountered
    seen = set()
    # Initialize a list to store the pairs of elements that sum up to the target
    pairs = []
    # Iterate over each element in the array
    for num in arr:
        # Calculate the complement of the current element
        diff = target - num
        # Check if the complement is already in the set
        if diff in seen:
            # If the complement is already in the set, we've found a pair that sums to the target
            # Add the pair to the list of pairs, but only if the pair is not already in the list
            if (diff, num) not in pairs and (num, diff) not in pairs:
                pairs.append((diff, num))
        # Add the current element to the set
        seen.add(num)
    # Return the list of pairs
    return pairs

# Example usage:
arr = [1, 5, 7, -1, 5]
target = 6
# Example usage:
arr = [1, 5, 7, -1, 5]
target = 6
print(find_pairs_with_sum(arr, target))  # Output: [(1, 5), (7, -1)]

#### Explanation
# We use a set to store the numbers we have already encountered.
# For each element in the array, we calculate its complement (i.e., target - num). 
# If this complement is already in the set, we've found a pair that sums to the target.
# We add the pair to the list of pairs, but only if the pair is not already in the list.
# The time complexity is O(n) because each element is processed only once.

#### Time Complexity
# The time complexity of this solution is O(n), where n is the number of elements in the input array.

#### Space Complexity
#   The space complexity of this solution is O(n), where n is the number of elements in the input array. This is because we use a set to store the numbers we've already encountered, and in the worst case, we might need to store all elements in the set.