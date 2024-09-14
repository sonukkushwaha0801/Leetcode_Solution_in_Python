# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :

from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0
        
        return longest
    
# Another way:
class Solution:
    def longestSubarray(self, nums):
        max_val = max(nums)
        max_len = curr_len = 0

        for num in nums:
            if num == max_val:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0

        return max_len