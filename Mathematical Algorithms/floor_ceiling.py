def find_floor_and_ceiling(arr, target):
    """
    Finds the floor and ceiling values of a given target in a sorted array.

    The floor is defined as the largest number in the array that is less than or equal to the target,
    while the ceiling is the smallest number that is greater than or equal to the target.

    :param arr: List of sorted integers.
    :param target: The target value to find the floor and ceiling for.
    :return: A tuple containing the floor and ceiling values (floor, ceiling).

    Time Complexity: O(n), where n is the number of elements in the array.
    Space Complexity: O(1), as we are using a constant amount of space.
    """
    floor, ceiling = None, None

    for num in arr:
        if num <= target:
            floor = num  # Update floor if num is less than or equal to target
        if num >= target and ceiling is None:  # Update ceiling only once
            ceiling = num
            break  # Exit loop early since we found the ceiling

    return floor, ceiling


# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 8, 10, 10, 12, 19]
    target = 5
    floor, ceiling = find_floor_and_ceiling(arr, target)
    print(f"Floor: {floor}, Ceiling: {ceiling}")  # Output: Floor: 2, Ceiling: 8
