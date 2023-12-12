# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        final = []
        def trav(root,path):
            if not root:
                return None

            if not root.left and not root.right:
                final.append(path)
            
            if root.left:
                trav(root.left, path + [root.left.val])
            
            if root.right:
                trav(root.right, path +  [root.right.val])

        trav(root,[root.val])
        total = 0
        for path in final:
            s = 0
            for i in path:
                s = (s*10) + i
            total += s
        
        return total
    

# Another way:

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr,num):
            if curr is None:
                return 0
            num=num*10+curr.val
            if not curr.left  and not curr.right:
                return num
            return dfs(curr.left,num)+dfs(curr.right,num)
        return dfs(root,0)