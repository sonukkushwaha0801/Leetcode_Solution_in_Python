# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        
        for char in s:
            if len(result) < 2 or not (result[-1] == result[-2] == char):
                result.append(char)
        return ''.join(result)
    
# ANOther way:
import re
class Solution:
    def makeFancyString(self, s: str) -> str:
        return re.sub(r'(.)\1+',r'\1\1',s)