# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from math import inf
from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        changes = 0
        min_sacrifice = inf
        final = 0

        for val in nums:
            tmp = val ^ k
            if tmp > val:
                changes += 1
                final += tmp
                min_sacrifice = min(min_sacrifice, tmp - val)
            else:
                final += val
                min_sacrifice = min(min_sacrifice, val - tmp)

        if changes % 2:
            final -= min_sacrifice

        return final
    
# Another way:
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sum_ = 0
        min_extra = 1000000
        count = 0

        for val in nums:
            if (val ^ k) > val:
                sum_ += val ^ k
                min_extra = min(min_extra, (val ^ k) - val)
                count += 1
            else:
                sum_ += val
                min_extra = min(min_extra, val - (val ^ k))

        if count % 2 == 0:
            return sum_
        else:
            return sum_ - min_extra