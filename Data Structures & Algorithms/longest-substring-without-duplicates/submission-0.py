class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        idx = 0
        n = len(s)
        result = 0
        current = 0
        left = 0
        while idx < n:
            char = s[idx]
            if char in d and d[char] != -1:
                # we have to start deleting from left until char[d]
                stop = d[char]
                while left <= stop:
                    char_to_del = s[left]
                    d[char_to_del] = -1
                    left += 1
            d[char] = idx
            result = max(result, idx - left + 1)
            idx += 1
        return result

