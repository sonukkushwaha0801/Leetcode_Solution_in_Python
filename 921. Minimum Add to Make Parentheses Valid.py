# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for x in s:
            if stack and stack[-1] == '(' and x == ')':
                stack.pop()
            else:
                stack.append(x)
        return len(stack)

# ANother way:
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        b = "()"
        if b not in s:
            return len(s)
        else:
            while b in s:
                s = s.replace(b,'')
        return len(s)

        