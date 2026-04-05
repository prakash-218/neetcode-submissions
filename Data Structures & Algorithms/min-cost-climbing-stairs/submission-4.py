class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost) + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        n = len(cost)
        cost.append(0) # padding
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return dp[-1] 
        