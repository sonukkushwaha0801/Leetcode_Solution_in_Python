# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        prev2=cost[0]
        prev1=cost[1]
        for i in range(2,n):
            temp=cost[i]+min(prev1,prev2)
            prev2=prev1
            prev1=temp
        return min(prev1,prev2)    
        

# Another Way:
class Solution:
    def minCostClimbingStairs(self, cost):
        sz = len(cost)
        minCost = [0] * sz
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        for indx in range(2, sz):
            minCost[indx] = cost[indx] + min(minCost[indx - 1], minCost[indx - 2])
        return min(minCost[sz - 2], minCost[sz - 1])