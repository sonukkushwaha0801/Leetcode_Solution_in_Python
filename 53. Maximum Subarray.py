# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maximumSum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            maximumSum = max(maximumSum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return maximumSum

# Another way:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0 
        maxi = -10001
        
        for i in range(len(nums)):
            s += nums[i]
            if s > maxi: maxi = s
            if s < 0:
                s = 0
        return maxi