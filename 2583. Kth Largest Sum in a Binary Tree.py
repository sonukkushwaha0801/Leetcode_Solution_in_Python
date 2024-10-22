# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        q = [root]
        while q:
            temp = []
            sm = 0
            for i in q:
                sm += i.val
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if len(h) < k:
                heappush(h, sm)
            else:
                if sm > h[0]:
                    heappop(h)
                    heappush(h, sm)
            q = temp
        return (h[0] if len(h) == k else -1)
        
# Another way:
class Solution:
    def __init__(self):
        self.n = 0
        self.lvls = [0] * 10**5

    def traverse(self, node, lvl):
        if lvl > self.n:
            self.n = lvl
        self.lvls[lvl] += node.val
        if node.right:
            self.traverse(node.right, lvl + 1)
        if node.left:
            self.traverse(node.left, lvl + 1)
        return

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        k = k - 1
        self.traverse(root, 0)
        if k > self.n:
            return -1
        return sorted(self.lvls[: self.n + 1], reverse=True)[k]