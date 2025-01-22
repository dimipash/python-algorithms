def reverse_letters(text):
    """
    Reverses letters in each word while maintaining word order.

    Time Complexity: O(n) where n is length of text
    Space Complexity: O(n) for storing reversed string
    """
    # Split text into words and reverse each word's letters
    return " ".join(word[::-1] for word in text.split())


def reverse_letters_loop(text):
    """
    Reverses letters using explicit loop approach.

    Time Complexity: O(n) where n is length of text
    Space Complexity: O(n) for storing reversed words
    """
    words = text.split()
    reversed_words = []
    for word in words:
        # Reverse letters in each word
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)


# Example usage
if __name__ == "__main__":
    test_text = "Hello World Python"
    print(f"Original: {test_text}")
    print(f"Reversed (slicing): {reverse_letters(test_text)}")
    print(f"Reversed (loop): {reverse_letters_loop(test_text)}")
