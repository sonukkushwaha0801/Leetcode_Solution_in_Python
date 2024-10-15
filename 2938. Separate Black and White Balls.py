# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def minimumSteps(self, s: str) -> int:
        return (b:=0)+sum((b:=b+(c>'0'))*(c<'1') for c in s)
    
# ANother way:
class Solution:
    def minimumSteps(self, s: str) -> int:
        res, i = 0, 0
        for j,c in enumerate(s):
            if c == '0':
                res += j - i
                i += 1

        return res