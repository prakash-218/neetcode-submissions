class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx = 0
        s = 0
        while idx < len(abbr) and s < len(word):
            currA = abbr[idx]
            if currA.isalpha():
                currW = word[s]
                if currA != currW:
                    return False
                s += 1
                idx += 1
            else:
                num = ''
                while idx < len(abbr) and abbr[idx].isdigit():
                    num += abbr[idx]
                    idx += 1
                if num[0] == '0':
                    return False
                num = int(num)
                s += num
        if s != len(word) or idx != len(abbr):
            return False
        return True


        