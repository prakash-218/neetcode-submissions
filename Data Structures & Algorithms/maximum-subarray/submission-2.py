class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -float('inf')
        curr = 0
        for i in nums:
            new = curr + i
            curr = max(new, i)
            best = max(best, curr)
        return best