# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        currString = ""

        for i in range(len(s)): 
            if s[i] == '(':
                stack.append(currString)
                currString = ""
            elif s[i].isalpha():
                currString += s[i]
            elif s[i] == ')':
                currString = currString[::-1]
                stackTop = stack.pop()
                currString = stackTop + currString
            
        return currString
            
# Another way:
class Solution:
    def reverseParentheses(self, s: str) -> str:
        self.stack = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == '(':
                self.stack.append(i)
            elif s[i] == ')':
                j = self.stack.pop()
                s[j:i+1] = s[j:i+1][::-1]
        
        result = ''.join([char for char in s if char not in '()'])
        return result