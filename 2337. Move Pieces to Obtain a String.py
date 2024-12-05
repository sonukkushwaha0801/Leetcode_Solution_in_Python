# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j, n = 0, 0, len(start)
        
        while i < n or j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            if i == n or j == n:
                break
            if start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            
            i += 1
            j += 1
        
        return i == n and j == n

# Another way:
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        sl_pos = []
        sr_pos = []
        tl_pos = []
        tr_pos = []
        for i in range(len(start)):
            if start[i] == 'L':
                sl_pos.append(i)
            elif start[i] == 'R':
                sr_pos.append(i)
            if target[i] == 'L':
                tl_pos.append(i)
            elif target[i] == 'R':
                tr_pos.append(i)
        for s_pos,t_pos in zip(sl_pos,tl_pos):
            if s_pos < t_pos:
                return False
        for s_pos,t_pos in zip(sr_pos,tr_pos):
            if s_pos > t_pos:
                return False
        return True
        
        