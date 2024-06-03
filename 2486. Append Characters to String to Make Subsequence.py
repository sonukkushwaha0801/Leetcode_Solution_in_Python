# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from functools import reduce


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        return reduce(lambda i,c:i-(i and c==t[-i]),s,len(t))
    
# Another way:
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        start = 0
        for c in s:
            if start >= len(t):
                return 0
            if c == t[start]:
                start += 1
        return len(t[start:])