# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import Counter, List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])

        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(m + 1):
            for j in range(n):
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD

                if i < m:
                    char_idx = ord(target[i]) - ord('a')
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * freq[j][char_idx]) % MOD

        return dp[m][n]
    

# Another way:
class Solution:
    def numWays(self, a: List[str], t: str) -> int:
        return (f:=cache(lambda i,j,z=[*map(Counter,zip(*a))]:i==len(t) or j<len(a[0]) and z[j][t[i]]*f(i+1,j+1)+f(i,j+1)))(0,0)%(10**9+7)