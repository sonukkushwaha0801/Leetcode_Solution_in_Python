# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
from typing import List


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        children = set()
        for parent, child, isLeft in descriptions:
            parentNode = nodes.setdefault(parent, TreeNode(val=parent))
            childNode = nodes.setdefault(child, TreeNode(val=child))
            children.add(child)
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
        for node in nodes:
            if node not in children:
                return nodes[node]
            
# Another way:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        is_child = set()

        # Create all nodes
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)

        # Set up the tree structure
        for parent_val, child_val, is_left in descriptions:
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]

            is_child.add(child_val)

        # Identify and return the root node
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in is_child:
                return nodes[parent_val]

        return None