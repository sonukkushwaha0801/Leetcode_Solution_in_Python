# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money if money<(x:=sum(heapq.nsmallest(2,prices))) else money-x
        

# Another way:

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money if money<(x:=sum(sorted(prices)[:2])) else money-x