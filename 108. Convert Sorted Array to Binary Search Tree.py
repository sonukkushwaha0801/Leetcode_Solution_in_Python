# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
# Another way:

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def cv(node,vals)->TreeNode:
            if vals:
                mid=len(vals)//2
                node.val,node.left,node.right=vals[mid],cv(TreeNode(),vals[:mid]),cv(TreeNode(),vals[mid+1:])
                return node
            else:
                return None
        return cv(TreeNode(),nums)