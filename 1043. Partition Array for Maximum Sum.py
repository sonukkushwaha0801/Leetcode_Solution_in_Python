# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from functools import cache


class Solution:
    def maxSumAfterPartitioning(self, a: list[int], k: int) -> int:
        return (f:=cache(lambda i,m,l:max((m:=max(m,a[i]))*(l:=l+1)+f(i+1,0,0),(l<k)*f(i+1,m,l)) if i-len(a) else m*l))(0,0,0)

# Another way:
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            currMax = 0
            end = min(n,i+k)

            for j in range(i,end):
                currMax = max(currMax,arr[j])
                dp[i] = max(dp[i],dp[j+1]+currMax*(j-i+1))

        return dp[0]
        