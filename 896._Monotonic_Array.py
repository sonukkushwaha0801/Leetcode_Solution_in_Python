# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_increasing = True 
        is_decreasing = True
        for i in range(1, len(nums)):
            print(nums[i],nums[i-1])
            if nums[i] < nums[i - 1]:
                is_increasing = False
            elif nums[i] > nums[i - 1]:
                is_decreasing = False
            if not is_increasing and not is_decreasing:
                break

        return is_increasing or is_decreasing 

# TYpe 2:

class Solution:
    def isMonotonic(self, A: list[int]) -> bool:
        return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))