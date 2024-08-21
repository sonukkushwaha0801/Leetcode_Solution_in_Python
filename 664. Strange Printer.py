# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j] + 1
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j])
        
        return dp[0][n - 1]
    
# Another way:
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Filling DP table
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1 # A single character needs 1 turn
            for j in range(i + 1, n):
                dp[i][j] = dp[i][j - 1] + 1 # Initial assumption, print s[j] separately
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
        
        return dp[0][n - 1]