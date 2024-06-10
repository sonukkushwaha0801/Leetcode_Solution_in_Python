# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freq=[0]*101
        for x in heights:
            freq[x]+=1
        cnt=0
        for x in range(1, 101):
            f=freq[x]
            for i in range(cnt, cnt+f):
                heights[i]-=x
            cnt+=f
        return len(heights)-heights.count(0)
        
# Another way:
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h!=s for h, s in zip(heights, sorted(heights)))