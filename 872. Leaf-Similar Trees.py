# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaf_values(root, leaf_values):
            if not root:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)

        leaf_values1 = []
        leaf_values2 = []

        collect_leaf_values(root1, leaf_values1)
        collect_leaf_values(root2, leaf_values2)

        return leaf_values1 == leaf_values2
    
# Another way:
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        return len(set(map(tuple, map(lambda root: (lambda root, func: [] if not root else ([root.val] if (not root.left and not root.right) else func(root.left, func) + func(root.right, func)))(root, (lambda root, func: [] if not root else ([root.val] if (not root.left and not root.right) else func(root.left, func) + func(root.right, func)))), (root1, root2))))) == 1