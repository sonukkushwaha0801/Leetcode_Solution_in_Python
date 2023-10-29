# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
import math
class Solution:
    def poorPigs(self, B: int, Die: int, Test: int) -> int:
        x = Test//Die
        x = x+1
        v = math.log2(B)/math.log2(x)
        return math.ceil(v)
        
# Another way:
from asyncio import log
from cmath import isclose
class Solution:
    def poorPigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
        pigs = log(buckets, minutes_to_test // minutes_to_die + 1)
        return round(pigs) if isclose(pigs, round(pigs)) else math.ceil(pigs)
