# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/

# Solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        mid=(len(nums))//2
        return nums[mid]