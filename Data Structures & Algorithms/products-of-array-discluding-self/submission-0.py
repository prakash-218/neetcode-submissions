class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in nums[:-1]:
            left.append(left[-1] * i)
        for i in nums[::-1][:-1]:
            right.append(right[-1] * i)
        print(left, right[::-1])
        right = right[::-1]
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res
        
        