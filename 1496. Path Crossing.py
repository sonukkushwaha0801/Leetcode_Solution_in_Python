# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        P=set()
        P.add((0, 0))
        x, y= 0, 0
        for c in path:
            if c=='N': y+=1
            elif c=='S': y-=1
            elif c=='E': x+=1
            else: x-=1
            if (x, y) in P : return True
            P.add((x, y))
        return False
    
# Another way:
def isPathCrossing(movementPath):
    visitedPoints = set()
    currentX, currentY = 0, 0
    visitedPoints.add((currentX, currentY))

    for direction in movementPath:
        if direction == 'N':
            currentY += 1
        elif direction == 'S':
            currentY -= 1
        elif direction == 'E':
            currentX += 1
        else:
            currentX -= 1

        if (currentX, currentY) in visitedPoints:
            return True

        visitedPoints.add((currentX, currentY))

    return False