class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        res = 0
        for price in prices:
            diff = price - min_so_far
            res = max(res, diff)
            min_so_far = min(price, min_so_far)
        return res if res > 0 else 0