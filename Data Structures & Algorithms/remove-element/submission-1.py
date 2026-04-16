class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        rep = len(nums) - 1
        while rep >= 0 and nums[rep] == val:
            rep -= 1
        
        while idx <= rep:
            if nums[idx] == val:
                nums[idx], nums[rep] = nums[rep], nums[idx]
                while rep >= 0 and nums[rep] == val:
                    rep -= 1
            idx += 1
        return idx
        