# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score
    
# Another way:
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(x)-ord(y)) for x, y in pairwise(s))