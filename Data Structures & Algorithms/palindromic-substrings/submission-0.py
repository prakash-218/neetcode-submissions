class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):

            # odd length case
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                res += 1
            
            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                res += 1
            
            i += 1
        return res
        