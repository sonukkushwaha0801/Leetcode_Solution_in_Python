# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def solve(self, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0
        ans = 0
        if text1[i] == text2[j]:
            ans = 1 + self.solve(text1, text2, i+1, j+1)
        else:
            ans = max(self.solve(text1, text2, i+1, j), self.solve(text1, text2, i, j+1))
        return ans

    def solve_mem(self, text1, text2, i, j, dp):
        if i == len(text1) or j == len(text2):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 0
        if text1[i] == text2[j]:
            ans = 1 + self.solve_mem(text1, text2, i+1, j+1, dp)
        else:
            ans = max(self.solve_mem(text1, text2, i+1, j, dp), self.solve_mem(text1, text2, i, j+1, dp))
        dp[i][j] = ans
        return ans

    def solve_tab(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                ans = 0
                if text1[i] == text2[j]:
                    ans = 1 + dp[i+1][j+1]
                else:
                    ans = max(dp[i+1][j], dp[i][j+1])
                dp[i][j] = ans
        return dp[0][0]

    def solve_tab_so(self, text1, text2):
        n = len(text1)
        m = len(text2)
        curr = [0] * (m+1)
        next_row = [0] * (m+1)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                ans = 0
                if text1[i] == text2[j]:
                    ans = 1 + next_row[j+1]
                else:
                    ans = max(next_row[j], curr[j+1])
                curr[j] = ans
            next_row = curr.copy()
        return next_row[0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve_tab_so(text1, text2)
    
# Another way:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]