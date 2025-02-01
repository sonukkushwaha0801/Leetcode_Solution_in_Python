# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1]%2==nums[i]%2:
                return False
        
        return True