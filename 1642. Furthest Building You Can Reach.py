# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import heapq


class Solution:
    
   def furthestBuilding(self, h: list[int], b: int, l: int) -> int:
       p = []
       
       i = 0
       for i in range(len(h) - 1):
           diff = h[i + 1] - h[i]
           
           if diff <= 0:
               continue
           
           b -= diff
           x = heapq.heappush(p, -diff)
           print(x)
           if b < 0:
               b += -heapq.heappop(p)
               l -= 1
               
           if l < 0:
               return i
       return len(h)-1
  
# Another way:
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i
        return len(heights) - 1