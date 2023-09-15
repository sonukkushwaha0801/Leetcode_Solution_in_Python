# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      nums[:] = [x for x in nums if x != val]
      return len(nums)

# Second Type:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      index = 0
      for i in range(len(nums)):
          if nums[i] != val:
              nums[index] = nums[i]
              index += 1
      return index