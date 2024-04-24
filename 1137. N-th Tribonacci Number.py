# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def tribonacci(self, n: int) -> int:

        t0 =0
        t1= 1
        t2 =1
        for i in range(n):
            temp = t0
            t0 = t1
            t1 = t2
            t2 = temp + t0 + t1
            

        return t0      
    
# Another way:
class Solution:
    def tribonacci(self, n: int) -> int:

        t0,t1,t2 = 0,1,1
        for i in range(n):
            t0,t1,t2 = t1,t2,(t0+t1+t2)

        return t0