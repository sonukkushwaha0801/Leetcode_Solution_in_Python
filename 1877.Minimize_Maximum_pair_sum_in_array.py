#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        return nums.sort() or max(nums[i]+nums[-1-i] for i in range((len(nums)>>1)+1))

# Another way:
class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return max([x+y for x,y in zip(nums[:len(nums)//2],nums[len(nums)//2:][::-1])])
        