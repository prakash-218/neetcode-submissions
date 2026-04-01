class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = str(len(string))
            length_of_length = str(len(length))
            result += length_of_length + length + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0
        end = len(s)
        while idx < end:
            length_of_length = int(s[idx])
            j = idx + 1
            length = ''
            while j < idx + length_of_length + 1:
                length += s[j]
                j += 1
            idx = j
            length = int(length)
            string = s[idx:idx+length]
            result.append(string)
            idx += length
        return result

