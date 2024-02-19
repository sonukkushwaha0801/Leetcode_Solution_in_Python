# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         return n > 0 and (n & (n - 1)) == 0

# Another way:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1