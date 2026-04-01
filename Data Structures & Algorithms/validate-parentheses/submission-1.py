class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {'{':'}', '(':')', '[':']'}
        for b in s:
            if b in pairs:
                st.append(pairs[b])
            else:
                if not st: return False
                closing = st.pop()
                if b != closing: return False
        return not st
        