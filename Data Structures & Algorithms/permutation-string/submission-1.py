class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        one = [0] * 26
        two = [0] * 26
        one_len = len(s1)
        two_len = len(s2)
        if two_len < one_len:
            return False
        
        for letter in s1:
            idx = ord(letter) - ord('a')
            one[idx] += 1
        
        l, r = 0, 0
        while r < one_len:
            idx = ord(s2[r]) - ord('a')
            two[idx] += 1
            r += 1
        
        while r < two_len:
            if compare(one, two):
                return True
            print(one, two)
            # drop l, add r
            idx = ord(s2[l]) - ord('a')
            two[idx] -= 1
            idx = ord(s2[r]) - ord('a')
            two[idx] += 1
            l += 1
            r += 1
        if compare(one, two):
                return True
        
        return False

def compare(a, b):
    for i, j in zip(a,b):
        if i != j:
            return False
    return True

        