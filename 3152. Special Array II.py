# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from itertools import accumulate, pairwise
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pref = [*accumulate(pairwise(nums), lambda c, n: c+sum(n)%2, initial=0)]
        return [pref[b]-pref[a] == b-a for a, b in queries]
    
# Type two:
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pref, cnt = [0], 0
        for a, b in pairwise(nums):
            if (a + b) % 2 == 1:
                cnt += 1
            pref.append(cnt)
        ans = []
        for a, b in queries:
            ans.append(pref[b]-pref[a] == b-a)
        return ans