# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n=len(s)
        dp=[True]
        for i in range(1,n+1):
            dp.append(any(dp[j] and s[j:i] in wordDict for j in range(i)))

        return dp[-1]    
# Another way:
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        n=len(s)
        dp = [False for _ in range(n+1)]
        dp[0]=True
        
        for i in range(n):
            if dp[i]:
                for w in wordDict:
                    if s[i:i+len(w)]==w:
                        dp[i+len(w)]=True
        return dp[-1]
	