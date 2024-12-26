def is_sorted(arr):
    """
    Checks whether a given list is sorted in ascending or descending order.

    This function iterates through the list and determines if it is sorted
    in either ascending or descending order.

    :param arr: List of comparable elements (e.g., integers, floats).
    :return: A tuple containing two boolean values:
    (is_sorted_ascending, is_sorted_descending).

    Time Complexity: O(n), where n is the number of elements in the array.
    Space Complexity: O(1), as we are using a constant amount of space.
    """
    ascending, descending = True, True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:  # Check for ascending order
            ascending = False
        if arr[i] > arr[i - 1]:  # Check for descending order
            descending = False

        # Early exit if both flags are False
        if not ascending and not descending:
            break

    return ascending, descending


# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ascending, descending = is_sorted(arr)
    print(
        f"Is Ascending: {ascending}, Is Descending: {descending}"
    )  # Output: Is Ascending: True, Is Descending: False
