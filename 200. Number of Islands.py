# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque
class Solution:
    def numIslands(self, grid):
        count = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.helper(grid,queue)
                    count += 1
        print(grid)
        return count
    
    def helper(self,grid,queue):
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0<= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0 

# Another way:
from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    #print(i,j,grid)
                    grid[i][j] = '0'
                    self.helper(grid,i,j)
                    count += 1
        return count
    def helper(self,grid,i,j):
        queue = deque([(i,j)])
        while queue:
            I,J = queue.popleft()
            for i,j in [I+1,J],[I,J+1],[I-1,J],[I,J-1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i,j))