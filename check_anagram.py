"""
Anagram Checker

Determines if two strings are anagrams by comparing character frequencies.
Supports case-insensitive comparison and handles spaces.

Time Complexity: O(n) where n is length of longer string
Space Complexity: O(k) where k is size of character set
"""

from collections import Counter
from typing import Dict


def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams.

    Args:
        str1 (str): First string
        str2 (str): Second string

    Returns:
        bool: True if strings are anagrams

    Examples:
        >>> are_anagrams("listen", "silent")
        True
        >>> are_anagrams("hello", "world")
        False
    """
    # Clean strings
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Quick length check
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


def are_anagrams_manual(str1: str, str2: str) -> bool:
    """
    Check anagrams without using Counter class.

    Args:
        str1 (str): First string
        str2 (str): Second string

    Returns:
        bool: True if strings are anagrams
    """
    # Clean strings
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    # Count characters
    char_count: Dict[str, int] = {}

    # Count characters in first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract counts for second string
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    return len(char_count) == 0


def main() -> None:
    """
    Demonstrate anagram checking with examples.
    """
    test_cases = [
        ("listen", "silent"),  # True
        ("hello", "world"),  # False
        ("debit card", "bad credit"),  # True
        ("python", "java"),  # False
        ("", ""),  # True
    ]

    for str1, str2 in test_cases:
        # Test both methods
        result1 = are_anagrams(str1, str2)
        result2 = are_anagrams_manual(str1, str2)

        print(f"Strings: '{str1}' and '{str2}'")
        print(f"Using Counter: {result1}")
        print(f"Using manual count: {result2}\n")


if __name__ == "__main__":
    main()
