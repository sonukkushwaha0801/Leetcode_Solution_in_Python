# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = []

        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i]))
        
        workers.sort()

        max_heap = []
        total_quality = 0
        min_cost = float('inf')
        sum_quality = 0

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q
            sum_quality += q

            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)

        return min_cost
    
# Another way:
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])  # Sort by wage-to-quality ratio
        result = float('inf')
        quality_sum = 0
        heap = []  # Use a min heap to keep track of the highest quality workers

        for ratio, q in workers:
            quality_sum += q
            heapq.heappush(heap, -q)  # Push negative quality to get the maximum quality

            if len(heap) > k:
                quality_sum += heapq.heappop(heap)  # Remove the worker with the highest quality

            if len(heap) == k:
                result = min(result, ratio * quality_sum)

        return result