class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini, maxi = nums[0], nums[0]
        best = nums[0]

        for i in nums[1:]:
            multMax = i * maxi
            multMin = i * mini
            mini = min(i, multMax, multMin)
            maxi = max(i, multMax, multMin)
            best = max(best, maxi)
        return best
