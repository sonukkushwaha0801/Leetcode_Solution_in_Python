# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import groupby
import itertools
class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum(
            x * (x + 1) >> 1
            for _, grp in groupby(s)
            for x in [len(list(grp))]
        ) % (10**9 + 7)
    
# Another way:
class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum((l:=len(list(g))) * (l+1) // 2 for _, g in itertools.groupby(s)) % (10 ** 9 + 7)
    
# Additional way:
class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        for i, j in itertools.groupby(s):
            temp = len(list(j))
            count += (temp * (temp + 1)) // 2

        return count % (10 ** 9 + 7)