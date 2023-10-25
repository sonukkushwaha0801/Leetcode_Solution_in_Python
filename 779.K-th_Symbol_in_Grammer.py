# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length = 2 ** (n - 2)
        if k <= length:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - length)

# Another way:
import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def f(k):
            if k==1: return 0
            b=(int)(math.log2(k)) # same as b=k.bit_length()-1
            if k==1<<b: return b%2
            else: return 1-f(k-(1<<b))
        return f(k)
        