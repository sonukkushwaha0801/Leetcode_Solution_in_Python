# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def minimizeXor(self, v: int, u: int) -> int:
        return int((bin(v)[:1:-1]+'0'*32).replace(*'10'[::2*((d:=v.bit_count()-u.bit_count())>0)-1],abs(d))[::-1],2)
    
class Solution:
    def minimizeXor(self, v: int, u: int) -> int:
        p, q = v.bit_count(), u.bit_count()
        if p > q:
            return int(bin(v)[:1:-1].replace('1','0',p-q)[::-1], 2)

        return int((bin(v)[:1:-1]+'0'*32).replace('0','1',q-p)[::-1], 2)