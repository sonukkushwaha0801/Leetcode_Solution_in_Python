# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
# Second way:
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)
    
# Third way:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last