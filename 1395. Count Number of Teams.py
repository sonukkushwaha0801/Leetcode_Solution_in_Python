# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
import bisect
from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            leftLess = leftGreater = rightLess = rightGreater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    leftLess += 1
                elif rating[i] > rating[j]:
                    leftGreater += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    rightLess += 1
                elif rating[k] > rating[j]:
                    rightGreater += 1
            
            count += leftLess * rightGreater + leftGreater * rightLess
        
        return count
    
# Another way:
from sortedcontainers import SortedList

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sl1 = SortedList()
        sl2 = SortedList(rating)
        res = 0
        for j in range(len(rating)):
            sl2.remove(rating[j])
            sl1Index = bisect.bisect(sl1, rating[j])
            sl2Index = bisect.bisect(sl2, rating[j])
            res += sl1Index * (len(sl2) - sl2Index)
            res += (len(sl1) - sl1Index) * sl2Index
            sl1.add(rating[j])
        return res