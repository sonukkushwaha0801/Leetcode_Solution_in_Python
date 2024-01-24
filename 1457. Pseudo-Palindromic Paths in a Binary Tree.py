# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def pseudoPalindromicPaths(self, root) -> int:
        def dfs(root, mask: int):
            if root is None:
                return 0
            mask ^= 1 << root.val
            if root.left is None and root.right is None:
                return int((mask & (mask - 1)) == 0)
            return dfs(root.left, mask) + dfs(root.right, mask)

        return dfs(root, 0)

# Another way:

class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        ans=0
        def search(node,even):
            if node==None:
                return
            even[node.val]= not even[node.val]
            if node.left==None and node.right==None:
                if sum(even)<=1:
                    nonlocal ans
                    ans+=1
            else:
                search(node.left,even)
                search(node.right,even)
            even[node.val]= not even[node.val]
        search(root,[False]*10)
        return ans                    