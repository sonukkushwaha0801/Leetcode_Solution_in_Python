# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    mod = 10 ** 9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return self.recursion(dp, n, k, target)

    def recursion(self, dp: list, n: int, k: int, target: int) -> int:
        if target == 0 and n == 0:
            return 1
        if n == 0 or target <= 0:
            return 0

        if dp[n][target] != -1:
            return dp[n][target] % self.mod

        ways = 0
        for i in range(1, k + 1):
            ways = (ways + self.recursion(dp, n - 1, k, target - i)) % self.mod

        dp[n][target] = ways % self.mod
        return dp[n][target]

# Another Way:
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        if n * k < target:
            return 0

        # Initialize a 2D list to store the number of ways to achieve each target sum using a specific number of dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # Dynamic Programming: Iterate over the number of dice and target sums
        for i in range(1, n + 1):
            for j in range(i, min(i * k, target) + 1):
                for temp in range(1, min(k, j) + 1):
                    # Update the number of ways to achieve the current target sum
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - temp]) % MOD

        # Return the result, cast to integer
        return int(dp[n][target])