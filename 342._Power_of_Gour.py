# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 and (n & (n - 1)) == 0:
            zero_count = 0
            while n > 1:
                zero_count += 1
                n >>= 1
            return zero_count % 2 == 0
        return False
    
#Another way:

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
    
# One more way:

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1