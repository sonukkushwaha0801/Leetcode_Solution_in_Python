# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        n=len(nums)
        n1=0
        n0=0
        maxLen=0
        mp={}
        mp[0]=-1
        for i in range(n):
            n1+=nums[i]
            n0=(i+1)-n1
            if (n1-n0) in mp:
                maxLen=max(maxLen, i-mp[n1-n0])
            else:
                mp[n1-n0]=i
        return maxLen
        
# Another way:
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        
        ones = 0
        zeros = 0
        res = 0
        diff = {} 

        for i, n in enumerate(nums):
            if n == 1:
                ones += 1
            else:
                zeros += 1
            
            if ones - zeros not in diff:
                diff[ones - zeros] = i
            
            if ones == zeros:
                res = ones + zeros
            else:
                idx = diff[ones - zeros]
                res = max(res, i - idx)
        
        return res