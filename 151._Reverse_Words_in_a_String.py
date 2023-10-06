# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split()
        return " ".join(s[::-1])

# Another Way: 
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
