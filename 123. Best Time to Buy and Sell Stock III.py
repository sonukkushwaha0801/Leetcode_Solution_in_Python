# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        ahd=[[0]*3 for _ in range(2)]
        for i in range(n-1,-1,-1):
            curr=[[0]*3 for _ in range(2)] 
            for j in range(1,-1,-1):
                for k in range(1,3):
                    if j:
                        curr[j][k]=max(ahd[j][k],ahd[0][k]-prices[i])
                    else:
                        curr[j][k]=max(ahd[j][k],ahd[1][k-1]+prices[i])
            ahd=curr
        return ahd[1][2]

# Another way:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = buy2 = float("inf")
        profit1 = profit2 = 0
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
        
        return profit2