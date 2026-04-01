class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin])
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1

        