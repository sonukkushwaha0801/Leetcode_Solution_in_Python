# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count=0
        prev='X'
        maxd=' '
        for c in num:
            if c==prev: count+=1
            else: count=1
            if count==3: maxd=max(c, maxd)
            prev=c
        if maxd==' ': return ""
        return maxd*3

# Another way:
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return str(next((d for d in range(9,-1,-1) if num.find(str(d)*3)>=0), ''))*3