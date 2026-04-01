class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        for i in stones:
            heapq.heappush(res, -1 * i)
        while len(res) > 1:
            first = heapq.heappop(res) * -1
            second = heapq.heappop(res) * -1
            if first > second:
                heapq.heappush(res, -1 * (first - second))
            elif second > first:
                heapq.heappush(res, -1 * (second - first))
        if len(res) == 1:
            return res[0] * -1
        return 0
        