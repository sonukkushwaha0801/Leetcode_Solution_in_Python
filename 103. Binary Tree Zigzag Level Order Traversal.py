# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

from collections import defaultdict, deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth % 2 == 0: ans[depth].append(node.val)
            else: ans[depth].insert(0, node.val)
            if node.left: queue.append((node.left, depth+1))
            if node.right: queue.append((node.right, depth+1))
        return ans.values()

# Another way:
class Solution:
    def zigzagLevelOrder(self, root_: TreeNode | None) -> list[list[int]]:
        def zigzag_level_order(root: TreeNode | None) -> Iterator[TreeNode]:
            level = (root,) if root else ()
            reverse = False
            while level:
                yield reversed(level) if reverse else iter(level)
                level = tuple(child for node in level for child in (node.left, node.right) if child)
                reverse = not reverse
        
        return [[node.val for node in level] for level in zigzag_level_order(root_)]

                