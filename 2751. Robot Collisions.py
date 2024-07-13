# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(list(zip(positions, directions, healths)))
        stack = []

        for bot in robots:
            c = False
            pos, dire, hp = bot
            while dire == 'L' and stack and stack[-1][1] == 'R':
                pos2, dire2, hp2 = stack.pop()
                if hp < hp2:
                    dire = 'R'
                    hp = hp2-1
                    pos = pos2
                elif hp > hp2:
                    hp -= 1
                else:
                    c = True
                    break
            if c: continue
            stack.append((pos, dire, hp))

        d = {pos: hp for pos, _, hp in stack}
        out = []
        for pos in positions:
            if pos in d: out.append(d[pos])
        return out
    
# Another way:
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        temp = []
        for i, j in enumerate(positions):
            temp.append((j, i))
        temp.sort()
        st = []
        for i in temp:
            if not st:
                st.append(i)
                continue
            if directions[i[1]] == 'R':
                st.append(i)
            else:
                hold = i
                while hold and st and directions[hold[1]] == 'L' and directions[st[-1][1]] == 'R':
                    a, b = st[-1][1], hold[1]
                    if healths[a] > healths[b]:
                        healths[a] -= 1
                        hold = None
                    elif healths[a] < healths[b]:
                        st.pop()
                        healths[b] -= 1
                    else:
                        st.pop()
                        hold = None
                if hold:st.append(i)
        d = {}
        for i in st:
            d[i[0]] = i[1]
        ans = []
        for i in positions:
            if i in d:
                ans.append(healths[d[i]])
        return ans
                      
        