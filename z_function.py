def z_function(s: str) -> list[int]:
    """
    Computes Z array for a given string where Z[i] represents the length of the longest
    substring starting from index i that matches a prefix of the string.

    Time Complexity: O(n) where n is the length of the input string
    Space Complexity: O(n) for storing the Z array

    Args:
        s (str): Input string to process

    Returns:
        list[int]: Z array containing lengths of matching prefixes

    Example:
        >>> z_function("aabcaabxaaaz")
        [0, 1, 0, 0, 4, 1, 0, 0, 2, 2, 1, 0]
        # For "aabcaabxaaaz":
        # Z[4] = 4 because "aabx" matches with prefix "aabc"
        # Z[8] = 2 because "aa" matches with prefix "aa"
    """
    n = len(s)
    z = [0] * n  # Initialize Z array with zeros

    # [l,r] form a window of previously matched substring
    l = r = 0

    # Start from index 1 as Z[0] is always 0
    for i in range(1, n):
        if i > r:  # If current position is outside the window
            l = r = i
            # Expand window while characters match
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            # If we're inside the window, use previously computed values
            k = i - l
            if z[k] < r - i + 1:  # If value fits inside window
                z[i] = z[k]
            else:  # Need to expand window
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z
