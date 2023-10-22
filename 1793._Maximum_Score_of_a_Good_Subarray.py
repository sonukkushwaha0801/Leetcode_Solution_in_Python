# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        res=nums[k]
        i=k
        j=k
        min_val=nums[k]

        while i>0 or j<len(nums)-1:
            if i==0:
                j+=1
                min_val=min(min_val,nums[j])
            elif j==len(nums)-1:
                i-=1
                min_val=min(min_val,nums[i])
            elif nums[i-1]>nums[j+1]:
                i-=1
                min_val=min(min_val,nums[i])
            else:
                j+=1
                min_val=min(min_val,nums[j])
            res=max(res,min_val*(j-i+1))
        return res

#Another way:
class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        l, r = k, k
        cur_min = nums[k]
        ans = float('-inf')
        while l >= 0 or r < len(nums):
            while l >= 0 and nums[l] >= cur_min:
                l -= 1
            while r < len(nums) and nums[r] >= cur_min:
                r += 1
            ans = max(ans, (r - l - 1) * cur_min)
            if l >= 0 and r < len(nums):
                cur_min = max(nums[l], nums[r])
            elif l >= 0:
                cur_min = nums[l]
            elif r < len(nums):
                cur_min = nums[r]
            else:
                break 
        return ans
        