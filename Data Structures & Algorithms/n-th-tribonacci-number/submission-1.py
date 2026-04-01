class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1]
        for i in range(n - 2):
            res.append(res[-1] + res[-2] + res[-3])
        return res[n]
        