# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


from itertools import accumulate
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        
        return False
    
# Another implementation:
class Solution:
    def checkSubarraySum(self, a: List[int], k: int) -> bool:
        d = {0:-1}
        for i,p in enumerate(accumulate(a)):
            q = p%k
            if q in d:
                if i - d[q] > 1:
                    return True
            else:
                d[q] = i
        
        return False