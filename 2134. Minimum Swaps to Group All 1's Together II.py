
# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        
        # Edge cases
        if total_ones == 0 or total_ones == n:
            return 0
        
        current_ones = sum(nums[:total_ones])
        max_ones = current_ones
        
        # Use two pointers to slide the window
        for i in range(n):
            current_ones -= nums[i]
            current_ones += nums[(i + total_ones) % n]
            max_ones = max(max_ones, current_ones)
        
        return total_ones - max_ones
    
# Another way:
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        windows_size = sum(nums)
        result = current_zero = windows_size - sum(nums[:windows_size])
        for i in range(n):
            if nums[(i + windows_size) %  n] == 0:
                current_zero += 1
            if nums[i] == 0:
                current_zero -= 1
            result = min(result, current_zero)
        return result
             