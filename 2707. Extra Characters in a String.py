# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:

from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        diction = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                if s[j: i] in diction:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]
                
        
# Another way:
class Solution: 
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        words = defaultdict(list)
        for word in dictionary: words[word[0]].append(word)

        @lru_cache(1000)  
        def dp(ptr:int)-> int:

            if ptr == len(s): return 0

            cands = (w for w in words[s[ptr]] if s[ptr:].startswith(w))
            return min([dp(ptr+len(w)) for w in cands]+[1+dp(ptr+1)])

        return dp(0)