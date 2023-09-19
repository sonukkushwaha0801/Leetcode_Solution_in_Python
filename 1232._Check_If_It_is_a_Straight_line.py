# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for i in range(2, n):
            x, y = coordinates[i]

            if (y - y1) * (x - x2) != (y - y2) * (x - x1):
                return False

        return True
    
# Second Type:
class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        point1 = coordinates[0]
        point2 = coordinates[1]
        for point in coordinates:
            if not self.is_straight_line(point1, point2, point):
                return False
        return True

    def is_straight_line(self, point1: list[int], point2: list[int], point3: list[int]) -> bool:
        (x1, y1) = point1
        (x2, y2) = point2
        (x3, y3) = point3
        return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)