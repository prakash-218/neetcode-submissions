from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heappush(self.right, num)
        else:
            heappush(self.left, -1 * num)
        
        if len(self.right) > len(self.left) + 1:
            heappush(self.left, -1 * heappop(self.right))
        elif len(self.left) > len(self.right) + 1:
            heappush(self.right, -1 * heappop(self.left))
        

    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        elif len(self.left) > len(self.right):
            return -1 * self.left[0]
        
        return (-1 * self.left[0] + self.right[0]) / 2
        
        