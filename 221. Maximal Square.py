# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp=[[0]*(len(matrix[0])+1)]
        for i in matrix:
            l=[0]
            for j in i:l.append(int(j))
            dp.append(l)
        mx=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                mx=max(mx,dp[i][j])
        return mx*mx
    
# Another way:
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        memo = [[0 for i in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        area = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    memo[i+1][j+1] = min(memo[i][j+1], memo[i+1][j], memo[i][j]) + 1
                    area = max(area, memo[i+1][j+1])
                    
        return area*area