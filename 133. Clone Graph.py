# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]
    
#Another way:
from typing import Optional

class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ntoc = {None: None} # node to copy

        def dfs(n):
            if n in ntoc:
                return ntoc[n]
            
            # create copy, search neighbors, return copy
            c = Node(n.val)
            ntoc[n] = c
            for nb in n.neighbors:
                c.neighbors.append(dfs(nb))
            return c
        
        return dfs(node)
