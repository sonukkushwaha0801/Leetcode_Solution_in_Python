# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        return next((s for s in words if s==s[::-1]), "")
        
# Another way:
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        return next((s for s in words if all(s[i]==s[-(i+1)] for i in range(len(s)//2))), "")