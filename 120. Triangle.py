# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[triangle[0][0]]]
        for d in range(1, len(triangle)):
            dp.append(
                [
                    min(
                        dp[d - 1][i] if i < len(dp[d - 1]) else float("Inf"),
                        dp[d - 1][i - 1] if i > 0 else float("Inf"),
                    )
                    + v
                    for i, v in enumerate(triangle[d])
                ]
            )
        return min(dp[-1])

# Another way:
class Solution:
    def minimumTotal(self, a: list[list[int]]) -> int:
        n=len(a)
        dp=[[0] * (n+1) for _ in range(n+1)]
        for level in range(n-1,-1,-1):
            for i in range(level+1):
                dp[level][i]=a[level][i] + min(dp[level+1][i], dp[level+1][i+1])
        return dp[0][0]            