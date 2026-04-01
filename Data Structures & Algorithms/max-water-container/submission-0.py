class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            at_left = heights[left]
            at_right = heights[right]

            curr = min(at_left, at_right) * (right - left)
            res = max(res, curr)

            if at_left < at_right:
                left += 1
            else:
                right -= 1
        return res
        