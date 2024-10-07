# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def minLength(self, s: str) -> int:
        temp = []
        for ch in s:
            if temp and temp[-1] == 'A' and ch == 'B':
                temp.pop()
            elif temp and temp[-1] == 'C' and ch == 'D':
                temp.pop()
            else:
                temp += ch
        return len(temp)
    
# Another way:
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i == "B" and stack[-1] == "A":
                    stack.pop() 
                elif i == "D" and stack[-1] == "C":
                    stack.pop() 
                else:
                    stack.append(i) 
        return len(stack) 