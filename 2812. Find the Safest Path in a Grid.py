# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import deque
import heapq
from itertools import product
from typing import List
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        A = [] # thieves
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    A.append([i, j])

        visited = [[0 for j in range(n)] for i in range(m)]
        distance = [[0 for j in range(n)] for i in range(m)]

        # find the minimum mahatten distance of each cell to theives 
        depth = 0
        while A:
            B = []
            for i, j in A:
                if not visited[i][j]:
                    visited[i][j] = 1
                    distance[i][j] = depth
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                        if 0 <= x < m and 0 <= y < n:
                            B.append([x, y])
            A = B
            depth += 1
            
        # start from 0,0 and use dijkstra  
        visited = [[0 for j in range(n)] for i in range(m)]
        pq = [[-distance[0][0], 0, 0]]
        while pq:
            dis, i, j = heapq.heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j] = 1
            if i == m - 1 and j == n - 1:
                return -dis

            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n:
                    heapq.heappush(pq, [-min(-dis, distance[x][y]), x, y])

        return -1
    
# Type two:
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)
        queue, safeness = deque(), [[-1] * n for _ in range(n)]
        unseen = set(product(range(n), range(n)))
        nei = lambda x,y: set(((x-1,y), (x,y-1), (x+1,y), (x,y+1))) & unseen
        
        for i, j in product(range(n),range(n)):
            if grid[i][j] == 1:
                safeness[i][j] = 0
                queue.append((0, i,j))
        
        while queue:
            
            s, x,y = queue.popleft()

            for X, Y in nei(x,y):
                if safeness[X][Y] == -1:
                    safeness[X][Y] = s + 1
                    queue.append((s+1, X,Y))

        heap = [(-safeness[-1][-1], n-1,n-1)]
        
        while heap:
            s ,x,y = heapq.heappop(heap)
            if (x,y) == (0,0): return min(-s,safeness[0][0])
            unseen.discard((x,y))

            for X, Y in nei(x,y):
                safe = max(s,-safeness[X][Y])
                heapq.heappush(heap,(safe, X,Y) )
                unseen.discard((X,Y))
            
        return -1