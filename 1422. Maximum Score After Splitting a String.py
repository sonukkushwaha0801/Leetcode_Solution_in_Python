# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxScore(self, s: str) -> int:
        Max=0
        for i in range(1,len(s)):
            maxx=s[:i].count("0")+s[i:].count("1")
            Max=max(Max,maxx)
        return Max

# Another way:
class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones, ans = 0, 0, float('-inf')
        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            if i != len(s) - 1:
                ans = max(ans, zeros - ones)
        return ans + ones