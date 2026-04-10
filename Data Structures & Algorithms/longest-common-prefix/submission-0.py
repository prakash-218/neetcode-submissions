class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr = strs[0]

        for s in strs:
            curr = getCommon(curr, s)
        return curr
    

def getCommon(pre, s):
    idx = 0
    i = len(pre)
    j = len(s)
    while idx < i and idx < j:
        if pre[idx] != s[idx]:
            break
        idx += 1
    return s[:idx]