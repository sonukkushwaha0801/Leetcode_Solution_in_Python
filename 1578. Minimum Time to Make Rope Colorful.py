# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        l=0
        removes=0
        for r in range(n):
            if (colors[r]!=colors[l]):
                sameColors=neededTime[l:r]
                removes+=sum(sameColors)-max(sameColors)
                l=r
        removes+=sum(neededTime[l:])-max(neededTime[l:])
        return removes
        
# Another way:
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        

        l=res=0

        for r in range(1,len(colors)):
            if colors[l]==colors[r]:
                if neededTime[l]<neededTime[r]:
                    res+=neededTime[l]
                    l=r
                else:
                    res+=neededTime[r]
            else:
                l=r 
                    

        return res
        