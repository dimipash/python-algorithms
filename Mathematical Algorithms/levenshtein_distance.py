"""
Levenshtein Distance Calculator

Calculates the minimum number of single-character edits (insertions,
deletions, substitutions) required to transform one string into another.
Uses dynamic programming for efficient computation.

Time Complexity: O(mn) where m,n are string lengths
Space Complexity: O(mn) for the DP matrix
"""


def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculate Levenshtein distance between two strings.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        int: Minimum number of edits required

    Examples:
        >>> levenshtein_distance("kitten", "sitting")
        3
        >>> levenshtein_distance("hello", "world")
        4
    """
    # Get string lengths
    m, n = len(s1), len(s2)

    # Create DP matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Deletions
    for j in range(n + 1):
        dp[0][j] = j  # Insertions

    # Fill DP matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + 1,  # Substitution
                )

    return dp[m][n]


def get_operations(s1: str, s2: str) -> list:
    """
    Get sequence of operations to transform s1 into s2.

    Args:
        s1 (str): Source string
        s2 (str): Target string

    Returns:
        list: Sequence of edit operations
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    # Backtrack to find operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Delete '{s1[i-1]}'")
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(f"Insert '{s2[j-1]}'")
            j -= 1
        else:
            operations.append(f"Replace '{s1[i-1]}' with '{s2[j-1]}'")
            i -= 1
            j -= 1

    return operations[::-1]


def main() -> None:
    """
    Demonstrate Levenshtein distance calculation with examples.
    """
    test_cases = [
        ("kitten", "sitting"),
        ("hello", "world"),
        ("sunday", "saturday"),
        ("", "test"),
        ("abc", "abc"),
    ]

    for s1, s2 in test_cases:
        distance = levenshtein_distance(s1, s2)
        operations = get_operations(s1, s2)

        print(f"\nTransforming '{s1}' to '{s2}':")
        print(f"Distance: {distance}")
        print("Operations:")
        for op in operations:
            print(f"- {op}")


if __name__ == "__main__":
    main()
