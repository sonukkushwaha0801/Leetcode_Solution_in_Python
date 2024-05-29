# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s != "1":
            if s[-1] == "0":
                s = s[:-1]
            else:
                s = bin(int(s, 2) + 1)[2:]
            steps += 1
        return steps
    
# Wrapped solution:
class Solution:
    def numSteps(self, s: str) -> int:
        return (f:=lambda v:v>1 and 1+f((v>>1,v+1)[v%2]) or 0)(int(s,2))