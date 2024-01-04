# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter
from math import ceil


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        from collections import Counter
        mp = Counter(nums)
        
        count = 0
        for t in mp.values():
            if t == 1:
                return -1
            count += t // 3
            if t % 3:
                count += 1
                
        return count

# Another way:
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return -1 if 1 in (v:=Counter(nums).values()) else sum(ceil(f/3) for f in v)