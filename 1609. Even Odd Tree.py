# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        level = 0

        while queue:
            prev_val = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val))):
                    return False

                prev_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
        return True
    
# Another way:
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 0)]
        current_value = 0
        current_index = 0
        while queue:
            root, index = queue.pop(0)
            if index % 2 == 0:
                if root.val % 2 == 0:
                    return False
                if index == current_index and root.val <= current_value:
                    return False
            else:
                if root.val % 2 != 0:
                    return False
                if index == current_index and root.val >= current_value:
                    return False
            current_index = index
            current_value = root.val
            if root.left:
                queue.append((root.left, index + 1))
            if root.right:
                queue.append((root.right, index + 1))
        return True