# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        return max(n-min(right+[n]), max(left+[0]))
    
# Another way:
class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        ans=0
        for i in left:
            ans=max(i,ans)
        for i in right:
            ans=max(n-i,ans)
        return ans        