# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from bisect import bisect_left
from typing import List


class Solution:
    def fn(self, p, m, mid):
        cnt = 1
        prev = p[0]
        for i in range(1, len(p)):
            if p[i] - prev >= mid:
                cnt += 1
                prev = p[i]
        return cnt >= m

    def maxDistance(self, p, m):
        p.sort()
        lo = 1
        hi = p[-1] - p[0]
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.fn(p, m, mid):
                lo = mid
            else:
                hi = mid - 1
        if self.fn(p, m, hi):
            return hi
        return lo
    
# Another way:
class Solution:
    def maxDistance(self, P: List[int], balls: int) -> int:
        P.sort()

        def count(d):
            n = 1
            x = P[0]
            for y in P:
                if y - x > d:
                    x = y
                    n += 1
            return n

        return bisect_left(range(P[-1] - P[0]), True, key=lambda d: count(d) < balls)