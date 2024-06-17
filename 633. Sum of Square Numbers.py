# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from cmath import sqrt
from math import isqrt
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s, e = 0, int(math.sqrt(c))
        
        while s <= e:
            sum_of_squares = s * s + e * e
            if sum_of_squares == c:
                return True
            elif sum_of_squares > c:
                e -= 1
            else:
                s += 1
                
        return False
    
# Another way to solve:
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(sqrt(c-a*a)%1==0 for a in range(isqrt(c)+1))