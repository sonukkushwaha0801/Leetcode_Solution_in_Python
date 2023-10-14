# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:



class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n=len(cost)
        dp =  [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(n, 0, -1): dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])
        return dp[n]
    
# Another way:
from functools import cache
class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n=len(cost)
        @cache
        def f(i, walls):
            if walls>=n: return 0
            if i>=n: 
                return 2**31+1
            ans=cost[i]+f(i+1, walls+1+time[i])
            ans=min(ans, f(i+1, walls))          
            return ans
        return f(0, 0)