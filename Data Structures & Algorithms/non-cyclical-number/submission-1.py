class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        while True:
            print(n, vis)
            n = process(n)
            if n in vis:
                return False
            vis.add(n)
            if n == 1:
                return True
        return False

def process(n):
    res = 0
    while n > 0:
        curr = n%10
        sq = curr ** 2
        res += sq
        n //= 10
    return res
        