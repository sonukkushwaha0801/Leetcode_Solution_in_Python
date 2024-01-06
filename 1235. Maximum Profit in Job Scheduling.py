# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from bisect import bisect_left, bisect_right


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        ind = 0
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            startTime[ind] = s
            endTime[ind]   = e
            profit[ind]    = p
            ind += 1
        
        dp = [profit[0]] + ([0] * ((n := len(profit))-1))

        for i in range(1, n):

            index = bisect_right(endTime, startTime[i]) - 1
            dp[i] = max(dp[i - 1], (dp[index] if index >= 0 else 0) + profit[i])

        return dp[-1]

#Another way:
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        
        dp = [[0,0]]                                           
        f = lambda x: dp[bisect_left(dp,[x+1])-1][1]            
        for e, s, p in sorted(zip(endTime,startTime, profit)):  
                                                                
            dp.append([e, max(f(e),p+f(s))])   
        return dp[-1][1]                                                                                                  