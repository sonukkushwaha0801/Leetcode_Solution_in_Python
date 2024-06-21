# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        total = sum((1 - grumpy[i]) * customers[i] for i in range(len(customers)))

        window_all = 0
        window_partial = 0
        for i in range(len(customers)):
            window_all += customers[i]
            window_partial += (1 - grumpy[i]) * customers[i]
            if i + 1 >= minutes:
                ans = max(ans, total - window_partial + window_all)
                left = i - minutes + 1
                window_all -= customers[left]
                window_partial -= (1 - grumpy[left]) * customers[left]

        return ans
    
# Another way to solve the problem:
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        totalsat = 0

        for i, j in zip(grumpy, customers):
            if(i==0):
                totalsat+=j

        maxsat = 0

        for i in range(len(grumpy)-minutes+1):
            sat = totalsat
            for j in range(i, i+minutes):
                if(grumpy[j]==1):
                    sat+=customers[j]
            if(sat>maxsat):
                maxsat = sat


        return maxsat