# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
class Solution:
    ans = float('-inf')    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root) :
            if root:
                lmax = dfs(root.left)
                rmax = dfs(root.right)                
                curr = root.val
                cmax = max(curr,curr+lmax,curr+rmax,lmax+curr+rmax)
                if cmax > self.ans :
                    self.ans = cmax                
                return max(curr,curr+lmax,curr+rmax)
            else:
                return 0
        dfs(root)
        return self.ans
        
# Another way:
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxs=float('-inf')
        self.maxSum(root,self.maxs)
        return self.maxs
    
    def maxSum(self,root,maxs):
        if root is None:
            return 0
        ls=max(0,self.maxSum(root.left,self.maxs))
        rs=max(0,self.maxSum(root.right,self.maxs))
        self.maxs=max(self.maxs,root.val+ls+rs)
        return root.val+max(ls,rs)