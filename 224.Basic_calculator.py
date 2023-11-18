#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1]: current env's sign

        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c == '+' or c == '-':
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0

        return ans + sign * num
# Another way:
class Solution:
    def calculate(self, s: str) -> int:
        output, curr, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                curr = (curr * 10) + int(c)
            
            elif c in '+-':
                output += curr * sign
                curr = 0
                if c == '+':
                    sign = 1

                else:
                    sign = -1
            
            elif c == '(':
                stack.append(output)
                stack.append(sign)
                sign = 1
                output = 0
            
            elif c == ')':
                output += curr * sign
                output *= stack.pop()    #sign
                output += stack.pop()    #last output
                curr = 0

        return output + (curr * sign)