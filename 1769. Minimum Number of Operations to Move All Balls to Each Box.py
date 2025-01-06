#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ans=[0]*n
        P=[]

        for i, x in enumerate(boxes):
            if x=='1':
                P.append(i)
                ans[0]+=i

        pz=len(P)
        L, R=0, pz
        j=0
        for i in range(1, n):
            if j<pz and i>P[j]:
                L+=1
                R-=1
                j+=1
            ans[i]=ans[i-1]+L-R
        return ans
    
# Another way:
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        bl, br = 0, 0
        ml, mr = 0, 0
        n = len(boxes)
        res = [0]*n
        for i in range(n):
            res[i] += bl + ml
            j = n-1-i
            res[j] += br + mr
            ml = bl + ml
            mr = br + mr
            bl += 1 if boxes[i] == '1' else 0
            br += 1 if boxes[j] == '1' else 0
            # print(res, i)
        return res
