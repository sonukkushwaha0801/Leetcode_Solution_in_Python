# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import bisect
from typing import List
from math import floor, sqrt

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        sum, cnt=0, 0
        for x in range(1, n+1):
            if x not in banned:
                sum+=x
                if sum>maxSum: break
                cnt+=1
        return cnt
    
# ANother way:
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = sorted(set(banned))
        i = -1
        j = 0
        while i != j:
            i = j
            x = min(n, floor((-1 + sqrt(1 + 8 * maxSum)) / 2))
            j = bisect.bisect(banned, x, lo=i)
            maxSum += sum(banned[i:j])
        return x - i