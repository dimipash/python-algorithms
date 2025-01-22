def word_pattern(pattern: str, s: str) -> bool:
    """
    Determines if a string matches a given pattern with consistent character-to-word mapping.

    Parameters:
    pattern (str): The pattern string consisting of characters.
    s (str): The input string consisting of words separated by spaces.

    Returns:
    bool: True if the string matches the pattern, False otherwise.

    Time Complexity: O(N), where N is the length of the pattern.
    Space Complexity: O(N), where N is the length of the pattern.
    """
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for p, w in zip(pattern, words):
        if p not in char_to_word:
            char_to_word[p] = w
        if w not in word_to_char:
            word_to_char[w] = p
        if char_to_word[p] != w or word_to_char[w] != p:
            return False
    return True


# Example usage
if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    match_result = word_pattern(pattern, s)
    print(f"Does the string '{s}' match the pattern '{pattern}'? {match_result}")
