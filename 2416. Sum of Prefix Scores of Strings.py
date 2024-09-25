# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# Solution:

from collections import defaultdict
from operator import setitem
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        k=defaultdict(int)
        ans=[]
        for i in words:
            for j in range(len(i)):
                k[i[0:j+1]]+=1
        #print(k)
        for i in words:
            temp=0
            for j in range(len(i)):
                temp+=k[i[0:j+1]]
            ans.append(temp)
        return ans

# Another way:
class Solution:
    def sumPrefixScores(self, a: List[str]) -> List[int]:
        d = {}
        [(p:=d,all((setitem(p.setdefault(c,{0:0}),0,p[c][0]+1),p:=p[c]) for c in s)) for s in a]

        return [(p:=d) and sum((p[c][0],p:=p[c])[0] for c in s) for s in a]