# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if (j > 0 and grid[i][j - 1] == 0) or j == 0:
                        cnt += 1

                    if (i > 0 and grid[i - 1][j] == 0) or i == 0:
                        cnt += 1

                    if (j < m - 1 and grid[i][j + 1] == 0) or j == m - 1:
                        cnt += 1

                    if (i < n - 1 and grid[i + 1][j] == 0) or i == n - 1:
                        cnt += 1
        return cnt
    
# another way:
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c=0
                if grid[i][j]==1:
                    if i-1>=0 and grid[i-1][j]==1:    c+=1
                    if j-1>=0 and grid[i][j-1]==1:    c+=1
                    if j+1<=len(grid[i])-1 and grid[i][j+1]==1:    c+=1
                    if i+1<=len(grid)-1 and grid[i+1][j]==1:    c+=1
                    s=s+(4-c)
        return s