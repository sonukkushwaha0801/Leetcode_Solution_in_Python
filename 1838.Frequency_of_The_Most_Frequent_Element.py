#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        sum_s_w = nums[0]
        fin = 1
        i=0
        for j in range(1,n):
            sum_s_w+=nums[j]
            mx = nums[j]
            while sum_s_w+k<mx*(j-i+1):
                sum_s_w -= nums[i]
                i += 1
            fin = max(fin,j-i+1)
        return fin
    
# Another way:
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l,r = 0,0
        res,total = 0,0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l+=1
            
            res = max(res,r-l+1)
            r+=1

        return res