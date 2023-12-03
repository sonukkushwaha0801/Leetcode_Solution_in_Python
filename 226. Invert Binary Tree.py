# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def firstPass(curr = root):
            if curr != None:
                curr.left, curr.right = curr.right, curr.left
                firstPass(curr.left)
                firstPass(curr.right)
            return
        firstPass()
        return root