# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspace_run(s):
            stack = []
            for char in s:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        
        final_s = backspace_run(s)
        final_t = backspace_run(t)
        return final_s == final_t

# Another Way:
import re
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(string):
            while '#' in string:
                string = re.sub(r'^#|[a-z]#', '', string)
            return string
        return solve(s) == solve(t)