# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i]!=s[i+1] for i in range(0, len(s), 2))
        

# Another way:
class Solution:
    def minChanges(self, s: str) -> int:
        c=0
        for i in range(0,len(s),2):
            if s[i]!=s[1+i]:
                c+=1
        return c