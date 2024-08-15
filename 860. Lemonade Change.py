# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5, cnt10=0, 0
        for b in bills:
            if b==5: cnt5+=1
            elif b==10:
                if cnt5>0:
                    cnt5-=1
                    cnt10+=1
                else:
                    return False
            else:
                if cnt10>0 and cnt5>0:
                    cnt10-=1
                    cnt5-=1
                elif cnt5>2: cnt5-=3
                else: return False
        return True
        
# Another way:
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives= 0 
        tens = 0 
        for i in bills:
            if(i==5):
                fives+=1 
            elif(i==10):
                tens+=1 
                if(fives>0):
                    fives-= 1 
                else:
                    return False
            else:
                if(tens>0 and fives>0):
                    tens-=1 
                    fives-=1 
                elif(fives>2):
                    fives-=3
                else:
                    return False
        return True