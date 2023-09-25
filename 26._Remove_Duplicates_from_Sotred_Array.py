# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

# Second Way:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]]
        return len(nums)
    
#Third Way:
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
        return left + 1