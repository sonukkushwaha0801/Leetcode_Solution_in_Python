# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if(fx==sx and fy==sy):
            if(t > 1 or t==0):
                return True
            return False
        
        xDiff = abs(fx-sx)
        yDiff = abs(fy-sy)
       
        if(max(xDiff,yDiff) <= t):
            return True
        return False

# Another way:
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and sx == fx and sy == fy:
            return False
        
        return max((abs(sx - fx)), (abs(sy - fy))) <= t