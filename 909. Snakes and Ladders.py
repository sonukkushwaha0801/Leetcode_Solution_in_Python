# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque
import collections
from itertools import chain


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        def label_to_position(label):
            r, c = divmod(label-1, n)
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
            
        seen = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            label, step = queue.popleft()
            r, c = label_to_position(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n*n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step+1))
        return -1

# Another way:
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        
        board.reverse()
        for i in range(1,len(board),2): board[i].reverse()
        arr = [None]+list(chain(*board))
                                                            
        n, queue, seen, ct = len(arr)-1, deque([1]), {1}, 0               

        while queue:             
            lenQ = len(queue)

            for _ in range(lenQ):   

                cur = queue.popleft()
                if cur == n: return ct

                for i in range(cur+1, min(cur+7,n+1)): 
                    nxt = arr[i] if arr[i]+1 else i 

                    if nxt in seen: continue      
                    seen.add(nxt)
                    queue.append(nxt)
                    
            ct += 1                    
        
        return -1