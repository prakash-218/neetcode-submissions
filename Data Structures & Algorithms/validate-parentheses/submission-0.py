class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        st = []
        for i in s:
            if i in pairs:
                st.append(pairs[i])
            else:
                if len(st) == 0:
                    return False
                last = st.pop()
                if i != last:
                    return False
        return True if len(st) == 0 else False
        