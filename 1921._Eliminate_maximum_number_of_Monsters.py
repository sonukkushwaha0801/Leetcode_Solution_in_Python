# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
import math


class Solution:
    def eliminateMaximum(self, dist, speed):
        n = len(dist)

        for i in range(n):
            dist[i] = math.ceil(dist[i] / speed[i])
        dist.sort()

        i = 0
        for j in range(n):
            if i >= dist[j]:
                return i
            i += 1

        return n

# Another way:
class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        n=len(dist)
        monsters_t=[0]*(n+1)

        for i in range(n):
            # the following is ceil function
            t=(dist[i]+speed[i]-1)//speed[i] 
            if t>n: 
                t=n
            monsters_t[t]+=1
        
        shot=1
        monsters=0
        while shot<=n:
            monsters+=monsters_t[shot-1]
            if shot<=monsters: 
                break
            shot+=1
        shot-=1
        return shot
        
        