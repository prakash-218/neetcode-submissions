import heapq

class Wrapper:
    def __init__(self, number, freq):
        self.num = number
        self.freq = freq
    
    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        h = []
        for i in nums:
            d[i]  = d.get(i, 0) + 1
        
        for i in d:
            heapq.heappush(h, Wrapper(i, d[i]))
            if len(h) > k:
                heapq.heappop(h)
        
        for i in range(len(h)):
            h[i] = h[i].num
        return h