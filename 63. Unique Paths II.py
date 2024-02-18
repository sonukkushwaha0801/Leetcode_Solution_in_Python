# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from itertools import product


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] or (i == 0 and j == 0): continue
                dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)
        return dp[m-1][n-1]
    
# Another way:
class Solution:
    def uniquePathsWithObstacles(self, A: list[list[int]]) -> int:
        if A[0][0] or A[-1][-1]:
            return 0
        rangeN, rangeM, source = range(len(A)), range(len(A[0])), [(-1, 0), (0, -1)]
        A[0][0] = -1
        for i, j, (_i, _j) in product(rangeN, rangeM, source):
            if A[i][j] == 1:
                continue
            try:
                if i+_i != -1 and j+_j != -1 and A[i+_i][j+_j] != 1:
                    A[i][j] += A[i+_i][j+_j]
            except:
                pass
        return -A[-1][-1]