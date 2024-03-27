# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        count = 0
        prod = 1
        left = 0
        for right, num in enumerate(nums):
            prod *= num  
            while prod >= k: 
                prod /= nums[left]
                left += 1
            count += right - left + 1  
        return count
        
# Another way:
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        ans = 0
        l,product = 0,1

        for r,num in enumerate(nums):
            product *=num
            while product>=k and l<=r:
                product//=nums[l]
                l+=1
            ans+=r-l+1
        return ans