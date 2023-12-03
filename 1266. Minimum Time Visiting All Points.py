# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
from ast import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        point=0
        for i in range(0,len(points)-1):
            point+=max(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        return point

# Another way:
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0

        for i in range(1, len(points)):

            previousPoint = points[i - 1]
            currentPoint = points[i]

            xDistance = abs(currentPoint[0] - previousPoint[0])
            yDistance = abs(currentPoint[1] - previousPoint[1])

            totalTime += max(xDistance, yDistance)

        return totalTime

        