# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        ans = 0
        
        if root.left:
            if not root.left.left and not root.left.right:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        
        ans += self.sumOfLeftLeaves(root.right)
        
        return ans
    
# Another way:
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.find_val(root, 1)
    
    def find_val(self, root: Optional[TreeNode], flag: int) -> int:
        if not root:
            return 0
        if flag == 0 and not root.right and not root.left:
            return root.val
        return self.find_val(root.left, 0) + self.find_val(root.right, 1)