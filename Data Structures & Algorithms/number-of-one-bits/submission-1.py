class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            if n & 1 != 0: res += 1
            n >>=1
        return res
        # count = 0
        # res = 0
        # while count < 32:
        #     print(2 ** count, 2**count & n, n)
        #     res += 1 if (2 ** count & n) > 0 else 0
        #     count += 1
        # return res
        