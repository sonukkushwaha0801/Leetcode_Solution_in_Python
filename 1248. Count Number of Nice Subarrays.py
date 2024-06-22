# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        count=0
        ans=0
        for j in range(n):
            if nums[j] & 1:
                k-=1
                count=0
            while k==0:
                k+= nums[i] & 1
                i+=1
                count+=1
            ans+=count
        return ans            

# Another way:
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_counts = [1 if num % 2 != 0 else 0 for num in nums]
        
        prefix_sum = 0
        prefix_count = {0: 1}  
        nice_subarrays = 0
        
        for count in odd_counts:
            prefix_sum += count
            
            if prefix_sum - k in prefix_count:
                nice_subarrays += prefix_count[prefix_sum - k]
            
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1
        
        return nice_subarrays