# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False

# Type Two:
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return any([s[:i]*(len(s)//i) == s for i in range(1, len(s))])