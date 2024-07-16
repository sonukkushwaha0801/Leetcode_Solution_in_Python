# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False

        def findLCA(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right
        
        lca = findLCA(root, startValue, destValue)
        
        startPath = []
        findPath(lca, startValue, startPath)
        
        destPath = []
        findPath(lca, destValue, destPath)
   
        startPath = ['U'] * len(startPath)
    
        return ''.join(startPath) + ''.join(destPath)
    
# Another way:
class Solution:

    def dfs(self, root, startValue, destValue):
        if not root:
            return 0, ''

        direct_l, path_l = self.dfs(root.left, startValue, destValue)
        direct_r, path_r = self.dfs(root.right, startValue, destValue)
        
        direct = direct_l + direct_r - (root.val == startValue) + (root.val == destValue)

        if direct_l < 0:
            return (direct, path_l + 'UR' + path_r) if direct_r else (direct, path_l + 'U')
        elif direct_l > 0:
            return (direct, path_r + 'UL' + path_l) if direct_r else (direct, 'L' + path_l)
        elif direct_r < 0:
            return direct, path_r + 'U' 
        elif direct_r > 0:
            return direct, 'R' + path_r
        return direct, path_l + path_r

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        return self.dfs(root, startValue, destValue)[1]