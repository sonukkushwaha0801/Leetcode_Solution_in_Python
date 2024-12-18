# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stact, ans = [], [0] * n

        for i in range(n):
            while stact and prices[stact[-1]] >= prices[i]:
                ans[stact[-1]] = prices[stact[-1]] - prices[i]
                stact.pop()
            stact.append(i)
            
        for idx in stact:
            ans[idx] = prices[idx]
        
        return ans

# Another way:
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i , price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()]-= price
            stack.append(i)
        return prices