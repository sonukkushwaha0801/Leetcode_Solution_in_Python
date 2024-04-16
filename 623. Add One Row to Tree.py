# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]: # type: ignore
        def dfs(node, level):
            if node:  
                if level + 1 == depth:
      
                    Leftnode = node.left
                    newnode = TreeNode(val) # type: ignore
                    node.left = newnode
                    newnode.left = Leftnode
                    
                    Rightnode = node.right
                    newnode = TreeNode(val) # type: ignore
                    node.right = newnode
                    newnode.right = Rightnode
                        
                dfs(node.left,  level+1)
                dfs(node.right, level+1)

        if depth == 1:
            newnode = TreeNode(val) # type: ignore
            newnode.left = root
            return newnode
            
        dfs(root, 1)
        return root
    
# Another way:
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int, side = "left") -> TreeNode: # type: ignore
        if d == 1:
            res = TreeNode(v) # type: ignore
            setattr(res, side, root)
            return res
        if root:
            root.left = self.addOneRow(root.left, v, d - 1)
            root.right = self.addOneRow(root.right, v, d - 1, 'right')
        return root