# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from functools import reduce
from operator import or_
from typing import List

class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        O = reduce(or_, a) # Max OR

        def f(i, o):
            if i < len(a):
                return f(i+1, o) + f(i+1, o|a[i])
            
            return o == O

        return f(0, 0)
    
# Another way:
class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        res = 0
        for m in range(1, 1<<len(a)):
            res += reduce(or_, (v for i,v in enumerate(a) if 1<<i&m)) == reduce(or_,a)

        return res