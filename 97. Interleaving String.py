# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        if m < n:
            return self.isInterleave(s2, s1, s3)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[n]
    
# Another way:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def rec(i1, i2, i3):
            if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
                return True
            return i3 < len(s3) and (i1 < len(s1) and s1[i1] == s3[i3] and rec(i1+1, i2, i3+1) or i2 < len(s2) and s2[i2] == s3[i3] and rec(i1, i2+1, i3+1))
        
        return rec(0, 0, 0)