# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        if n == d:
            return sum(jobDifficulty)

        dp = [int(1e9)] * n
        dp[0] = jobDifficulty[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], jobDifficulty[i])

        dpPrev = dp.copy()

        for i in range(1, d):
            dp = [int(1e9)] * n
            for j in range(i, n):
                lastDayDifficulty = jobDifficulty[j]
                tmpMin = lastDayDifficulty + dpPrev[j - 1]

                for t in range(j - 1, i - 1, -1):
                    lastDayDifficulty = max(lastDayDifficulty, jobDifficulty[t])
                    tmpMin = min(tmpMin, lastDayDifficulty + dpPrev[t - 1])

                dp[j] = tmpMin
            dpPrev = dp.copy()

        return dp[n - 1]
    
# Another way:
class Solution:
    def minDifficulty(self, jD: list[int], d: int) -> int:
        if len(jD)<d:return -1
        def solve(i,d):
            if i==len(jD):return 100000000
            if d==1:return max(jD[i:])
            if dp[i][d]!=-1:return dp[i][d]
            ans=100000000
            mx=-1
            for j in range(i,len(jD)):
                mx=max(mx,jD[j])
                temp=mx+solve(j+1,d-1)
                ans=min(ans,temp)
            dp[i][d]=ans
            return dp[i][d]
        dp=[[-1 for i in range(d+1)] for i in range(len(jD))]
        return solve(0,d)