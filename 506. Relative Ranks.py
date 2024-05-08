# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from itertools import chain, count


class Solution:
    def findRelativeRanks(self, a: list[int]) -> list[str]:
        return map({v:{1:'Gold Medal',2:'Silver Medal',3:'Bronze Medal'}.get(i,str(i)) for i,v in enumerate(sorted(a)[::-1],1)}.get,a)
    
# Another way:
class Solution:
    def findRelativeRanks(self, a: list[int]) -> list[str]:
        return map(dict(zip(sorted(a)[::-1],chain(('Gold Medal','Silver Medal','Bronze Medal'),map(str,count(4))))).get,a)