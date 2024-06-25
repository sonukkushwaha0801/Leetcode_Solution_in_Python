# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    sum=0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: return root
        self.bstToGst(root.right)
        self.sum+=root.val
        root.val=self.sum
        self.bstToGst(root.left)
        return root
    
# Another way:
class Solution:
    def __init__(self):
        self.tally = 0


    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: return
        
        self.bstToGst(root.right)
        self.tally+= root.val
        root.val = self.tally
        self.bstToGst(root.left)
        
        return root