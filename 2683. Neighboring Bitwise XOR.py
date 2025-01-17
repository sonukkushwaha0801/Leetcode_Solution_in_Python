# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum=0
        for i in derived:
            xor_sum^=i
        return xor_sum==0
    
# Another way:

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return derived.count(1) % 2 == 0