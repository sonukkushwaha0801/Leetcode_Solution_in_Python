# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import math
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        return min(
            nums[-1] - nums[3],
            nums[-2] - nums[2],
            nums[-3] - nums[1],
            nums[-4] - nums[0])
    
# Another way:
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        k = 3  
        if len(nums) <= k + 1:
            return 0

        res, _ = math.inf, nums.sort()
        for (a, b) in [(k - i, -(1 + i)) for i in range(k + 1)]:
            res = min(res, nums[b] - nums[a])

        return res