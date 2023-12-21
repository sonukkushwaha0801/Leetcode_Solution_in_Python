# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from cmath import inf


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        stack.append([root,-1*float('inf'),float('inf')])
        while(stack):
            s=stack.pop()
            t=s[0]
            le=s[1]
            ri=s[2]
            if t.val<=le or t.val>=ri:
                return False
            if t.right!=None:
                stack.append([t.right,t.val,ri])
            if t.left!=None:
                stack.append([t.left,le,t.val])
        return True
    
# Another way:
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float(-inf), max_val=float(inf)) -> bool:
        return False if root.val < min_val or root.val > max_val else ((not root.right or self.isValidBST(root.right, root.val + 1, max_val)) and (not root.left or self.isValidBST(root.left, min_val, root.val - 1 )))