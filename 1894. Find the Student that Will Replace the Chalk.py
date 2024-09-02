# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        rem = k % total
        for i, value in enumerate(chalk):
            rem -= value
            if rem < 0:
                return i
        return -1 
    
# Another way:
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        ans = k % sum(chalk) 
        for i in range(len(chalk)):
            ans -= chalk[i]
            if ans < 0:
                return i
            