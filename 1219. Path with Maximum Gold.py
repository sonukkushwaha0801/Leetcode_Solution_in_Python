# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List
class Solution:
  def getMaximumGold(self, grid: List[List[int]]) -> int:
    def dfs(i: int, j: int) -> int:
      if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
        return 0
      if grid[i][j] == 0:
        return 0

      gold = grid[i][j]
      grid[i][j] = 0  # Mark as visited.
      maxPath = max(dfs(i + 1, j), dfs(i - 1, j),
                    dfs(i, j + 1), dfs(i, j - 1))
      grid[i][j] = gold
      return gold + maxPath

    return max(dfs(i, j)
               for i in range(len(grid))
               for j in range(len(grid[0])))
  
# Another way:
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def local_max(x,y):
            nonlocal m,n
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            curr = grid[x][y]
            grid[x][y] = 0
            gold = curr + max(local_max(x+1,y), local_max(x-1,y), local_max(x,y+1), local_max(x,y-1))
            grid[x][y] = curr
            return gold
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, local_max(i, j))
        return max_gold