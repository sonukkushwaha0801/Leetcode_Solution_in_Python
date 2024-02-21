# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import Optional
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        row, col = len(word1), len(word2)

        d = [[0] * (col+1) for _ in range(row+1)]

        for i in range(row+1):
            d[i][0] = i
        for j in range(col+1):
            d[0][j] = j

        for i in range(1, row+1):
            for j in range(1, col+1):
                
                

                d[i][j] = min(
                    d[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                    d[i][j-1] + 1,
                    d[i-1][j] + 1
                )
        
        return d[-1][-1]
    
# Another way:
class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
      dp[i][0] = i

    for j in range(1, n + 1):
      dp[0][j] = j

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]