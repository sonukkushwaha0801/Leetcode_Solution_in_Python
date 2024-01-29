# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.lo = []  
        self.hi = []  

    def addNum(self, num):
        heappush(self.lo, -num)
        heappush(self.hi, -self.lo[0])
        heappop(self.lo)
        
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)
            
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]                  
        else:
            return (self.hi[0] - self.lo[0]) / 2
        
# Another way:
from heapq import *
class MedianFinder:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        while len(self.maxheap) - len(self.minheap) > 1:
            heappush(self.minheap, -heappop(self.maxheap))
        while len(self.maxheap) - len(self.minheap) < -1:
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        diff = len(self.maxheap) - len(self.minheap)
        if diff == 1:
            return -self.maxheap[0]
        elif diff == -1:
            return self.minheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2
