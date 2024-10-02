# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return [rank[x] for x in arr] if(rank:={x:i+1 for i,x in enumerate(sorted(set(arr)))}) else []
      

# Another way:
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        list1=[]
        x=sorted(set(arr))
        dict1={}
        for i in range(len(x)):
            dict1[x[i]]=i+1
        for j in arr:
            y=dict1[j]
            list1.append(y)
        return list1