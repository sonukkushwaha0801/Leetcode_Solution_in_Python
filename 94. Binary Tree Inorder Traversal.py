# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res
    
# Another way:
class Solution(object):
    def inorderTraversal(self, root):
        def helper(root,result):
          if root != None:
            helper(root.left,result)
            result.append(root.val)
            helper(root.right,result)  
            
        result = []
        helper(root,result)
        return result