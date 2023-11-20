# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from cv2 import accumulate


class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        n=len(garbage)
        tG, tP, tM=0, 0, 0
        Time=0
        for i in range(n-1, -1, -1):
            x=garbage[i]
            Time+=len(x)
            if tG==0 and x.find('G')!=-1: tG=i 
            if tP==0 and x.find('P')!=-1: tP=i
            if tM==0 and x.find('M')!=-1: tM=i
        Time+=sum(travel[:tG])+sum(travel[:tP])+sum(travel[:tM])
        return Time

# Another way:
class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        peekGarbageTime = endM = endP = endG = 0

        for i, g in reversed(list(enumerate(garbage))):
            peekGarbageTime += len(g)
            if not endM and 'M' in g: endM = i
            if not endP and 'P' in g: endP = i
            if not endG and 'G' in g: endG = i

        dist = list(accumulate(travel, initial = 0))

        return dist[endM] + dist[endP] + dist[endG] + peekGarbageTime