# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and (s+s).find(goal)!=-1
        

# Another way:
class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        doubled = s + s
        return goal in doubled