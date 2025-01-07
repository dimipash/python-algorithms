from typing import List, Dict, Optional
import time


class CoinChange:
    """
    Implements solutions for the Coin Change problem using different approaches.
    Finds minimum coins needed and counts total possible combinations.
    """

    def __init__(self, coins: List[int]):
        self.coins = sorted(coins)
        self.memo: Dict[int, int] = {}

    def min_coins_dp(self, amount: int) -> int:
        """
        Finds minimum coins needed using dynamic programming.

        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        if amount < 0:
            return -1

        # Initialize dp array
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # Fill dp array
        for coin in self.coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1

    def min_coins_recursive(self, amount: int) -> int:
        """
        Recursive solution with memoization.
        """
        if amount in self.memo:
            return self.memo[amount]

        if amount == 0:
            return 0
        if amount < 0:
            return -1

        min_coins = float("inf")
        for coin in self.coins:
            result = self.min_coins_recursive(amount - coin)
            if result >= 0:
                min_coins = min(min_coins, result + 1)

        self.memo[amount] = min_coins if min_coins != float("inf") else -1
        return self.memo[amount]

    def count_combinations(self, amount: int) -> int:
        """
        Counts total number of combinations to make amount.

        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in self.coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]

    def find_coin_combination(self, amount: int) -> Optional[List[int]]:
        """
        Finds one possible combination of coins.
        Returns None if not possible.
        """
        if amount < 0:
            return None

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        parent = [-1] * (amount + 1)

        for coin in self.coins:
            for x in range(coin, amount + 1):
                if dp[x] > dp[x - coin] + 1:
                    dp[x] = dp[x - coin] + 1
                    parent[x] = coin

        if dp[amount] == float("inf"):
            return None

        # Reconstruct solution
        result = []
        while amount > 0:
            result.append(parent[amount])
            amount -= parent[amount]

        return result


def benchmark_methods(solver: CoinChange, amount: int) -> None:
    """Compares performance of different methods."""
    # Test DP solution
    start = time.perf_counter()
    dp_result = solver.min_coins_dp(amount)
    dp_time = time.perf_counter() - start

    # Test recursive solution
    start = time.perf_counter()
    rec_result = solver.min_coins_recursive(amount)
    rec_time = time.perf_counter() - start

    print("\nPerformance comparison:")
    print(f"DP Solution: {dp_time:.6f} seconds")
    print(f"Recursive: {rec_time:.6f} seconds")

    assert dp_result == rec_result, "Results don't match!"


def main():
    test_cases = [
        ([1, 2, 5], 11, "Basic case"),
        ([2], 3, "Impossible amount"),
        ([1], 0, "Zero amount"),
        ([1, 5, 10, 25], 30, "Common coins"),
        ([186, 419, 83, 408], 6249, "Large amount"),
    ]

    for coins, amount, case_type in test_cases:
        print(f"\nCase: {case_type}")
        print(f"Coins: {coins}")
        print(f"Amount: {amount}")

        solver = CoinChange(coins)

        # Find minimum coins needed
        min_coins = solver.min_coins_dp(amount)
        print(f"Minimum coins needed: {min_coins}")

        # Find one possible combination
        combination = solver.find_coin_combination(amount)
        if combination:
            print(f"One possible combination: {combination}")
            print(f"Verification: sum = {sum(combination)}")

        # Count total combinations
        if amount <= 100:  # Only for reasonable amounts
            combinations = solver.count_combinations(amount)
            print(f"Total possible combinations: {combinations}")

        # Benchmark methods
        if amount <= 1000:
            benchmark_methods(solver, amount)


if __name__ == "__main__":
    main()
