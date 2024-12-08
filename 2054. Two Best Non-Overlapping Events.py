# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

import bisect
import heapq
from itertools import accumulate

class Solution:
    def maxTwoEvents(self, events):
        events.sort()
        pq = []
        max_val = 0
        ans = 0

        for start, end, value in events:
            while pq and pq[0][0] < start:
                max_val = max(max_val, heapq.heappop(pq)[1])
            ans = max(ans, max_val + value)
            heapq.heappush(pq, (end, value))

        return ans
    
# Another way:
class Solution:
    def maxTwoEvents(self, events):
        ev = sorted([e, v] for s, e, v in events)
        dp = list(accumulate((v for _, v in ev), func=max, initial=0))
        return max(dp[bisect.bisect_right(ev, [s, 0])] + v for s, _, v in events)