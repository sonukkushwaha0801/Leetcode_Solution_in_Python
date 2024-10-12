# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for interval in intervals:
            left, right = interval
            events.append((left, 1))
            events.append((right + 1, -1))
        events.sort()
        
        max_groups = 0
        current_groups = 0
        for _, event in events:
            current_groups += event
            max_groups = max(max_groups, current_groups)
        
        return max_groups
    
# Another way:
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ok = []

        for i,j  in intervals:
            if ok and ok[0] < i:
                heappop(ok)
            heappush(ok,j)
        
        a = len(ok)
        return a