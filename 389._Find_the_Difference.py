# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((Counter(t)-Counter(s)).keys())[0]
        

# Second Way:
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ord(t[-1])
        for i in range(len(s)):
            res += ord(t[i])
            res -= ord(s[i])
        return chr(res)