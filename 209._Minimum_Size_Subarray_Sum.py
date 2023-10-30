# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target: return 0
        s, l, ans = 0, 0, len(nums)
        for r,val in enumerate(nums):
            s+= val
            while s >= target:
                s-= nums[l]  
                ans = min(ans, r - l + 1)
                l+= 1
        return ans                                    
    
# Another way:
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        end = 0
        sm = nums[start]
        minlen = len(nums)
        totSum = 0

        while(start<=end and end<len(nums)):
            
            if nums[end]>=target:
                return 1
            if sm>=target:
                
                diff = end-start+1
                if diff<=minlen:
                    minlen = diff
                    totSum = sm
                sm = sm - nums[start]
                start = start+1
            else:
                end = end + 1
                if end<len(nums):
                    sm = sm + nums[end]
                    
        if minlen==len(nums):
            if totSum==0:
                return 0
        return minlen
        