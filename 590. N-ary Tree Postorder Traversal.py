# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        output = []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.children:
                stack.extend(node.children)
        
        return output[::-1]
    
# Another way:
class Solution:
    def postorder(self, r: 'Node') -> List[int]:
        return (f:=lambda n,q=[]:n and [*map(f,n.children),q.append(n.val)] and q)(r)