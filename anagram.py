"""
Anagram Generator and Checker

Provides functions to generate anagrams, check if strings are anagrams,
and generate anagrams in lexicographic order.

Time Complexity: O(n!) for generation, O(n log n) for checking
Space Complexity: O(n!) for storing all anagrams
"""

from itertools import permutations
from collections import Counter


def generate_anagrams(s: str) -> set:
    """
    Generate all possible unique anagrams of a string.

    Args:
        s (str): Input string

    Returns:
        set: Set of all unique anagrams

    Examples:
        >>> generate_anagrams("abc")
        {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
    """
    return set("".join(p) for p in permutations(s))


def are_anagrams_sorting(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using sorting method.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        bool: True if strings are anagrams
    """
    return sorted(s1) == sorted(s2)


def are_anagrams_frequency(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using character frequency.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        bool: True if strings are anagrams
    """
    return Counter(s1) == Counter(s2)


def lexicographic_anagrams(s: str) -> list:
    """
    Generate anagrams in lexicographic order.

    Args:
        s (str): Input string

    Returns:
        list: Sorted list of anagrams
    """
    return sorted("".join(p) for p in permutations(s))


def main() -> None:
    """
    Demonstrate anagram operations.
    """
    # Generate all anagrams
    s = "abc"
    anagrams = generate_anagrams(s)
    print(f"Anagrams of '{s}': {anagrams}")

    # Check if strings are anagrams
    s1, s2 = "listen", "silent"
    result1 = are_anagrams_sorting(s1, s2)
    result2 = are_anagrams_frequency(s1, s2)
    print(f"Are '{s1}' and '{s2}' anagrams?")
    print(f"Using sorting: {result1}")
    print(f"Using frequency: {result2}")

    # Generate lexicographic anagrams
    s = "bca"
    lex_anagrams = lexicographic_anagrams(s)
    print(f"Lexicographic anagrams of '{s}': {lex_anagrams}")


if __name__ == "__main__":
    main()
