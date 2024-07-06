# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one: 
class Solution(object):
    def passThePillow(self, n, time):
        stand, flag = 1, 1
        while time:
            time -= 1
            if flag:
                stand += 1
                if stand == n:
                    flag = not flag
            else:
                stand -= 1
                if stand == 1:
                    flag = not flag
        return stand
    
# Another way:
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = (n - 1) * 2

        position_in_cycle = time % cycle_length
        
        if position_in_cycle < n:
            return position_in_cycle + 1
        else:
            return 2 * n - position_in_cycle - 1
        