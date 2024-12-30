# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from functools import cache


class Solution:
    def countGoodStrings(self, l: int, h: int, z: int, o: int) -> int:
        return (f:=cache(lambda i:i<=h and ((i>=l)+f(i+z)+f(i+o))%(10**9+7)))(0)
    
# Another way:
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        def rec(length):
            if length > high:
                return 0
            if length in memo:
                return memo[length]
            count = 1 if low <= length <= high else 0
            count += rec(length + zero) % MOD
            count += rec(length + one) % MOD
            count %= MOD
    
            memo[length] = count
            return count
        return rec(0)