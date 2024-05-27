# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for x in range(n + 1):
            count = sum(1 for num in nums if num >= x)
            
            if count == x:
                return x
        
        return -1
    
# Another way:
class Solution:
    def specialArray(self, a: List[int]) -> int:
        return next((x for x in range(len(a)+1) if sum(v>=x for v in a)==x),-1)