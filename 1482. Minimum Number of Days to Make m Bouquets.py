# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

from bisect import bisect_left
from itertools import groupby
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets >= m:
                            return True
                else:
                    flowers = 0
            return bouquets >= m
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
# Another way:
class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        def f(d):
            return sum(v*sum(1 for _ in p)//k for v,p in groupby(b, lambda q: d >= q)) >= m

        return k*m <= len(b) and bisect_left(range(max(b)), 1, key=f) or -1