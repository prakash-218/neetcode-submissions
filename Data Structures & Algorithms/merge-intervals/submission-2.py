class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        idx = 0
        res = []
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        newStart = currStart
        newEnd = currEnd
        for i in range(1, len(intervals)):
            newStart = intervals[i][0]
            newEnd = intervals[i][1]
            if currEnd >= newStart:
                currEnd = max(newEnd, currEnd)
            else:
                res.append([currStart, currEnd])
                currStart = newStart
                currEnd = newEnd
        res.append([currStart, currEnd])
        return res
