# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')
        n = n.zfill(32)

        return int(n[::-1], 2)

# Another way:
class Solution:
    def reverseBits(self, n: int) -> int:
        def f(n,r,count):
            if n<1:
                return r<<(32-count)
            return f(n>>1,(r<<1)|(n&1),count+1)
        return f(n,0,0)