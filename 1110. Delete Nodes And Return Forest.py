# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def DFS(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = DFS(root.left, parent_exist=False)
                root.right = DFS(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = DFS(root.left, parent_exist=True)
                root.right = DFS(root.right, parent_exist=True)
                return root
        DFS(root, parent_exist=False)
        return res
    
# Another way:
class Solution(object):
    def delNodes(self, root, to_delete):
        ans = []
        d = set(to_delete)
        def postorder(node):
            if node==None:
                return
            postorder(node.left)
            postorder(node.right)
            if node.left and node.left.val in d:
                if node.left.left:
                    ans.append(node.left.left)
                if node.left.right:
                    ans.append(node.left.right)
                node.left = None
            if node.right and node.right.val in d:
                if node.right.left:
                    ans.append(node.right.left)
                if node.right.right:
                    ans.append(node.right.right)
                node.right = None
        postorder(root)
        if root.val in d:
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
        else:
            ans.append(root)
        return ans