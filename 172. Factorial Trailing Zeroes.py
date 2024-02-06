# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def trailingZeroes(self, n):
        x   = 5
        res = 0
        while x <= n:
            print(n//x)
            res += n//x
            x   *= 5
        return res

# Another way:
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n >= 5:
            n //= 5
            zero_count += n
        return zero_count