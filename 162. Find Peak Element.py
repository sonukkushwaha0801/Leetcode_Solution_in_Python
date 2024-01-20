# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                high=mid-1
            elif mid<len(nums)-1 and nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                return mid

# Another way:
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        while left<=right:
            mid=(left+right)>>1
            if (mid==0 or nums[mid]>=nums[mid-1] ) and (mid==len(nums)-1 or nums[mid]>=nums[mid+1]) :
                return mid
            elif nums[mid]<=nums[mid+1]:
                left=mid+1
            else:
                right=mid-1
        return -1