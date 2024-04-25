# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from operator import setitem


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:


        l = [0] * 128
        for c in s:
            i = ord(c)
            l[i] = max(l[i - k : i + k + 1]) + 1
        return max(l)
    
# Another way:
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        return (d:=[0]*123) and max(setitem(d,z:=ord(c),1+max(d[z-k:z+k+1])) or d[z] for c in s)