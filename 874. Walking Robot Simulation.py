# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir=['N','E','S','W']
        d=0
        x=0
        y=0
        res=0
        s=set((i,j) for i,j in obstacles)
        for i in range(len(commands)):
            if commands[i]==-1:
                d+=1
                d=d%4
            elif  commands[i]==-2:
                d-=1
                d=d%4
            else:
                if dir[d]=='N':
                    for move in range(commands[i]):
                        if (x,y+1) in s:
                            break
                        y+=1
                elif dir[d]=='E':
                    for move in range(commands[i]):
                        if (x+1,y) in s:
                            break
                        x+=1
                elif dir[d]=='S':
                    for move in range(commands[i]):
                        if (x,y-1) in s:
                            break
                        y-=1
                else:
                    for move in range(commands[i]):
                        if (x-1,y) in s:
                            break
                        x-=1
            res=max(res,x**2+y**2)
        return res

# Another way:
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple,obstacles))
        directions = {'N':{-2:'W',-1:'E'},'E':{-2:'N',-1:'S'},'S':{-2:'E',-1:'W'},'W':{-2:'S',-1:'N'}}
        x = y =0
        direction = 'N'
        res = 0
        for i in commands:
            if i < 0:
                direction = directions[direction][i]
                continue
            steps = i
            match direction:
                case 'N':
                    while steps > 0 and (x,y+1) not in obstacles:
                        y+=1
                        steps-=1
                case 'E':
                    while steps > 0 and (x+1,y) not in obstacles:
                        x+=1
                        steps-=1
                case 'S':
                    while steps > 0 and (x,y-1) not in obstacles:
                        y-=1
                        steps-=1
                case 'W':
                    while steps > 0 and (x-1,y) not in obstacles:
                        x-=1
                        steps-=1
            res = max(res,(x ** 2) + (y ** 2))
        return res
        