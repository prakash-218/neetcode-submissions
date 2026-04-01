class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        idx = 0
        while idx < len(s):
            curr_vis = set()
            init = idx
            curr = s[idx]
            curr_vis.add(curr)
            last = get_last(idx, curr, s)
            idx += 1
            print(curr, last)
            # we know the last occurence of current character
            # now we have to check all the chars between idx and last and update last accordingly
            while idx <= last:
                new = s[idx]
                if new in curr_vis:
                    idx += 1
                    continue
                curr_vis.add(new)
                new_last = get_last(idx, new, s)
                last = max(last, new_last)
                idx += 1
            curr_len = last - init + 1
            res.append(curr_len)
        return res
            



def get_last(idx, c, s):
    for i in range(len(s) - 1, idx, -1):
        if s[i] == c:
            return i
    return idx
        