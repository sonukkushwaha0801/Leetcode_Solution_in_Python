# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = []
        for i in range(m):
            dp.append([[-1] * (maxMove + 1) for j in range(n)])
        return self.findPathMemo(dp, maxMove, startRow, startColumn)

    def findPathMemo(self, dp, leftMove, x, y):
        if leftMove < 0:
            return 0

        if x < 0 or x >= len(dp) or y < 0 or y >= len(dp[0]):
            return 1

        if dp[x][y][leftMove] >= 0:
            return dp[x][y][leftMove]

        pathNum = self.findPathMemo(dp, leftMove-1, x-1, y) + \
        self.findPathMemo(dp, leftMove-1, x+1, y) + \
        self.findPathMemo(dp, leftMove-1, x, y-1) + \
        self.findPathMemo(dp, leftMove-1, x, y+1)
        
        dp[x][y][leftMove] = pathNum

        return pathNum % (10**9+7)

# Another way:
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = (10**9) + 7
        cache = {}
        
        def dfs(r, c, moves):
            if r < 0 or r == m or c < 0 or c == n:
                return 1
            if moves == 0:
                return 0
            if (r, c, moves) in cache:
                return cache[(r, c, moves)]
            
            cache[(r, c, moves)] = (
                                    (dfs(r-1, c, moves - 1) +
                                    dfs(r+1, c, moves - 1)) % mod +
                                    (dfs(r, c+1, moves - 1) +
                                    dfs(r, c- 1, moves - 1)) % mod
                                    ) % mod
            return cache[(r, c, moves)]
        
        
        return dfs(startRow, startColumn, maxMove)