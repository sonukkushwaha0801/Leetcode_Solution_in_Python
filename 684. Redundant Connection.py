# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        return (t:=''.join(map(chr,range(1001)))) and next([u,v] for u,v in e if (t[u]==t[v],t:=t.replace(t[u],t[v]))[0])

# Another way:
class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        t = ''.join(map(chr, range(1001)))
        for u,v in e:
            if t[u] == t[v]:
                return [u, v]
                
            t = t.replace(t[u], t[v])