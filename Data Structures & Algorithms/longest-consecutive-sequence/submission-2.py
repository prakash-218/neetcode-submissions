class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 1
        idx = 0
        n = len(nums)
        result = 0
        while idx < n:
            num = nums[idx]
            if num - 1 in d:
                idx += 1
                continue
            
            # this means num could be the start of the series
            count = 1
            while num + 1 in d:
                count += 1
                num += 1
            result = max(result, count)

            idx += 1
        return result