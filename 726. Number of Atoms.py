# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from re import *
import re
from typing import Counter


class Solution:
    def countOfAtoms(self, s: str) -> str:
        return [s:=re.sub('\((\w+)\)(\d*)',lambda m:re.sub('([A-Z][a-z]*)(\d*)',lambda mm:mm[1]+str(int(mm[2] or '1')*int(m[2] or '1')),m[1]),s) for _ in s] and \
            ''.join(e+str(c)*(c>1) for e,c in sorted(sum((Counter({m[1]:int(m[2] or 1)}) for m in finditer('([A-Z][a-z]*)(\d*)',s)),Counter()).items()))
    
# Another  way:
class Solution:
    def countOfAtoms(self, s: str) -> str:
        pattern = r'([A-Z][a-z]*)(\d*)'

        def f(m):
            def ff(mm):
                return mm[1] + str(int(mm[2] or '1')*int(m[2] or '1'))

            return re.sub(pattern, ff, m[1])
        
        while '(' in s:
            s = re.sub(r'\((\w+)\)(\d*)', f, s)

        c = sum((Counter({m[1]: int(m[2] or 1)}) for m in finditer(pattern, s)), Counter())
        
        return ''.join(e + str(c)*(c>1) for e,c in sorted(c.items()))