# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter, List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return True if sorted(list(target)) == sorted(list(arr)) else False
    
# Another way:
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)