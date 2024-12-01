# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def checkIfExist(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num << 1 in seen:
                return True
            if not num & 1 and num >> 1 in seen:
                return True
            seen.add(num)
        return False
    
# Another way:
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set_nums = set()
        for nums in arr:
            if nums*2 in set_nums or (nums%2 == 0 and nums//2 in set_nums):
                return True
            set_nums.add(nums)   
        return False