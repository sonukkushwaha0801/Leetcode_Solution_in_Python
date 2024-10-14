# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from heapq import heapify, heappushpop, heapreplace
from operator import neg
from typing import List


class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        return heapify(h:=[*map(neg,a)]) or -sum(heappushpop(h,h[0]//3) for _ in range(k))
    
# Another way:
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range( len( nums ) ):
            nums[i] = -nums[i]
        heapify( nums )
        score = 0
        for i in range( k ):
            score -= nums[0]
            heapreplace( nums, -( (2-nums[0]) // 3 ) )
        return( score )