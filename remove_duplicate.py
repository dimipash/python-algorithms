def remove_duplicates_list(lst):
    """
    Removes duplicates from a list using set conversion.
    Does not maintain original order.

    Time Complexity: O(n) where n is length of list
    Space Complexity: O(n) for storing unique elements

    Args:
        lst (list): Input list with potential duplicates

    Returns:
        list: List with duplicates removed
    """
    return list(set(lst))


def remove_duplicates_list_ordered(lst):
    """
    Removes duplicates from a list while maintaining original order.

    Time Complexity: O(n) where n is length of list
    Space Complexity: O(n) for storing unique elements

    Args:
        lst (list): Input list with potential duplicates

    Returns:
        list: List with duplicates removed, maintaining order
    """
    unique_list = []
    # Add items to new list only if not seen before
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def remove_duplicates_dict(lst):
    """
    Removes duplicates using dictionary to maintain order.
    More efficient than list checking for large inputs.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return list(dict.fromkeys(lst))


# Example usage
if __name__ == "__main__":
    # Test with numbers
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original list: {numbers}")
    print(f"Using set: {remove_duplicates_list(numbers)}")
    print(f"Maintaining order: {remove_duplicates_list_ordered(numbers)}")
    print(f"Using dict: {remove_duplicates_dict(numbers)}")

    # Test with strings
    words = ["hello", "world", "hello", "python", "world"]
    print(f"\nOriginal list: {words}")
    print(f"Using set: {remove_duplicates_list(words)}")
    print(f"Maintaining order: {remove_duplicates_list_ordered(words)}")
    print(f"Using dict: {remove_duplicates_dict(words)}")
