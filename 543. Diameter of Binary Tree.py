# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, res):
            if not node:
                return 0
            
            left = diameter(node.left, res)
            right = diameter(node.right, res)

            res[0] = max(res[0], left + right)
            return max(left, right) + 1
        res = [0]
        diameter(root, res)
        return res[0]
    
# Another way:
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root):
            nonlocal ans
            if not root: return 0
            r=dfs(root.left)
            l=dfs(root.right)
            ans=max(ans, l+r)
            return 1+max(l, r)
        
        dfs(root)
        return ans
        