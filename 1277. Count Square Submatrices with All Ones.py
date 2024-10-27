# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row < m - 1 and col < n - 1:
                    if matrix[row][col]:
                        matrix[row][col] += min(matrix[row + 1][col], matrix[row][col + 1], matrix[row + 1][col + 1])
                res += matrix[row][col]
        return res
    
# Another way:
class Solution:
    def countSquares(self, arr: List[List[int]]) -> int:
        n=len(arr)
        m=len(arr[0])
        dp=[[0 for i in range(m)]for j in range(n)]
        for i in range(n):
            dp[i][0]=arr[i][0]
        for j in range(m):
            dp[0][j]=arr[0][j]
        for i in range(1,n):
            for j in range(1,m):
                if arr[i][j]==1:
                    dp[i][j]= 1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                else:
                    dp[i][j]=0
                    
        ans=0
        for i in range(n):
            ans+=sum(dp[i])
        return ans