# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for c in s:
            low += 1 if c == '(' else -1
            high += 1 if c != ')' else -1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0
# Another way:
class Solution:
    def checkValidString(self, s: str) -> bool:
        curr = 0
        tot = 0
        for ch in s:
            if ch == '(':
                curr += 1
                tot += 1
            elif ch == ')':
                curr -= 1
                tot -= 1
            else: 
                curr -= 1
                tot += 1
            if curr < 0:
                curr = 0
            if tot < 0:
                return False
        return curr == 0 