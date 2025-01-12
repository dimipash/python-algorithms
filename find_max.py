"""
Maximum Value Finder

Provides various methods to find maximum values in collections:
1. Built-in max() function for simple cases
2. Manual iteration for custom logic
3. Key-based comparison for complex objects

Time Complexity: O(n) for all methods
Space Complexity: O(1) for all methods
"""


def find_max_builtin(numbers: list) -> int:
    """Find maximum using built-in max()."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


def find_max_manual(numbers: list) -> int:
    """Find maximum using manual iteration."""
    if not numbers:
        raise ValueError("List cannot be empty")
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_max_with_key(items: list, key=None) -> any:
    """Find maximum using custom key function."""
    if not items:
        raise ValueError("List cannot be empty")
    return max(items, key=key)


def main() -> None:
    """Demonstrate different maximum finding methods."""
    # Test basic number list
    numbers = [3, 5, 1, 8, 2]
    print(f"Built-in max: {find_max_builtin(numbers)}")
    print(f"Manual max: {find_max_manual(numbers)}")

    # Test with strings and key function
    strings = ["apple", "banana", "cherry"]
    longest = find_max_with_key(strings, key=len)
    print(f"Longest string: {longest}")

    # Test with multiple lists
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"Max list: {max(list1, list2)}")


if __name__ == "__main__":
    main()
