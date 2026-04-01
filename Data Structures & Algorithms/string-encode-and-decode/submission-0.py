class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            length = len(string)
            length_of_length = len(str(length))
            res += str(length_of_length) + str(length) + string
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        idx = 0
        res = []
        while idx < len(s):
            length_ = int(s[idx])
            idx += 1
            count = 0
            length = ""
            while count < length_:
                length += s[idx]
                count += 1
                idx += 1
            length = int(length)
            count = 0
            curr = ""
            while count < length:
                curr += s[idx]
                count += 1
                idx += 1
            res.append(curr)
        return res
