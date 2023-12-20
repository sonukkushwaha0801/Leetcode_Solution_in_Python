# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, cur = [], root
        
        while True:
            while cur: 
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
                
            cur = cur.right

# Another way:
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            li.append(root.val)
            helper(root.right)

        helper(root)
        return li[k - 1]
