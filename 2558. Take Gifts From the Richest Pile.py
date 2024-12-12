# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        while k:
            current_gift = heapq.heappop(gifts) * -1
            left = math.floor(math.sqrt(current_gift))
            heapq.heappush(gifts, -left)
            k -= 1
        
        return (sum(gifts) * -1)
    
# Another way:


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -math.floor(largest ** 0.5))
        return -sum(max_heap)