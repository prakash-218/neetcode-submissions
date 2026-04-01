class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            new = [0 for j in range(26)]
            for k in i:
                new[ord(k) - ord('a')] += 1
            if str(new) in d:
                d[str(new)].append(i)
            else:
                d[str(new)] = [i]
        return d.values()
        