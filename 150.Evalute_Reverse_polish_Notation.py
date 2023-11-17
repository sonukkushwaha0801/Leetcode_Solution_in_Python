#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        for t in tokens:
            if t in op:
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(x + y if t == '+' else y - x if t == '-' else x * y if t == '*' else int(y / x))
            else:
                stack.append(t)
        return int(stack[-1])

# Another way:
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        signs = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y
        }


        for token in tokens:
            if token not in signs:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(int(signs[token](left, right)))
            
        return stack.pop()
            
    