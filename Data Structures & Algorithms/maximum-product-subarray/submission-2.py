class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini, maxi = nums[0], nums[0]
        best = nums[0]

        for i in nums[1:]:
            mult_mini = mini * i
            mutl_maxi = maxi * i
            mini = min(mult_mini, mutl_maxi, i)
            maxi = max(mult_mini, mutl_maxi, i)
            best = max(best, maxi)
        return best
