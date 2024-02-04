# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while (right > left):
            right = right & (right - 1)
        return right & left
    
# Another way:
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift