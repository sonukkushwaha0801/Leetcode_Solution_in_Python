# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten(root.right)  
        self.flatten(root.left)
        root.right = self.prev
        root.left = None 
        self.prev = root

# Another way:

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        def dfs(root):
            if root == None: return root

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            
            return rightTail or leftTail or root
        
        return dfs(root)
        