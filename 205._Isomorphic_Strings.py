# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))

# Another way:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(s) == len(t) and all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))