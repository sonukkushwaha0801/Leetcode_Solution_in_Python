# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from itertools import accumulate


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diff = list(accumulate([g - c for g,c in zip(gas,cost)], initial = 0))
        return diff.index(min(diff)) if diff[-1] >= 0 else -1

# Type two:
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int: 
        if sum(gas) < sum(cost): return -1                                        
        tank = idx = 0                                                              
        for i in range(len(gas)):                                             
            tank+= gas[i]-cost[i]             
            if tank < 0: tank, idx = 0, i+1                                    
        return idx                           
                                