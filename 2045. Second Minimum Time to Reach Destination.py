# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import deque
import heapq
from typing import List


class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0
        while q:
            x, freq = q.popleft()
            t = dist1[x] if freq == 1 else dist2[x]
            if (t // change) % 2:
                t = change * (t // change + 1) + time
            else:
                t += time
            for y in g[x]:
                if dist1[y] == -1:
                    dist1[y] = t
                    q.append((y, 1))
                elif dist2[y] == -1 and dist1[y] != t:
                    if y == n:
                        return t
                    dist2[y] = t
                    q.append((y, 2))
        return 0
    
# Another way:
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        d = [[float("inf"), float("inf")] for _ in range(n + 1)]
        pq = [(0, 1)]
        while pq:
            t1, u1 = heapq.heappop(pq)
            if u1 == n and d[u1][1] != float("inf"): return d[u1][1]
            t = time
            if (t1 // change) % 2 == 1: t += (t1 // change + 1) * change - t1
            for u2 in g[u1]:
                if t1 + t < d[u2][0]:
                    d[u2][0], d[u2][1] = t1 + t, d[u2][0]
                    heapq.heappush(pq, (t1 + t, u2))
                if d[u2][0] < t1 + t < d[u2][1]:
                    d[u2][1] = t1 + t
                    heapq.heappush(pq, (t1 + t, u2))

        return -1