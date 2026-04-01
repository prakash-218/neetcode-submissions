class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxToRight = nums[0]
        for idx, num in enumerate(nums):
            if idx <= maxToRight:
                maxToRight = max(maxToRight, idx + num)
        return maxToRight + 1 >= len(nums)

