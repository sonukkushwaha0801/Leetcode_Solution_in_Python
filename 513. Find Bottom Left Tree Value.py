# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque
from functools import reduce
from typing import Optional


class Solution:
    def findBottomLeftValue(self, r: Optional[TreeNode]) -> int:
        return reduce(lambda _,n:q.extend(filter(None,(n.right,n.left))) or n.val,q:=[r],0)
    
# Another way:
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        node  = None

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return node.val
                