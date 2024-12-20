# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque


class Solution:
    def reverseOddLevels(self, root):
        if not root:
            return root

        queue = deque()
        queue.append(root) 

        nodes = []
        nodes.append([root]) 

        values = []
        values.append([root.val])

        while queue:
            value_level = []
            node_level = []
            for i in range(len(nodes[-1])):
                node = queue.popleft()

                if node.left:
                    node_level.append(node.left)
                    value_level.append(node.left.val)
                    queue.append(node.left)

                if node.right:
                    node_level.append(node.right)
                    value_level.append(node.right.val)
                    queue.append(node.right)

            nodes.append(node_level)
            values.append(value_level)


        for row in range(len(nodes)):
            if row % 2 != 0:
                for col in range(len(nodes[row])):
                    nodes[row][col].val = values[row][-col - 1] 
                
        return nodes[0][0]


# Another way:
class Solution:
    def reverseOddLevels(self, root):
        def dfs(leftChild, rightChild, level):
            if not leftChild or not rightChild:
                return
            if level % 2 == 1:  

                leftChild.val, rightChild.val = rightChild.val, leftChild.val
            dfs(leftChild.left, rightChild.right, level + 1)
            dfs(leftChild.right, rightChild.left, level + 1)

        dfs(root.left, root.right, 1)
        return root            