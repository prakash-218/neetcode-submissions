class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        so_fa = -float("inf")
        curr = 0
        for i in nums:
            curr += i
            so_fa = max(so_fa, curr)
            curr = max(curr, 0)
        return so_fa
        
        