"""
Bitap String Matching Algorithm

Implements approximate string matching using bitwise operations.
Originally invented by Dömölki (1964) and extended by Baeza-Yates and 
Gonnet (1989).

Time Complexity: O(m*n) where m=pattern length, n=text length
Space Complexity: O(m) for pattern mask storage
"""


def bitap_search(text: str, pattern: str) -> int:
    """
    Search for pattern in text using Bitap algorithm.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        int: Index of first match, or -1 if not found

    Examples:
        >>> bitap_search("hello world", "world")
        6
        >>> bitap_search("abdabababc", "ababc")
        5
    """
    # Handle edge cases
    if not pattern:
        return 0
    if len(pattern) > 63:  # Typical machine word length limitation
        raise ValueError("Pattern length exceeds maximum")

    m = len(pattern)
    pattern_mask = {}

    # Precompute pattern bitmasks
    for i in range(m):
        pattern_mask[pattern[i]] = pattern_mask.get(pattern[i], 0) | (1 << i)

    # Initialize state
    current_state = 0

    # Process text character by character
    for i in range(len(text)):
        if text[i] in pattern_mask:
            current_state = ((current_state << 1) | 1) & pattern_mask[text[i]]
        else:
            current_state = (current_state << 1) | 1

        # Check if pattern is found
        if current_state & (1 << (m - 1)) == 0:
            return i - m + 1

    return -1  # Pattern not found


def main() -> None:
    """
    Demonstrate Bitap string matching.
    """
    test_cases = [
        ("hello world", "world"),  # Basic match
        ("abdabababc", "ababc"),  # Overlapping pattern
        ("aaaaaaa", "aaa"),  # Repeating characters
        ("test", "xyz"),  # No match
    ]

    for text, pattern in test_cases:
        result = bitap_search(text, pattern)
        print(f"Text: {text}")
        print(f"Pattern: {pattern}")
        print(f"Match at index: {result}\n")


if __name__ == "__main__":
    main()
