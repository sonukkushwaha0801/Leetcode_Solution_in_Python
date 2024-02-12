# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                    
        return dp[-1]
    
# Another way:
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        q = deque([s])
        while q:
            remaining = q.popleft()
            for word in wordDict:
                if remaining == word:
                    return True
                elif remaining.startswith(word):
                    q.append(remaining[len(word):])
        return False