# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([('0000', 0)]) 
        visited = set('0000')
        
        while queue:
            current_combination, moves = queue.popleft()
            
            if current_combination == target:
                return moves
            
            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(current_combination[i]) + delta) % 10
                    new_combination = (
                        current_combination[:i] + str(new_digit) + current_combination[i+1:]
                    )
                    
                    if new_combination not in visited and new_combination not in deadends:
                        visited.add(new_combination)
                        queue.append((new_combination, moves + 1))
    
        return -1
    
# Another way:
from queue import deque
class Solution:

    def openLock(self, deadends: list[str], target: str) -> int:
        queue = deque()
        
        deadends = set(deadends)
        if "0000" not in deadends:
            deadends.add("0000")
            queue.append(("0000", 0))
        while queue:
            curr_combination, moves = queue.popleft()
            if curr_combination == target:
                return moves
            
            for i in range(4):
                new_combination = curr_combination[:i] + str((int(curr_combination[i])+1)%10) + curr_combination[i+1:]
                if new_combination not in deadends:
                    deadends.add(new_combination)
                    queue.append((new_combination, moves+1))
                new_combination = curr_combination[:i] + str((int(curr_combination[i])-1)%10) + curr_combination[i+1:]
                if new_combination not in deadends:
                    deadends.add(new_combination)
                    queue.append((new_combination, moves+1))
        return -1




            





        