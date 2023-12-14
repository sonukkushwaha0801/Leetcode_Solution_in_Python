# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first:
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack=[]
        parent=defaultdict(TreeNode)
        res=[]
        stack.append([root,0])
        while(stack):
            t=stack.pop()
            node=t[0]
            level=t[1]
            if node.val in [p.val,q.val]:
                res.append([node,level])
            if node.right:
                stack.append([node.right,level+1])
                parent[node.right]=node
            if node.left:
                stack.append([node.left,level+1])
                parent[node.left]=node
        p,pl=res[0][0],res[0][1]
        q,ql=res[1][0],res[1][1]
        if pl>ql:
            for i in range(pl-ql):
                p=parent[p]
                print(p.val)
        elif pl<ql:
            for i in range(ql-pl):
                q=parent[q]
                print(q.val)
        while(p.val!=q.val):
            p=parent[p]
            q=parent[q]
        return p
    
# Another way:
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left==None:
            return right
        elif right==None:
            return left
        else:
            return root