# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n!=0:
            cnt += (n % 2)
            n >>= 1
        return cnt
    
# Another way:
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()