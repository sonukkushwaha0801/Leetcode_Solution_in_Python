# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:   
        counter = 1
        if len(points) < 2:
            return 1
        for i in range(len(points)):
            egimList = {}
            for j in range(i+1,len(points)):
                y = points[j][1] - points[i][1]
                x = points[j][0] - points[i][0]
                if x != 0:
                    egimList[y / x] = 1 + egimList.get(y / x, 0)
                else:
                    egimList['inf'] = 1 + egimList.get('inf', 0)
            for key,value in egimList.items():
                counter = max(counter,value)
        return counter+1

# Another way:
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
                                              
        points.sort()
        slope, M = defaultdict(int), 0
        for i, (x1, y1) in enumerate(points):
            slope.clear()
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x1, y2 - y1
                G = gcd(dx, dy)
                m = (dx//G,dy//G)
                
                slope[m] += 1
                if slope[m] > M: M = slope[m]
    
        return M + 1