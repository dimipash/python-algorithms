def next_greater_element(arr):
    """
    Finds the next greater element for each element in the array.

    Parameters:
    arr (list of int): The input array of integers.

    Returns:
    list of int: A list where each element is replaced by the next greater element to its right. If no such element exists, the value is -1.

    Time Complexity: O(n), where n is the number of elements in the array.
    Space Complexity: O(n), due to the stack and the result list.
    """
    stack, result = [], [-1] * len(arr)  # Initialize stack and result list
    for i in range(len(arr)):  # Iterate through each element's index
        while (
            stack and arr[i] > arr[stack[-1]]
        ):  # While current element is greater than the element at the index on top of the stack
            result[stack.pop()] = arr[
                i
            ]  # Set the result for the popped index to the current element
        stack.append(i)  # Push the current index onto the stack
    return result  # Return the result list


# Example usage
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]

    # Additional test cases
    print(next_greater_element([5, 4, 3, 2, 1]))  # Output: [-1, -1, -1, -1, -1]
    print(next_greater_element([1, 2, 3, 4, 5]))  # Output: [2, 3, 4, 5, -1]
    print(next_greater_element([10]))  # Output: [-1]
    print(next_greater_element([3, 3, 3]))  # Output: [-1, -1, -1]
    print(next_greater_element([-1, -2, -3, -4]))  # Output: [-1, -1, -1, -1]
    print(next_greater_element([1, -1, 2, -3, 4]))  # Output: [2, 2, 4, 4, -1]
