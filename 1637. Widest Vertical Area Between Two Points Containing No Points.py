# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()
        diff = 0
        for i in range(1, len(points)):
            diff = max(diff, points[i][0] - points[i - 1][0])
        return diff

# Another way:
class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_coordinates = sorted(set(point[0] for point in points))
        max_diff = 0
        prev_x = None
        
        for x in x_coordinates:
            if prev_x is not None:
                max_diff = max(max_diff, x - prev_x)
            prev_x = x
            
        return max_diff

