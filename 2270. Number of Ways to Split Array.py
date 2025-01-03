# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0]*(len(nums))
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        count = 0
        for i in range(len(nums)-1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                count += 1

        return count

        

# Another way:
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSideSum = 0
        rightSideSum = sum(nums)
        validSplits = 0
        
        for i in range(len(nums) - 1):
            leftSideSum += nums[i]
            rightSideSum -= nums[i]
            if leftSideSum >= rightSideSum:
                validSplits += 1
                
        return validSplits