# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from math import floor


def inverts(st):
        l=[s for s in st]
        for i in range(len(l)):
            if l[i]=='1':
                l[i]='0'
            elif l[i]=='0':
                l[i]='1'
        return ''.join(l)
class Solution:
    


    def findKthBit(self, n: int, k: int) -> str:
        a=['0']*n
        
        for i in range(1,n):
           a[i] =a[i-1]+ '1' + inverts(a[i-1])[::-1]
            
        b=a[n-1]
        return b[k-1]

        
# Another way:
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def f(n,k):
            m = floor((2**(n-1) + 0.5))
            if n == 1 and k == 1:
                return 0
            elif n != 1 and k == m:
                return 1
            elif k < m:
                return f(n-1,k)
            elif k > m:
                return not f(n,m - abs(m-k))
        return str(int(f(n,k)))