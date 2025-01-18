# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0, 0)]) 
        
        while queue:
            r, c, cost = queue.popleft()
            
            if visited[r][c]:
                continue
            visited[r][c] = True
            
            if (r, c) == (m - 1, n - 1):
                return cost

            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if grid[r][c] == i + 1:  
                        queue.appendleft((nr, nc, cost))
                    else:
                        queue.append((nr, nc, cost + 1))
        
        return -1 
    
# Another way:
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def inBounds(r, c, cost):
            return r >= 0 and r < n and c >= 0 and c < m and cost < visited.get((r, c), float("inf"))
            


        n, m = len(grid), len(grid[0])
        moves = {1 : [0, 1], 2 : [0, -1], 3 : [1, 0], 4 : [-1, 0]}
        queue = deque([(0, 0, 0)])
        visited = {(0, 0) : 0}

        while queue:
            print(1)
            r, c, cost = queue.popleft()
            if (r, c) == (n - 1, m - 1):
                return cost

            for move in moves:
                print(2)
                x, y = moves[move]
                newR, newC = r + x, c + y
                newCost = cost if grid[r][c] == move else cost + 1
                if inBounds(newR, newC, newCost):
                    print(3)
                    visited[(newR, newC)] = newCost

                    if grid[r][c] == move:
                        queue.appendleft((newR, newC, newCost))
                    else:
                        queue.append((newR, newC, newCost))