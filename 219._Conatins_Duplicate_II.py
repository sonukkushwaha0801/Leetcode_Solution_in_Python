# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_indices = {} 

        for i in range(len(nums)):
            num = nums[i]
            if num in num_indices and i - num_indices[num] <= k:
                return True
            num_indices[num] = i
        return False
            
# Another way:
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_indices = {} 

        for i, num in enumerate(nums):
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True
            num_indices[num] = i

        return False