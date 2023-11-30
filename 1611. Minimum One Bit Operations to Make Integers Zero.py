# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
from functools import cache


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        
        n = bin(n)[2:]
        
        @cache
        def zero(n):
            if '1' not in n:
                return 0
            elif n[0] == '0':
                return zero(n[1:])
            else:
                if n == '1': return 1
                new = '1' + '0' * (len(n) - 2)
                return 1 + zero(new) + ones(n[1:])
            
        @cache
        def ones(n):
            if n == '1' or n[0] == '1' and n.count('1') == 1:
                return 0
            elif n[0] == '1':
                return zero(n[1:])
            else:
                if n == '0': return 1
                new = '1' + '0' * (len(n) - 2)
                return 1 + zero(new) + ones(n[1:])
            
        return zero(n)
    
# Another solution:
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        f = 0
        
        for i in range(31, -1, -1):
            if ((n >> i) & 1) == 1:
                if f == 0:
                    ans = ans + ((1 << (i + 1))) - 1
                    f = 1
                else:
                    ans = ans - ((1 << (i + 1)) - 1)
                    f = 0
        
        return ans

