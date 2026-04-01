class Solution:
    def longestPalindrome(self, s: str) -> str:

        idx = 0
        n = len(s)
        bestLen = 1
        bestStr = s[0]
        while idx < n:
            # considering odd length
            left = idx - 1
            right = idx + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > bestLen:
                    bestLen = right - left + 1
                    bestStr = s[left: right + 1]
                left -= 1
                right += 1
            
            #considering even length
            left = idx
            right = idx + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > bestLen:
                    bestLen = right - left + 1
                    bestStr = s[left: right + 1]
                left -= 1
                right += 1
            idx += 1
        return bestStr

        