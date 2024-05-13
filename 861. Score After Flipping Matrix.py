# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        for j in range(m):
            set_count = sum(grid[i][j] == grid[i][0] for i in range(n))
            res += max(set_count, n - set_count) * (1 << (m - 1 - j))

        return res
    
# Another way:
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        for i in range(m):
            s = ''.join(map(str,grid[i]))
            dec = int(s,2)
            if dec^int('1'*len(s),2)>dec:
                for j in range(n):
                    grid[i][j] = (grid[i][j]+1)%2

        for j in range(n):
            count1 = 0
            for i in range(m):
                count1+=grid[i][j]

            if count1<m-count1:
                for i in range(m):
                    grid[i][j] = (grid[i][j]+1)%2

        ans = 0
        for i in range(m):
            ans+=int(''.join(map(str,grid[i])),2)

        return ans
            