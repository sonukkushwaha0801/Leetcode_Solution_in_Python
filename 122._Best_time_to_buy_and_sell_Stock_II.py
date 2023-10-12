# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            profit += max((prices[i+1]-prices[i]), 0)

        return profit
    
# Similar way:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                maxprofit+=prices[i+1]-prices[i]
        return maxprofit