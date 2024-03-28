# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = {}
        l = 0
        n = len(nums)
        for r in range(n):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            if mp[nums[r]] > k:
                while nums[l] != nums[r]:
                    mp[nums[l]] -= 1
                    l += 1
                mp[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
    
# Another way:
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        res = 0
        M = {}
        
        for i in range(n):
            M[nums[i]] = M.get(nums[i], 0) + 1
            
            while M[nums[i]] > k:
                M[nums[j]] -= 1
                j += 1
            
            res = max(res, i - j + 1)
        
        return res