# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            nonlocal res
            res = max(res, j)
            if res == cols - 1:
                return
            for d in (-1, 0, 1):
                ni = i + d
                if 0 <= ni < rows and grid[ni][j + 1] > grid[i][j]:
                    dfs(ni, j + 1)
            grid[i][j] = 0 

        for i in range(rows):
            dfs(i, 0)
        return res
    
# Another way:
class Solution:
    def __init__(self):
        self.ans = 0

    def adj(self, x, y, g):
        for (i, j) in [(-1, 1), (0, 1), (1, 1)]:
            if 0 <= x + i < len(g) and 0 <= y + j < len(g[0]):
                yield (x + i, y + j)
            else:
                continue
    
    def dfs(self, x, y, g, path = 0):
        self.ans = max(self.ans, path)
        for (i, j) in self.adj(x, y, g):
            if g[i][j] > g[x][y]: self.dfs(i, j, g, path + 1)
        g[x][y] = -1 # mark as visited


    def maxMoves(self, grid: List[List[int]]) -> int:
        for x in range(len(grid)):
            self.dfs(x, 0, grid)
        
        return self.ans