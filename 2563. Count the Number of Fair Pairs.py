# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List
from bisect import bisect, bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 1):
            # Find the range of valid j values for each i
            left_bound = bisect_left(nums, lower - nums[i], i + 1, n)
            right_bound = bisect_right(nums, upper - nums[i], i + 1, n) - 1
            
            # Count all valid pairs in the range [left_bound, right_bound]
            if left_bound <= right_bound:
                count += right_bound - left_bound + 1
                
        return count
        
# Another way:
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 1):
            min_val = lower - nums[i]
            max_val = upper - nums[i]   
            start = bisect.bisect_left(nums, min_val, i + 1, n)
            end = bisect.bisect_right(nums, max_val, i + 1, n) - 1   
            if start <= end:
                count += end - start + 1
        return count