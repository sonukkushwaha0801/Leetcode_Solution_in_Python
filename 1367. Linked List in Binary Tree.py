# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :

class Solution(object):
    def checkPath(self, head, root):
        if not head:
            return True
        if not root or head.val != root.val:
            return False
        return self.checkPath(head.next, root.left) or self.checkPath(head.next, root.right)

    def isSubPath(self, head, root):
        if not root:
            return False
        return (head.val == root.val and self.checkPath(head, root)) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)      
    
# Another way:
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def comparison(root, head):
            if head is None: return True
            if root is None: return False
            if root.val != head.val: return False

            return comparison(root.left, head.next) or comparison(root.right, head.next)
        def inOrder(root, head):
            if root is None: return
            res = False
            if root.val == head.val:
                res = comparison(root, head)

            if res == True: return True
            return inOrder(root.left, head) or inOrder(root.right, head)

        return inOrder(root, head)