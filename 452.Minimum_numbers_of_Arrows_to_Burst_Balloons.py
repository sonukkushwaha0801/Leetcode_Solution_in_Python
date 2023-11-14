#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res, last_end = 0, -float('inf')
        for p in sorted(points, key = lambda x: x[1]):
            if p[0] > last_end:
                res += 1
                last_end = p[1]
        return res
    
# Another way:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        points = sorted(points, key = lambda x: x[1])
        maxa=-float('inf')
 
        ans=0

        for i in range(0,n):
            if maxa<points[i][0]:
                ans+=1
                maxa=points[i][1]

        return ans