class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for i in nums:
            d[i] = 1
        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            prev = curr - 1
            nex  = curr + 1
            if not d[curr]:
                continue
            while prev in d:
                count += 1
                d[prev] = 0
                prev -= 1
            while nex in d:
                count += 1
                d[nex] = 0
                nex += 1
            res = max(res, count)
        return res
        