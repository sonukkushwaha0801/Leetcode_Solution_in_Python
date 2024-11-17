# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from cmath import inf
from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        min_length = float('inf')

        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return min_length if min_length != float('inf') else -1
    
# Another way:
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf 
        queue = deque([(-1, 0)])
        prefix = 0
        for i, x in enumerate(nums): 
            prefix += x
            while queue and prefix - queue[0][1] >= k: ans = min(ans, i - queue.popleft()[0])
            while queue and queue[-1][1] >= prefix: queue.pop()
            queue.append((i, prefix))
        return ans if ans < inf else -1 