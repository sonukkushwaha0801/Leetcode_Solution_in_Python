# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.right:
            return root.val
        else:
            if root.val == 3:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        
# Another way:
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True if root.val else False

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)