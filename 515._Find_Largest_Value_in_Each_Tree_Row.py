# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # Check if the root is None (an empty tree)
        if not root:
            return []

        # Initialize an empty list to store the maximum values in each level
        result = []

        # Create a deque (double-ended queue) and add the root node to it
        queue = deque([root])

        # Perform a breadth-first traversal
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)

            # Initialize the maximum value to negative infinity
            max_val = float('-inf')

            # Iterate through all nodes at the current level
            for _ in range(level_size):
                # Remove the first node from the queue
                node = queue.popleft()

                # Update the maximum value if the current node's value is greater
                max_val = max(max_val, node.val)

                # Add the left and right children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the maximum value of the current level to the result list
            result.append(max_val)

        # Return the list containing the maximum values in each level
        return result

    
# Another way:
from collections import deque
from typing import List

class Solution:
    def largestValues(self, root) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            max_val = float('-inf')

            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_val)

        return result
