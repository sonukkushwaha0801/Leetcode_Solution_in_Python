# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        queue1 = deque([(1, None, root)])
        queue2 = []
        values = defaultdict(int)
        parents = defaultdict(int)
        parents[None] = root.val
        while queue1:           
            level, _, node = tree_node = queue1.popleft()    
            queue2.append(tree_node)       
            values[level] += node.val
            if node.left:
                parents[node] += node.left.val
                queue1.append((level + 1, node, node.left))
            if node.right:
                parents[node] += node.right.val
                queue1.append((level + 1, node, node.right))
        
        for level, parent, node in queue2:
            node.val = values[level] - parents[parent]
        return root
        
# Another way:
class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        q = deque([root])
        level_sum = []

        # First BFS to compute level sums
        while q:
            level_size = len(q)
            level_total = 0
            for _ in range(level_size):
                node = q.popleft()
                level_total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(level_total)

        # Second BFS to replace node values
        q.append(root)
        root.val = 0
        level = 0

        while q:
            level_size = len(q)
            next_level_sum = level_sum[level + 1] if level + 1 < len(level_sum) else 0

            for _ in range(level_size):
                node = q.popleft()
                child_sum = 0

                if node.left:
                    child_sum += node.left.val
                    q.append(node.left)
                if node.right:
                    child_sum += node.right.val
                    q.append(node.right)

                if node.left:
                    node.left.val = next_level_sum - child_sum
                if node.right:
                    node.right.val = next_level_sum - child_sum

            level += 1

        return root