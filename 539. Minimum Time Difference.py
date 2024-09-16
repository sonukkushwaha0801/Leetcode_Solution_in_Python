# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/

from operator import sub
from typing import List
#type first:

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        times = []
        for time in timePoints:
            hours, minutes = map(int, time.split(':'))
            times.append(hours * 60 + minutes)
        
        times.sort()
        
        min_diff = float('inf')

        for i in range(len(times) - 1):
            min_diff = min(min_diff, times[i + 1] - times[i])
        
        min_diff = min(min_diff, 1440 + times[0] - times[-1])
        
        return min_diff

# one Liner: 
class Solution:
    def findMinDifference(self, a: List[str]) -> int:
        return min(map(sub,(q:=sorted(int(s[:2])*60+int(s[3:]) for s in a))[1:]+[q[0]+1440],q))


# Another way:
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        minutes = [timeToMinutes(tp) for tp in timePoints]
        
        minutes.sort()
        
        min_diff = float('inf') 
        
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        circular_diff = 1440 - minutes[-1] + minutes[0]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff