# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from math import isqrt
from typing import List


class Solution:
    def longestSquareStreak(self, nums):
        mp = {}
        nums.sort()
        res = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1
                res = max(res, mp[num])
            else:
                mp[num] = 1

        return res
    
# Another way:
class Solution:
    def longestSquareStreak(self, a: List[int]) -> int:
        @cache
        def f(v):
            return 1 + (v*v in a and f(v*v))

        a = {*a}
        r = max(map(f, a))
        if r > 1:
            return r
        return -1