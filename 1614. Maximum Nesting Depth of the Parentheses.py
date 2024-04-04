# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def maxDepth(self, s):
        count = 0
        max_num = 0
        for i in s:
            if i == "(":
                count += 1
                if max_num < count:
                    max_num = count
            if i == ")":
                count -= 1
        return(max_num)
    
# Another way:
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_depth = 0
        for char in s:
            if char == '(':
                count += 1
            max_depth = max(count, max_depth)
            if char == ')':
                count -= 1
        return max_depth