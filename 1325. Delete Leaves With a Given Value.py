# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        def f(n):
            if n:
                n.left, n.right = f(n.left), f(n.right)

                return (n, None)[n.left == n.right == None and n.val == t]
        
        return f(r)
    
# Another way:
class Solution(object):
    def removeLeafNodes(self, root, target):
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root