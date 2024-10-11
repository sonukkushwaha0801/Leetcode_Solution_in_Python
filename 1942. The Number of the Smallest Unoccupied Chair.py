# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from collections import *
from heapq import *
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = [(t[0], f) for f,t in enumerate(times)] + [(t[1], -f) for f,t in enumerate(times)]
        events.sort()
        available_seats = list(range(len(times)))
        # seat maps a friend to their seat number
        seat = dict()
        for t, f in events:
            f = abs(f)
            if f == targetFriend:
                return heappop(available_seats)
            if f in seat:
                heappush(available_seats, seat[f])
                del seat[f]
            else:
                seat[f] = heappop(available_seats) 
        
# Another way:
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_time = times[targetFriend]
        times.sort()

        n = len(times)
        chair_time = [0] * n

        for time in times:
            for i in range(n):
                if chair_time[i] <= time[0]:
                    chair_time[i] = time[1]
                    if time == target_time:
                        return i
                    break
        return 0