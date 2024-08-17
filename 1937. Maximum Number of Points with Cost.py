# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [0] * n

        for j in range(n):
            dp[j] = points[0][j]

        for i in range(1, m):
            leftMax = [0] * n
            rightMax = [0] * n
            newDp = [0] * n

            leftMax[0] = dp[0]
            for j in range(1, n):
                leftMax[j] = max(leftMax[j - 1], dp[j] + j)

            rightMax[n - 1] = dp[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                rightMax[j] = max(rightMax[j + 1], dp[j] - j)

            for j in range(n):
                newDp[j] = max(leftMax[j] - j, rightMax[j] + j) + points[i][j]

            dp = newDp

        return max(dp)
    
# Another way:

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        for i in range(len(points)):
            if i > 0:
                for j in range(len(points[0])):
                    points[i][j] += points[i-1][j]
            for j in range(1,len(points[0])):
                points[i][j] = max(points[i][j],points[i][j-1]-1)
            for j in range(len(points[0])-2,-1,-1):
                points[i][j] = max(points[i][j],points[i][j+1]-1)
        return max(points[-1])