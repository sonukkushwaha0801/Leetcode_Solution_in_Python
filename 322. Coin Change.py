# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import math
from sys import maxsize


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount==0:
            return 0
        n=len(coins)
        prev=[0]*(amount+1)
        for j in range(amount+1):
            if j%coins[0]==0:
                prev[j]=j//coins[0]
            else:
                prev[j]=maxsize
        for i in range(1,n):
            curr=[0]*(amount+1)
            for j in range(amount+1):
                not_pick=prev[j]
                pick=maxsize
                if coins[i]<=j:
                    pick=1+curr[j-coins[i]]
                curr[j]=min(pick,not_pick)
            prev=curr[:]
        ans=prev[amount]
        if ans>=maxsize:
            return -1
        return ans
    
# Another way:
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:        
        dp=[math.inf] * (amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1]==math.inf else dp[-1]
                