class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s == 0:
                    res.append([a, nums[l], nums[r]])
                    prevL = nums[l]
                    prevR = nums[r]
                    l += 1
                    r -= 1
                    while l < r and prevL == nums[l]:
                        l += 1
                    while r > l and prevR == nums[r]:
                        r -= 1
                if s < 0:
                    l += 1
                if s > 0:
                    r -= 1
        return res
