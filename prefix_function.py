def compute_prefix_function(s):
    """
    Computes the prefix function (pi) array for a string, where pi[i] is the length of
    the longest proper prefix that is also a suffix of s[0:i+1].

    Time Complexity: O(n) where n is length of string
    Space Complexity: O(n) for storing prefix array

    Args:
        s (str): Input string to compute prefix function for

    Returns:
        list: Array containing prefix function values
    """
    n = len(s)
    # Initialize prefix array with zeros
    pi = [0] * n

    # j tracks length of current prefix
    j = 0

    # Compute prefix values for each position
    for i in range(1, n):
        # Backtrack until we find matching prefix or reach beginning
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]

        # If characters match, extend prefix
        if s[i] == s[j]:
            j += 1

        # Store prefix length for current position
        pi[i] = j

    return pi


# Example usage
if __name__ == "__main__":
    test_strings = ["abacab", "aaaa", "ababab"]

    for s in test_strings:
        prefix_array = compute_prefix_function(s)
        print(f"String: {s}")
        print(f"Prefix Function: {prefix_array}")
        print()
