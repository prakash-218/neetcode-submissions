class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        power = 0
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            res.append(rem)
            columnNumber //= 26
        print(res)
        resStr = ''.join([chr(i + ord('A')) for i in res[::-1]])
        return resStr