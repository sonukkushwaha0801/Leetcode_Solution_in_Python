# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ans=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[ans-2]:nums[ans]=nums[i];ans+=1
        return ans

# Another way:
class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for i in nums:
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k      