# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)
        return sCount == tCount

# Type Second:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(s)==sorted(t))