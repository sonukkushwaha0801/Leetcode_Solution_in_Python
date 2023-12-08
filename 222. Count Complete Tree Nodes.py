# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
      if root is None:
        return 0
      return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Another way:
class Solution:
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    l = root
    r = root
    heightL = 0
    heightR = 0

    while l:
      heightL += 1
      l = l.left

    while r:
      heightR += 1
      r = r.right

    if heightL == heightR:  # Root is a complete tree
      return pow(2, heightL) - 1
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)