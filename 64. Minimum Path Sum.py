# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==0:
                    if j!=0:
                        grid[i][j]+=grid[i][j-1]
                elif j==0:
                    if i!=0:
                        grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[n-1][m-1]
    
# Another way:
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    continue
                elif i==0:
                    grid[i][j]+=grid[i][j-1]
                elif j==0:
                    grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[-1][-1]