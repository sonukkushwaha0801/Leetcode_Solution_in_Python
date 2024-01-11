# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxVal = 0

        queue = deque([(root, root.val, root.val)])
        while queue:
            curr, high, low = queue.popleft()
            currVal = curr.val
            diff1, diff2 = currVal - low, high - currVal
            maxVal = max(maxVal, diff1, diff2)

            if curr.left:
                queue.append((curr.left, max(currVal, high), min(currVal, low)))
            if curr.right:
                queue.append((curr.right, max(currVal, high), min(currVal, low)))
        return maxVal

# Another way:
class Solution:
    def maxAncestorDiff(self, r: Optional[TreeNode]) -> int:
        return (f:=lambda n,a,b:max(f(n.left,a:=min(a,n.val),b:=max(b,n.val)),f(n.right,a,b)) if n else b-a)(r,r.val,r.val)