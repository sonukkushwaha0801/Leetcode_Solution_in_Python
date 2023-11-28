# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from math import prod
import re


class Solution:
    def numberOfWays(self, c: str) -> int:
        return prod(len(m.group(1))+1 for m in re.finditer(r'S(P*)S', c[c.find('S')+1:]))%(10**9+7) if (s:=c.count('S')) and s%2 == 0 else 0
    
# Another way:
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        seatsTotal = corridor.count('S')
        if seatsTotal == 0 or seatsTotal%2:
            return 0

        result = 1
        i = 0
        while i < len(corridor):
            seats = 0
            while i < len(corridor) and seats < 2:
                if corridor[i] == 'S':
                    seats += 1
                i += 1
            
            iPrev = i
            while i < len(corridor):
                if corridor[i] == 'S':
                    break
                i += 1
            
            if i < len(corridor) and i-iPrev:
                result *= i-iPrev+1
                result %= MOD

        return result