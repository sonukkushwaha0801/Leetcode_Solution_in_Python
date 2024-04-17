# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def smallestFromLeaf(self, n: Optional[TreeNode]) -> str:
        def f(n, q):
            if n:
                q = chr(97+n.val) + q
                minn = min(f(n.left, q), f(n.right, q))
                if n.left == n.right == None:
                    minn = q
                
                return minn

            return '~'
        
        return f(n, '')
    
# Another way:
class Solution:
    def smallestFromLeaf(self, n: Optional[TreeNode]) -> str:
        return (f:=lambda n,q:n and (min(f(l:=n.left,q:=chr(97+n.val)+q),f(r:=n.right,q)),q)[l==r==None] or '~')(n,'')