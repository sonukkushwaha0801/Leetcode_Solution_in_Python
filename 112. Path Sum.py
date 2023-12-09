# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first

import collections
from pyparsing import Optional


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        queue = collections.deque([(root, root.val)])
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                if val == targetSum: return True
                else: continue
            if node.left:
                queue.append((node.left, val + node.left.val))   
            if node.right:
                queue.append((node.right, val + node.right.val))   
        return False
    
# Another way:
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        #what if we are given an empty tree?
        if not root:
            return False
        #this 
        flag = 0
        def dfs(root,pathSumSoFar):
            nonlocal flag
            if flag==0:
                if not root.left and not root.right:
                    pathSumSoFar+=root.val
                    if targetSum==pathSumSoFar:
                        flag = 1
                    return 
                if flag:
                    return
                if root.left:
                    dfs(root.left,pathSumSoFar+root.val)
                if root.right:
                    dfs(root.right,pathSumSoFar+root.val)
            return
        dfs(root,0)
        return flag==1
         