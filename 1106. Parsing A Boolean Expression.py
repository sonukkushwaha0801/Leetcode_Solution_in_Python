# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from functools import cache
from typing import List


class Solution:
    @cache
    def parseBoolExpr(self, expression: str) -> bool:
        if expression[0] == '&':
            return all(map(self.parseBoolExpr, self.split(expression[2:-1])))
        if expression[0] == '|':
            return any(map(self.parseBoolExpr, self.split(expression[2:-1])))
        if expression[0] == '!':
            return not self.parseBoolExpr(expression[2:-1])
        if expression == 'f':
            return False
        if expression == 't':
            return True
    
    def split(self, expression: str) -> List[str]:
        opened = 0
        prev = 0
        res = []
        for i in range(len(expression)):
            if expression[i] == '(':
                opened += 1
            elif expression[i] == ')':
                opened -= 1
            
            if expression[i] == ',' and not opened:
                res.append(expression[prev:i])
                prev = i+1
        res.append(expression[prev:i+1])
        return res
    
# Another way:
class Solution:
    def andd(self, exp):
        n = len(exp)
        j = 0
        subexp = ""
        active = 0

        while j < n:
            if active == 0 and exp[j] == ',':
                if not self.parseBoolExpr(subexp):
                    return False
                subexp = ""
                j += 1
                continue
            if exp[j] == '(':
                active += 1
            if exp[j] == ')':
                active -= 1

            subexp += exp[j]
            j += 1
        if not self.parseBoolExpr(subexp):
            return False

        return True

    def orr(self, exp):
        n = len(exp)
        j = 0
        subexp = ""
        active = 0

        while j < n:
            if active == 0 and exp[j] == ',':
                if self.parseBoolExpr(subexp):
                    return True  
                subexp = ""  
                j += 1
                continue
            if exp[j] == '(':
                active += 1
            if exp[j] == ')':
                active -= 1

            subexp += exp[j]
            j += 1
        if self.parseBoolExpr(subexp):
            return True

        return False 

    def parseBoolExpr(self, exp):
        n = len(exp)
        if n == 1:
            return exp[0] == 't'
        if exp[0] == '!':
            return not self.parseBoolExpr(exp[2:n-1])
        if exp[0] == '&':
            return self.andd(exp[2:n-1])
        if exp[0] == '|':
            return self.orr(exp[2:n-1])

        return False  