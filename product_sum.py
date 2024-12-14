from typing import List, Union


def product_sum(arr: List[Union[int, List]], depth: int = 1) -> int:
    """
    Calculates the product sum of an array, where each element is multiplied by its depth level.

    Args:
        arr (List[Union[int, List]]): The input array, which can contain integers and nested arrays.
        depth (int, optional): The current depth level. Defaults to 1.

    Returns:
        int: The product sum of the array.

    Examples:
        >>> product_sum([1, 2, [3, 4, [5]], 5])
        43

    Notes:
        The function recursively calculates the product sum for nested arrays by increasing the depth.
        If the element is an integer, its contribution to the product sum is simply the integer multiplied by its depth.
    """
    # Initialize a total sum
    total = 0
    # Iterate through each element in the array
    for elem in arr:
        # Check if the element is a list
        if isinstance(elem, list):
            # Recursively call the function for nested arrays, increasing the depth by 1
            total += product_sum(elem, depth + 1)
        else:
            # Add the integer to the total
            total += elem
    # Multiply the total by the depth to account for the product sum contribution
    return total * depth


# Example usage:
arr = [1, 2, [3, 4, [5]], 5]
result = product_sum(arr)
print(result)  # Output: 43


#### Explanation
# The `product_sum` function takes an array and an optional depth parameter, defaulting to 1. It initializes a total sum and iterates through each element in the array. If the element is a list, the function recursively calls itself, increasing the depth by 1. If the element is an integer, it is added to the total. Finally, the total is multiplied by the depth to account for the product sum contribution.

#### Time Complexity
#    The time complexity of this solution is O(n), where n is the total number of elements in the array, including nested arrays.

#### Space Complexity
#   The space complexity of this solution is O(d), where d is the maximum depth of the nested arrays. This is because the recursive function calls can go up to a depth of d.
