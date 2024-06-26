# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def inorder(root):
            if root==None: return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        def BST(l, r):
            if l>r: return None
            m=(l+r)//2
            left=BST(l, m-1)
            right=BST(m+1, r)
            return TreeNode(arr[m], left, right)
        
        inorder(root)
        return BST(0, len(arr)-1)