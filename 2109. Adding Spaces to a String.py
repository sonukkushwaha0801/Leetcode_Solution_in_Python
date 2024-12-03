# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from bisect import bisect_left
from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        arr.append(s[:spaces[0]])
        for i in range(1, len(spaces)):
            arr.append(s[spaces[i-1]:spaces[i]])
        arr.append(s[spaces[-1]:])
        return ' '.join(arr)
    
# Another way:
class Solution:
    def addSpaces(self, s: str, a: List[int]) -> str:
        return ''.join(((q:=bisect_left(a,i))<len(a) and a[q]==i)*' '+c for i,c in enumerate(s))