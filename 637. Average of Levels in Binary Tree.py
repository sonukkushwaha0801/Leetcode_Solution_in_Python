# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        s=defaultdict(int)
        n=defaultdict(int)
        def dfs(root,depth):
            s[depth]+=root.val
            n[depth]+=1
            if root.left: dfs(root.left,depth+1)
            if root.right: dfs(root.right,depth+1)
        dfs(root,0)
        ar=[]
        for i in s.keys():
            ar.append(s[i]/n[i])
        return ar
    
# Another way:

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        q.append(root)
        res=[]
        while q:
            qlen=len(q)
            list1=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    list1.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if list1:
                res.append(sum(list1)/len(list1))
        return res
            