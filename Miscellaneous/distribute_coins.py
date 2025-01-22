import math


def comb(n, k):
    """
    Calculates the number of combinations of n items taken k at a time.

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose.

    Returns:
        int: The number of combinations.

    Notes:
        This function uses the formula for combinations: n! / (k! * (n-k)!)
        It also takes advantage of symmetry to reduce the number of calculations.
    """
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def distribute_coins(n, k):
    """
    Calculates the number of ways to distribute n coins into k piles.

    Each pile must have at least one coin, and the remaining coins are distributed as evenly as possible.

    Args:
        n (int): The total number of coins.
        k (int): The total number of piles.

    Returns:
        int: The number of ways to distribute the coins.

    Notes:
        This function uses the formula for combinations to calculate the number of ways to distribute the coins.
        If there are not enough coins to give at least one to each pile, it returns 0.

        Explanation:
            1. The comb function calculates the number of combinations of n items taken k at a time.
            2. The distribute_coins function calculates the number of ways to distribute n coins into k piles.
            3. If there are not enough coins to give at least one to each pile, it returns 0.
            4. Otherwise, it uses the formula for combinations to calculate the number of ways to distribute the coins.

        Time Complexity: O(k), where k is the number of piles.
        Space Complexity: O(1), since we only use a constant amount of space to store the result.
    """
    if n < k:  # Not enough coins to give at least one to each pile
        return 0
    return comb(n - 1, k - 1)  # Combinations of (n-1) choose (k-1)


# Example usage:
if __name__ == "__main__":
    n = 10  # Total coins
    k = 3  # Total piles
    result = distribute_coins(n, k)
    print(result)  # Output: 36 (ways to distribute 10 coins into 3 piles)
