from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for stone in stones:
            heappush(arr, -stone)
        while len(arr) > 1:
            x = - heappop(arr)
            y = - heappop(arr)

            if x != y:
                new = x - y
                heappush(arr, - new)




        return - arr[0] if arr else 0
        