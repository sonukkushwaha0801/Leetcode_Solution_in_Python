# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from itertools import chain, count
from operator import mul
from typing import Counter, List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        COUNT = [0] * n 
        for A,B in roads:
            COUNT[A] += 1 
            COUNT[B] += 1
        COUNT.sort()
        sum_of = 0
        for i in range(len(COUNT)):
            sum_of += COUNT[i] * (i+1)
        
        return sum_of

# Another way:    
class Solution:
    def maximumImportance(self, n: int, r: List[List[int]]) -> int:
        return -sum(map(mul,count(-n),sorted(Counter(chain(*r)).values())[::-1]))
