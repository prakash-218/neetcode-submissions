class Solution:
    def longestPalindrome(self, s: str) -> str:
        # at every index, we need to expand outwards
        # even then there are two cases, 
        #   palindrome is odd length
        #   palindrome is even length
        # for odd, l = i, r = i and expand until s[l] != s[r]
        # for even, l = i - 1, r = i and expand until s[l] != s[r]
        idx = 0
        n = len(s)
        best = 0
        lbest = 0
        rbest = 0
        while idx < n:
            # testing odd
            odd, l, r = solve(n, s, idx, idx)
            # print("odd", best, odd, l, r)
            if odd > best:
                best = odd
                lbest = l
                rbest = r 
            even, l, r = solve(n, s, idx - 1, idx)
            if even > best:
                best = even
                lbest = l
                rbest = r 
            idx += 1
        return s[lbest:rbest+1]

        
def solve(n, s, l, r):
    while l >= 0 and r < n:
        if s[l] != s[r]:
            return r - l - 1, l + 1, r - 1
        l -= 1
        r += 1
    return r - l - 1, l + 1, r - 1

