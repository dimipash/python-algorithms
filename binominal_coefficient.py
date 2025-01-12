"""
Binomial Coefficient Calculator

Provides two methods for computing binomial coefficients:
1. Using factorials (faster for small numbers)
2. Using dynamic programming (better for large numbers)

Time Complexity: 
- Factorial method: O(n) due to factorial calculation
- Dynamic Programming method: O(n*k) to fill the table
Space Complexity:
- Factorial method: O(1)
- Dynamic Programming method: O(n*k) for the table
"""


def binomial_coefficient_factorial(n: int, k: int) -> int:
    """
    Calculate binomial coefficient using factorial method.

    Args:
        n (int): Total number of elements
        k (int): Number of elements to choose

    Returns:
        int: Binomial coefficient C(n,k)
    """
    if k < 0 or k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def binomial_coefficient_dp(n: int, k: int) -> int:
    """
    Calculate binomial coefficient using dynamic programming.

    Args:
        n (int): Total number of elements
        k (int): Number of elements to choose

    Returns:
        int: Binomial coefficient C(n,k)
    """
    if k < 0 or k > n:
        return 0

    # Create and initialize dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = 1  # C(n,0) = 1
    for j in range(k + 1):
        if j <= n:
            dp[j][j] = 1  # C(n,n) = 1

    # Fill dp table using Pascal's identity
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]


def main() -> None:
    """
    Demonstrate both methods with example cases.
    """
    test_cases = [
        (5, 2),  # Small numbers
        (10, 5),  # Medium numbers
        (20, 10),  # Larger numbers
    ]

    for n, k in test_cases:
        result1 = binomial_coefficient_factorial(n, k)
        result2 = binomial_coefficient_dp(n, k)
        print(f"C({n},{k}) = {result1} (factorial method)")
        print(f"C({n},{k}) = {result2} (dynamic programming method)")


if __name__ == "__main__":
    main()
