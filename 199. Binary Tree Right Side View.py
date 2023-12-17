# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

from pyparsing import Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root: return root
        q = [root]
        ans = []
        while q:
            t = q.copy()
            q.clear()

            r = 0
            for node in t:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                r = node.val
            ans.append(r)
        return ans
    
# Another way:
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        depth = 0
        

        def rightSide(root , result , depth):
            if root == None:
                return

            if len(result) == depth :
                result.append(root.val)

            depth += 1        

            rightSide(root.right , result , depth)
            rightSide(root.left , result , depth)

        rightSide(root , result , depth)
        return result    


        