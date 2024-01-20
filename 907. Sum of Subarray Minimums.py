# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import takewhile
from operator import itemgetter


class Solution:
    def sumSubarrayMins(self, a: list[int]) -> int:
        return (s:=[]) or sum(s.append((v,c:=1+sum(map(itemgetter(1),takewhile(lambda q:q[0]>v and s.pop(),s[::-1]))),S:=(s[-1][2] if s else 0) + v*c)) or S for v in a)%(10**9+7)

# Another way:
from sortedcontainers import SortedList

class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        sl = SortedList([-1, n])
        x_i = sorted((x, i) for i, x in enumerate(arr))
        ans = 0
        for x, i in x_i:
            index = sl.bisect(i)
            r = sl[index]
            l = sl[index - 1]
            ans += (i - l) * (r - i) * x
            ans %= mod
            sl.add(i)
        return ans