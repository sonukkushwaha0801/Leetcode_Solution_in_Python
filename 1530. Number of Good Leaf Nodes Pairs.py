# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]  

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.count += 1
            
            return [d + 1 for d in left_distances + right_distances if d + 1 <= distance]

        self.count = 0
        dfs(root)
        return self.count
    
# Another way:
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def visit(current: TreeNode, counter: int) -> list:
            if not current:
                return []
            left = visit(current.left, counter + 1)
            right = visit(current.right, counter + 1)
            if not current.left and not current.right:
                return [counter]
            for l in left:
                for r in right:
                    if l + r - 2 * counter <= distance:
                        self.result += 1
            return left + right
        visit(root, 0)
        return self.result