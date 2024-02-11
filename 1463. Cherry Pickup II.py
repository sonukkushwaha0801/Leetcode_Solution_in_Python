# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from functools import lru_cache
from math import inf


class Solution:
    def cherryPickup(self, grid):
        m = len(grid)
        n = len(grid[0])
        mem = [[[ -1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        for A in mem:
            for B in A:
                B[:] = [-1] * n
        return self.cherryPick(grid, 0, 0, n - 1, mem)

    def cherryPick(self, grid, x, y1, y2, mem):
        if x == len(grid):
            return 0
        if y1 < 0 or y1 == len(grid[0]) or y2 < 0 or y2 == len(grid[0]):
            return 0
        if mem[x][y1][y2] != -1:
            return mem[x][y1][y2]
        currRow = grid[x][y1] + (0 if y1 == y2 else grid[x][y2])
        for d1 in range(-1, 2):
            for d2 in range(-1, 2):
                mem[x][y1][y2] = max(mem[x][y1][y2], currRow + self.cherryPick(grid, x + 1, y1 + d1, y2 + d2, mem))
        return mem[x][y1][y2]
    
# ANother way:
class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        @lru_cache(None)
        def dp(i,j,k):
            if not 0<=j<=k<n:
                return -inf
            if i==m:
                return 0
            ans=grid[i][j]+(j!=k)*grid[i][k]
            return ans+max(dp(i+1,y,z) for y in (j-1,j,j+1) for z in (k-1,k,k+1))
        return dp(0,0,n-1)          