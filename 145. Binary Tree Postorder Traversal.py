# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.val)
        
        traverse(root)
        return result
    
# Another way:
class Solution:
    def postorderTraversal(self, r: Optional[TreeNode]) -> List[int]:
        return (f:=lambda n,q=[]:(n and (f(n.left),f(n.right),q.append(n.val))) and q)(r)