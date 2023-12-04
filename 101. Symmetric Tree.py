# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSame(root.left, root.right)
    def isSame(self, leftroot, rightroot):
        if leftroot == None and rightroot == None:
            return True
        if leftroot == None or rightroot == None:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
    
# Another way:

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]
        while stack:
            node1,node2 = stack.pop(), stack.pop()
            if node1 is None and node2 is None: continue
            elif (node1 is None or node2 is None) or node1.val != node2.val: 
                return False

            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True