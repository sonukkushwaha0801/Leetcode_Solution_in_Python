# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n=len(s)
        alpha=[-1]*26
        maxLen=-1 
        for i, c in enumerate(s):
            if alpha[ord(c)-ord('a')]!=-1:
                maxLen =max(maxLen, i-alpha[ord(c)-ord('a')]-1)
            else:
               alpha[ord(c)-ord('a')]=i
        return maxLen

# Another way:
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max(s.rfind(ch) - s.find(ch) - 1 for ch in set(s))