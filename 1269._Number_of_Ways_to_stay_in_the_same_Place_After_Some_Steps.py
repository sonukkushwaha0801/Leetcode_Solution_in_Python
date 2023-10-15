# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxPosition = min(steps // 2 + 1, arrLen)
        dp = [[0] * maxPosition for _ in range(2)]
        dp[0][0] = 1
        
        for i in range(1, steps + 1):
            current, prev = i % 2, (i - 1) % 2
            for j in range(maxPosition):
                dp[current][j] = dp[prev][j]
                if j > 0:
                    dp[current][j] = (dp[current][j] + dp[prev][j - 1]) % MOD
                if j < maxPosition - 1:
                    dp[current][j] = (dp[current][j] + dp[prev][j + 1]) % MOD
        
        return dp[steps % 2][0]


# Another way:
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_position = min(steps // 2 + 1, arrLen)
        cur_ways = [0] * (max_position + 2)
        next_ways = [0] * (max_position + 2)
        cur_ways[1] = 1
        mod = 10 ** 9 + 7

        while steps > 0:
            for pos in range(1, max_position + 1):
                next_ways[pos] = ((cur_ways[pos] + cur_ways[pos - 1] + cur_ways[pos + 1]) % mod)

            cur_ways, next_ways = next_ways, cur_ways
            steps -= 1

        return cur_ways[1]