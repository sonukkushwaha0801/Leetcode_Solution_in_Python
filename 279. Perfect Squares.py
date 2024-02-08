# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from functools import reduce
import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=i
            for j in range(1,int(math.sqrt(i))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[n]

# Another way:
class Solution:
    def numSquares(self, n: int) -> int:
        return reduce(lambda a,k:a+[1+min(a[k-q*q] for q in range(1,math.isqrt(k)+1))],range(1,n+1),[0])[-1]