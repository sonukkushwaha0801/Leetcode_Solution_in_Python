# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#Solution:

class Solution:
    def diffWaysToCompute(self, expression: str):
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, ch in enumerate(expression):
            if ch in '+-*':
                for l in self.diffWaysToCompute(expression[:i]):
                    for r in self.diffWaysToCompute(expression[i+1:]):
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        elif ch == '*':
                            res.append(l * r)
        return res
    
# Another One:
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        # Loop through the expression
        for i in range(len(expression)):
            oper = expression[i]
            # If the current character is an operator, split the expression
            if oper == "+" or oper == "-" or oper == "*":
                # Divide the expression into two parts
                sub_str1 = expression[:i]
                sub_str2 = expression[i+1:]
                
                # Recursively compute the results for both parts
                s1 = self.diffWaysToCompute(sub_str1)
                s2 = self.diffWaysToCompute(sub_str2)
                
                # Combine the results from both sides based on the operator
                for i in s1:
                    for j in s2:
                        if oper == "*":
                            res.append(int(i) * int(j))
                        if oper == "+":
                            res.append(int(i) + int(j))
                        if oper == "-":
                            res.append(int(i) - int(j))
        
        # If no operator was found, this means the expression is a single number
        if len(res) == 0:
            res.append(int(expression))
        
        return res