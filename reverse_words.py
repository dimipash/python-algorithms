from typing import List


def reverse_words(text: str) -> str:
    """Reverses letters in each word while maintaining word order.

    Splits string into words, reverses each word's characters using slicing,
    then joins words back with spaces.

    Time: O(n) - Split, reverse, and join operations
    Space: O(n) - To store reversed string

    Args:
        text: Input string containing words to reverse

    Returns:
        String with letters in each word reversed

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return " ".join(word[::-1] for word in text.split())


# Example usage
if __name__ == "__main__":
    print(reverse_words("Hello World"))  # Outputs: "olleH dlroW"
    print(reverse_words("Python Programming"))  # Outputs: "nohtyP gnimmargorP"
    print(reverse_words(""))  # Empty string
