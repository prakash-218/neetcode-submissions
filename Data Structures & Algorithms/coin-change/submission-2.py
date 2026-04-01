class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(amount):
            if i != 0 and dp[i] == float('inf'):
                continue
            for coin in coins:
                if coin + i <= amount:
                    dp[coin + i] = min(dp[coin + i], dp[i] + 1)
        print(dp)
        return -1 if dp[-1] == float('inf') else dp[-1]