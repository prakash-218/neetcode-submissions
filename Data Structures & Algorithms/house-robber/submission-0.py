class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0 for i in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], nums[i] + res[i - 2])
        print(res)
        return res[-1]

        