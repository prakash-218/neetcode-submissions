class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for j,i in enumerate(nums):
            balance = target - i
            if balance in d:
                return [d[balance], j]
            d[i] = j
        
        