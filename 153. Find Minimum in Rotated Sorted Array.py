# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findMin(self, nums: list[int]) -> int:
        ans = nums[0]
        low, high = 0, len(nums) - 1

        if nums[low] < nums[high]:
            return nums[low]

        while low <= high:
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            
            mid = (low + high) // 2
            ans = min(ans, nums[mid])

            
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return ans
    
# Another way:
import math
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1 or nums[0]<nums[len(nums)-1]:
            return nums[0]
        low=0
        high=len(nums) - 1
        while low<high:
            mid=low+(high-low)//2
            if nums[mid]<nums[low]:
                low=mid
            if nums[mid]>nums[high]:
                high=mid
        return nums(low+1)