# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if not node:
                return ""
            if node.right:
                return f"{node.val}({dfs(node.left)})({dfs(node.right)})"
            elif node.left:
                return f"{node.val}({dfs(node.left)})"
            else:
                return f"{node.val}"
        return dfs(root)
    
# Another way:

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
      res = []
      def preorder(root):
        if not root:
          return 
        res.append('(')
        res.append(str(root.val))
        if not root.left and root.right:
          res.append("()") 
        preorder(root.left)
        preorder(root.right)
        res.append(")")
      preorder(root)
      return "".join(res[1:-1])
            
        