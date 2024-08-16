# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from functools import reduce
from math import inf
from typing import List


class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        return reduce(lambda q,b:(max(q[0],b[-1]-q[1],q[2]-b[0]),min(q[1],b[0]),max(q[2],b[-1])),a,(0,inf,-inf))[0]
    
# Another way:
class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        res, minn, maxx = 0, inf, -inf
        for b in a:
            res = max(res, b[-1] - minn, maxx - b[0])
            minn = min(minn, b[0])
            maxx = max(maxx, b[-1])
            
        return res