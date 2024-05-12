# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        res = []

        for i in range(1, n - 1):
            tempRow = []
            for j in range(1, n - 1):
                temp = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        temp = max(temp, grid[k][l])
                tempRow.append(temp)
            res.append(tempRow)
        
        return res
    
# Another way to find the largest local solution:

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        return [[max(grid[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2)) for j in range(1, len(grid)-1)] for i in range(1, len(grid)-1)]