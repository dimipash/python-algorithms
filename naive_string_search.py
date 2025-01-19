def naive_string_search(text, pattern):
    """
    Implements naive string search algorithm to find all occurrences of pattern in text.

    Time Complexity: O(nm) where n is text length, m is pattern length
    Space Complexity: O(k) where k is number of pattern occurrences

    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for

    Returns:
        list: Indices where pattern occurs in text
    """
    n = len(text)
    m = len(pattern)
    indices = []

    # Check pattern at each possible position in text
    for i in range(n - m + 1):
        # Compare characters one by one
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        # Store index if pattern found
        if match:
            indices.append(i)

    return indices


# Example usage
if __name__ == "__main__":
    text = "abracadabra"
    pattern = "abra"
    matches = naive_string_search(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {matches}")
