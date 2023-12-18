# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        return (X:=sorted(nums))[-1]*X[-2]-X[1]*X[0]
    
# Another way:
class Solution:
    def maxProductDifference(self, nums):
        nums.sort()
        n1 = nums[-1] * nums[-2]
        n2 = nums[0] * nums[1]
        return n1 - n2