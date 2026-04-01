class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        n = len(s)
        d = {}
        res = 0
        prev = -1
        while r < n:
            if r != prev:
                d[s[r]] = d.get(s[r], 0) + 1
            maxi = 0
            for i in d:
                maxi = max(maxi, d[i])
            prev = r
            sub = r - l + 1
            if sub - maxi <= k:
                res = max(res, sub)
                r += 1
            else:
                d[s[l]] = d.get(s[l], 0 ) - 1
                l += 1
        print(d)
        return res
